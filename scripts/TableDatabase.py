"""
TableDatabase.py

Appending table widget and updating the remote database

"""
import os
import re
import supabase
import random
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem, QPushButton, 
                               QInputDialog, QLabel, QAbstractItemView, QApplication, 
                               QMessageBox)

from DetailNotes import DetailsDialog
from datetime import datetime
import webbrowser
import urllib.parse

class TableController:
    def __init__(self, table: QTableWidget, client: supabase.Client, data, tab_no: int):
        self.table = table
        self.client = client
        self.data = data
        self.tab_no = tab_no

    def create_ticket(self):
        # Add a new row at the end of the table
        # row_position = self.table.rowCount()
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Disable sorting when filling in the rows
        self.table.setSortingEnabled(False)
        # Disable editing
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Button references
        status_button = QPushButton()
        status_button.setCheckable(True)
        details_button = QPushButton()
        report_button = QPushButton()

        # Outputs
        ticket_str = self.input_dialog("Ticket Name", "Name of the ticket:")
        id_str = self.generate_id()
        location_str = self.input_dialog("Cleanroom Location", "Cleanroom location e.g. G15:")
        urgency_str = self.choice_dialog()

        # Defining table text items
        ticket_name = QTableWidgetItem(ticket_str)
        ticket_name.setTextAlignment(Qt.AlignCenter)

        ticket_id = QTableWidgetItem(id_str)
        ticket_id.setTextAlignment(Qt.AlignCenter)

        urgency = QTableWidgetItem(urgency_str)
        urgency.setTextAlignment(Qt.AlignCenter)

        location = QTableWidgetItem(location_str)
        location.setTextAlignment(Qt.AlignCenter)

        # Database dictionary
        row_dict = {
            "Ticket Name": ticket_str,
            "Ticket ID": id_str,
            "Urgency": urgency_str,
            "Cleanroom Location": location_str,
            "Status": "Active",
            "Details": "",
            "History": "",
            "Tab": self.tab_no
        }

        # Insert row into the database
        response = self.client.table("SafetyManager").insert(row_dict).execute()

        # Return row ID
        row_id = response.data[0]["id"]

        # Storing the ID in a hidden column
        self.table.setItem(row_position, 6, QTableWidgetItem(str(row_id)))

        # Update the Ticket ID into the Details history
        self.client.rpc("append_signature", {"row_id": row_id, "extra_text": str(f"Ticket ID: {id_str}")}).execute()

        # Button functions
        self.trigger_button(status_button, "Active", "green", lambda _, r = row_position: self.toggle_status(r))
        self.trigger_button(details_button, "Details", "black", lambda _, r = row_position: self.open_details(r))
        self.trigger_button(report_button, "Report", "black", lambda _, r = row_position: self.mail_to(r))

        # Append the table row for display
        self.table.setItem(row_position, 0, ticket_name)
        self.table.setItem(row_position, 1, ticket_id)
        self.table.setItem(row_position, 2, urgency)
        self.table.setItem(row_position, 3, location)
        self.table.setCellWidget(row_position, 4, status_button)
        self.table.setCellWidget(row_position, 5, details_button)
        self.table.setCellWidget(row_position, 7, report_button)

        # Enable sorting after filling in the rows
        self.table.setSortingEnabled(True)

    def input_dialog(self, title: str, maintext: str):
        # Cell text input
        text, ok = QInputDialog.getText(None, title, maintext)
        if ok:
            return text
        return None
    
    def generate_id(self):
        # Generate a unique 6-digit ticket ID
        id_check = {row['Ticket ID'] for row in self.data}
        while True:
            random_id = str(random.randint(0,999999)).zfill(6)
            if random_id not in id_check:
                return random_id

    def choice_dialog(self):
        # Choose the urgency level of the ticket
        items = ["Urgent", "Medium", "Low"]
        item, ok = QInputDialog.getItem(None, "Urgency Selection", "Choose the urgency:", items, 0, False)
        if ok and item:
            return item
        return None

    def trigger_button(self, button: QPushButton, label: str, colour: str, callback):
        # Generic method for the buttons
        button.setText(label)
        button.setStyleSheet("background: none;\n"
                            f"color: {colour}")
        button.clicked.connect(callback)
        font = QFont("JetBrains Mono NL")
        font.setBold(True)
        button.setFont(font)

    def toggle_status(self, row_position):
        # Toggle the activity status button between Active and Completed
        id_item = self.table.item(row_position, 6)        
        row_id = int(id_item.text())
        button = self.table.cellWidget(row_position, 4)

        def user_signature(value: str):
            # Retrieve staff name for toggle updates
            user_name = self.input_dialog("Username", "Please input your name for the status update")
            if user_name == "":
                QMessageBox.critical(None, "Empty Name", "Please provide your name", QMessageBox.Ok)
                return None
            elif user_name is None:
                return None
            date_time = datetime.now()
            user_signature = f"\n\n•Ticket signed off as {value} by {user_name} at {date_time.strftime("%d/%m/%Y %H:%M:%S")}•"
            return user_signature

        if button.isChecked():
            value = "Completed"
            user_signature = user_signature(value)
            if user_signature is None:
                return
            else: 
                button.setText(value)
                button.setStyleSheet("background: transparent;\n"
                                    "color: gray")
        else:
            value = "Active"
            user_signature = user_signature(value)
            if user_signature is None:
                return
            else:
                button.setText(value)
                button.setStyleSheet("background: transparent;\n"
                                    "color: green")
        # Update the status in database
        self.client.table("SafetyManager").update({"Status": value}).eq("id", row_id).execute()
        # Update the details with user signature
        self.client.rpc("append_signature", {"row_id": row_id, "extra_text": str(user_signature)}).execute()

    def open_details(self, row_position):
        # Open the input window for ticket details
        id_item = self.table.item(row_position, 6)
        row_id = int(id_item.text())
        details = DetailsDialog(row_id, self.client)
        details.resize(550,450)
        details.exec()
    
    def mail_to(self, row_position):
        # Drafting a pre-filled mail for ticket reporting
        id_item = self.table.item(row_position, 6)
        ticket_item = self.table.item(row_position, 0)
        location_item = self.table.item(row_position, 3)
        
        # Retrieving relative row information per button
        row_id = int(id_item.text())
        row_ticket = str(ticket_item.text())
        row_location = str(location_item.text())

        # Fetching details information
        response = (
                self.client.table("SafetyManager")
                .select("History")
                .eq("id", row_id)
                .single()
                .execute()
            )
        
        recipient = "mikel@liverpool.ac.uk"
        subject = f"Safety Ticket - {row_ticket} at {row_location} - Report"
        contents = response.data["History"]
        body = f"Hello Mike,\n\n I am including the cleanroom safety ticket for your perusal:\n{contents}"
        mail_to = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
        webbrowser.open(mail_to)
    
    def load_table(self):
        # Load data after login
        self.table.setSortingEnabled(False)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        def item_and_align(item):
            widget_item = QTableWidgetItem(item)
            widget_item.setTextAlignment(Qt.AlignCenter)
            return widget_item

        self.row_position = 0
        for row in self.data:
            if row["Tab"] == self.tab_no:
                status_button = QPushButton()
                status_button.setCheckable(True)
                details_button = QPushButton()
                report_button = QPushButton()

                self.table.insertRow(self.row_position)
                self.table.setItem(self.row_position, 6, QTableWidgetItem(str(row["id"])))

                if row["Status"] == "Active":
                    self.trigger_button(status_button, row["Status"], "green", 
                                        lambda _, r = self.row_position: self.toggle_status(r))
                else:
                    self.trigger_button(status_button, row["Status"], "gray", 
                                        lambda _, r = self.row_position: self.toggle_status(r))

                self.trigger_button(details_button, "Details", "black", lambda _, r = self.row_position: self.open_details(r))
                self.trigger_button(report_button, "Report", "black", lambda _, r = self.row_position: self.mail_to(r))
                
                self.table.setItem(self.row_position, 0, item_and_align(row["Ticket Name"]))
                self.table.setItem(self.row_position, 1, item_and_align(row["Ticket ID"]))
                self.table.setItem(self.row_position, 2, item_and_align(row["Urgency"]))
                self.table.setItem(self.row_position, 3, item_and_align(row["Cleanroom Location"]))
                self.table.setCellWidget(self.row_position, 4, status_button)
                self.table.setCellWidget(self.row_position, 5, details_button)
                self.table.setCellWidget(self.row_position, 7, report_button)

                self.row_position += 1
            
        self.table.setSortingEnabled(True)
