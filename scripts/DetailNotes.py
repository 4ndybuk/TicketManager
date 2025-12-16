"""
Pop-up window to store and read ticket details
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, 
                               QTextEdit, QMessageBox, QHBoxLayout, QLabel,
                               QTabWidget, QInputDialog)
import supabase
from datetime import datetime

class DetailsDialog(QDialog):
    def __init__(self, row_id: int, client: supabase.Client, tab_no: int):
        super().__init__()
        self.row_id = row_id
        self.client = client

        # Create tabs widget
        tabs = QTabWidget()

        # Button stylesheet
        buttonstyle = """
        QPushButton {
                background-color: rgb(177, 180, 180);
                border: 2px solid #000000;
                border-radius: 10px;
                padding: 6px 12px;
                font-size: 13px;
                color: #000000;
                text-align: center;
                }
        QPushButton:hover {
                background-color: rgba(134, 135, 135, 0.9);
                border: 3px solid #000000
                }
        QPushButton:pressed {
                background-color: rgb(134, 135, 135);
                border: 2px solid #717171;
                }
                """

        # Edit Tab
        edit_tab = QTabWidget()

        save_button = QPushButton("Save")
        save_button.setStyleSheet(buttonstyle)
        save_button.clicked.connect(self.save_text)

        close_button = QPushButton("Close")
        close_button.setStyleSheet(buttonstyle)
        close_button.clicked.connect(self.accept)

        edit_label = QLabel("Ticket Description:")
        edit_label.setFont("JetBrains Mono NL")

        self.editor = QTextEdit()

        edit_layout = QVBoxLayout()
        h_edit_layout = QHBoxLayout()
        h_edit_layout.addWidget(save_button)
        h_edit_layout.addWidget(close_button)
        edit_layout.addWidget(edit_label)
        edit_layout.addWidget(self.editor)
        edit_layout.addLayout(h_edit_layout)
        edit_tab.setLayout(edit_layout)
        edit_tab.setWindowTitle("Ticket Details")

        # History Tab

        hist_tab = QTabWidget()

        hist_label = QLabel("Ticket History")
        hist_label.setFont("JetBrains Mono NL")

        self.reader = QTextEdit()
        self.reader.setReadOnly(True)
        self.load_reader()

        hist_layout = QVBoxLayout()
        hist_layout.addWidget(hist_label)
        hist_layout.addWidget(self.reader)
        hist_tab.setLayout(hist_layout)
        hist_tab.setWindowTitle("Ticket History")

        # Add the tabs
        tabs.addTab(edit_tab, "Edit")
        tabs.addTab(hist_tab, "History")

        layout = QVBoxLayout()
        layout.addWidget(tabs)

        # Turn off functions for the Deleted tab
        if tab_no == 4:
            save_button.setEnabled(False)
            self.editor.setReadOnly(True)
            # Show history upon opening
            tabs.setCurrentIndex(1)

        self.setLayout(layout)

        self.setWindowTitle("Ticket Details")
    
    def user_name(self):
        # Retrieve user's name
        name, ok = QInputDialog.getText(None, "Signoff Name", "Please insert your name for signoff")
        if ok:
            return name
        return None
    
    def load_reader(self):
        # Load the text into the reader
        try:
            response = (
                self.client.table("SafetyManager")
                .select("History")
                .eq("id", self.row_id)
                .single()
                .execute()
            )
            # Write data into the editor
            self.reader.setReadOnly(False)
            self.reader.setPlainText(response.data["History"])
            self.reader.setReadOnly(True)
        except Exception as e:
            print(e)
            pass
    
    def save_text(self):
        # Save and upload the text
        text = self.editor.toPlainText()
        date_time = datetime.now()
        # Safety check for giving name input
        name = self.user_name()
        if name == "":
            QMessageBox.critical(None, "Empty Name", "Please provide your name", QMessageBox.Ok)
            return
        elif name is None:
            return
        else:
            name_text = f"Saved by {name} at {date_time.strftime("%d/%m/%Y %H:%M:%S")}"
            full_text = text + "\n" + name_text
            # Update the history column in the database
            self.client.rpc("append_signature", {"row_id": self.row_id, "extra_text": str(full_text)}).execute()
            QMessageBox.information(None, "Save", "Details saved", QMessageBox.Ok)
            # Reload the reader
            self.load_reader()