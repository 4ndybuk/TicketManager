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
        self.table.setColumnHidden(7, True)

        # Table Page Setup
        self.ui.createButton.clicked.connect(self.create_ticket)
        self.ui.logoutButton.clicked.connect(self.signout)
        self.ui.deleteButton.clicked.connect(self.delete_row)
        self.ui.refreshButton.clicked.connect(self.refresh)
    
    def login(self):
        # Login to the database and return client
        username = self.ui.userInput.text()
        password = self.ui.passInput.text()
        self.next_page = self.ui.stackedWidget
        client = login(username, password, self.next_page)
        self.client = client

        # Fetch all data from the database
        self.all_data = self.client.table("SafetyManager").select("*", count='exact').execute().data
        self.table_control = TableController(self.ui.tableWidget, self.client, self.all_data)
        self.table_control.load_table()

    def signout(self):
        # Logout from the database~
        logout(self.next_page)
        self.ui.userInput.clear()
        self.ui.passInput.clear()
        self.ui.tableWidget.clear()
        self.ui.userInput.setFocus()
    
    def create_ticket(self):
        # Creating a table row for the ticket
        self.table_control.create_ticket()

    def refresh(self):
        self.all_data = self.client.table("SafetyManager").select("*", count='exact').execute().data
        self.ui.tableWidget.setRowCount(0)
        self.table_control = TableController(self.ui.tableWidget, self.client, self.all_data)
        self.table_control.load_table()
    
    def delete_row(self):
        item = self.ui.tableWidget.currentItem()
        if item is None:
            QMessageBox.critical(None, "Delete Ticket", "Click on the row to delete it", QMessageBox.Ok)
            return
        
        # Delete row from the table and database
        row = item.row()
        id_item = self.table.item(row, 6)
        row_id = int(id_item.text())
        self.client.table("SafetyManager").delete().eq("id", row_id).execute()
        self.table.removeRow(row)

        # Refresh the table to maintain proper button binding
        self.refresh()

def main():
    app = QApplication(sys.argv)
    clipboard = app.clipboard()

    window = SafetyManager(clipboard)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()