DEBUG = False

import os
import sys

# Include the nested folders with modules and assets for importing
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'assets'))

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QClipboard, QAction, QFont

from main_gui import Ui_MainWindow, toolbar_style # type: ignore
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

        # Set font
        font = QFont("JetBrains Mono NL")

        # Set up a toolbar
        self.toolbar = QToolBar("Toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(12,12))
        self.toolbar.setStyleSheet(toolbar_style)
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.hide()

        # Default API variables
        self.client = None
        self.all_data = None

        # Toolbar actions
        # Search tickets by name
        search_name = QAction("Search by Name", self)
        search_name.triggered.connect(lambda: self.filter_table("creator"))
        search_name.setFont(font)
        self.toolbar.addAction(search_name)

        # Search ticket by project
        search_project = QAction("Search by Project", self)
        search_project.triggered.connect(lambda: self.filter_table("project"))
        search_project.setFont(font)
        self.toolbar.addAction(search_project)

        # Search tickets by location
        search_location = QAction("Search by Location", self)
        search_location.triggered.connect(lambda: self.filter_table("location"))
        search_location.setFont(font)
        self.toolbar.addAction(search_location)

        # Reset all search filters
        show_all = QAction("Show All", self)
        show_all.triggered.connect(self.show_all_action)
        show_all.setFont(font)
        self.toolbar.addAction(show_all)

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
        self.toolbar.show()

    def signout(self):
        # Logout from the database~
        logout(self.next_page)
        self.toolbar.hide()
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
        table.clearContents()
        table.setRowCount(0)
        table.setSortingEnabled(False)
        self.table_controller = TableController(table, self.client, self.all_data, tab_no)
        self.table_controller.load_table()
        table.setSortingEnabled(True)
    
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
    
    def show_all_action(self):
        self.refresh(self.table, 1)
        self.refresh(self.table2, 2)
        self.refresh(self.table3, 3)
    
    def filter_table(self, filter_name: str):
        # Filter the table based on the search preference
        match filter_name:
            case "creator":
                filter_str = self.table_control.input_dialog("Search", "Search by creator name:")
                dict_str = "Creator"
            case "project":
                filter_str = self.table_control.project_dialog()
                dict_str = "Project"
            case "location":
                filter_str = self.table_control.input_dialog("Search", "Search by location e.g G15:")
                dict_str = "Cleanroom Location"
            case _:
                return
        
        if filter_str == "":
            QMessageBox.critical(None, "Filter Error", "Please provide a valid input", QMessageBox.Ok)
            return
        elif filter_str is None:
            return
            
        # Load the full data for repeated filtering
        self.all_data = self.client.table("SafetyManager").select("*", count='exact').execute().data 
        # Filter the data
        filtered_list = []
        for row in self.all_data:
            if row[dict_str] == str(filter_str):
                filtered_list.append(row)
        self.all_data = filtered_list

        if len(self.all_data) < 1:
            QMessageBox.critical(None, "Filter Info", "No tickets found!", QMessageBox.Ok)
            return
        else:
            # Clear tables and load filtered data
            self.table.setRowCount(0)
            self.table2.setRowCount(0)
            self.table3.setRowCount(0)
            self.table_control = TableController(self.table, self.client, self.all_data, 1)
            self.table_control2 = TableController(self.table2, self.client, self.all_data, 2)
            self.table_control3 = TableController(self.table3, self.client, self.all_data, 3)
            self.table_control.load_table()
            self.table_control2.load_table()
            self.table_control3.load_table()

def main():
    app = QApplication(sys.argv)
    clipboard = app.clipboard()

    window = SafetyManager(clipboard)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()