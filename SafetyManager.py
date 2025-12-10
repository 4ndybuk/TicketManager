DEBUG = False

import os
import sys

# Include the nested folders with modules and assets for importing
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'assets'))

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QClipboard

from main_gui import Ui_MainWindow # type: ignore
from Login import login, logout # type: ignore
from TableDatabase import TableController # type: ignore

class SafetyManager(QMainWindow):
    def __init__(self, clipboard):
        super(SafetyManager,self).__init__()

        # Create an instance of the Ui_Mainwindow class
        self.ui = Ui_MainWindow()

        # Set up the UI for this window
        self.ui.setupUi(self)

        # Set up system wide clipboard
        self.clipboard = clipboard

        self.client = None
        self.all_data = None

        if DEBUG:
            page = self.ui.stackedWidget.setCurrentIndex(1)
        else:
            page = self.ui.stackedWidget.setCurrentIndex(0)

        # Login Page Setup
        # Set password to be masked with * markers
        self.ui.passInput.setEchoMode(QLineEdit.Password)

        # Set focus on username line
        self.ui.userInput.setFocus()

        # Connect entry buttons
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.quitButton.clicked.connect(quit)

        # Hide non-interactive columns on the next page
        self.table = self.ui.tableWidget
        self.table.setColumnHidden(6, True)

        self.table2 = self.ui.table_2_Widget
        self.table2.setColumnHidden(6, True)

        self.table3 = self.ui.table_3_Widget
        self.table3.setColumnHidden(6, True)

        # Table 1 Page Setup (Safety)
        self.ui.create1Button.clicked.connect(lambda: self.create_ticket(self.table_control))
        self.ui.logout1Button.clicked.connect(self.signout)
        self.ui.delete1Button.clicked.connect(lambda: self.delete_row(self.table, 1))
        self.ui.refresh1Button.clicked.connect(lambda: self.refresh(self.table, 1))

        # Table 2 Page Setup (General)
        self.ui.create2Button.clicked.connect(lambda: self.create_ticket(self.table_control2))
        self.ui.logout2Button.clicked.connect(self.signout)
        self.ui.delete2Button.clicked.connect(lambda: self.delete_row(self.table2, 2))
        self.ui.refresh2Button.clicked.connect(lambda: self.refresh(self.table2, 2))

        # Table 3 Page Setup (Stock)
        self.ui.create3Button.clicked.connect(lambda: self.create_ticket(self.table_control3))
        self.ui.logout3Button.clicked.connect(self.signout)
        self.ui.delete3Button.clicked.connect(lambda: self.delete_row(self.table3, 3))
        self.ui.refresh3Button.clicked.connect(lambda: self.refresh(self.table3, 3))
    
    def login(self):
        # Login to the database and return client
        username = self.ui.userInput.text()
        password = self.ui.passInput.text()
        self.next_page = self.ui.stackedWidget
        client = login(username, password, self.next_page)
        self.client = client

        # Fetch all data from the database
        self.all_data = self.client.table("SafetyManager").select("*", count='exact').execute().data
        self.table_control = TableController(self.table, self.client, self.all_data, 1)
        self.table_control2 = TableController(self.table2, self.client, self.all_data, 2)
        self.table_control3 = TableController(self.table3, self.client, self.all_data, 3)
        self.table_control.load_table()
        self.table_control2.load_table()
        self.table_control3.load_table()

    def signout(self):
        # Logout from the database~
        logout(self.next_page)
        self.ui.userInput.clear()
        self.ui.passInput.clear()
        self.table.setRowCount(0)
        self.table2.setRowCount(0)
        self.table3.setRowCount(0)
        self.ui.userInput.setFocus()
    
    def create_ticket(self, table_control):
        # Creating a table row for the ticket
        table_control.create_ticket()

    def refresh(self, table: QTableWidget, tab_no: int):
        self.all_data = self.client.table("SafetyManager").select("*", count='exact').execute().data
        table.setRowCount(0)
        self.table_controller = TableController(table, self.client, self.all_data, tab_no)
        self.table_controller.load_table()
    
    def delete_row(self, table: QTableWidget, tab_no: int):
        item = table.currentItem()
        if item is None:
            QMessageBox.critical(None, "Delete Ticket", "Click on the row to delete it", QMessageBox.Ok)
            return
        
        # Delete row from the table and database
        row = item.row()
        id_item = table.item(row, 6)
        row_id = int(id_item.text())
        self.client.table("SafetyManager").delete().eq("id", row_id).execute()
        table.removeRow(row)

        # Refresh the table to maintain proper button binding
        self.refresh(table, tab_no)

def main():
    app = QApplication(sys.argv)
    clipboard = app.clipboard()

    window = SafetyManager(clipboard)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()