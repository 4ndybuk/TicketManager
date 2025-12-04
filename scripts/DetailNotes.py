"""
Pop-up window to store and read ticket details
"""

from PySide6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, 
                               QTextEdit, QMessageBox, QHBoxLayout, QLabel)
import supabase

class DetailsDialog(QDialog):
    def __init__(self, row_id: int, client: supabase.Client):
        super().__init__()
        self.row_id = row_id
        self.client = client

        label = QLabel("Ticket Description:")
        label.setFont("JetBrains Mono NL")
        
        self.editor = QTextEdit()
        self.load_text()

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

        save_button = QPushButton("Save")
        save_button.setStyleSheet(buttonstyle)
        save_button.clicked.connect(self.save_text)

        close_button = QPushButton("Close")
        close_button.setStyleSheet(buttonstyle)
        close_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        hor_layout = QHBoxLayout()
        hor_layout.addWidget(save_button)
        hor_layout.addWidget(close_button)
        layout.addWidget(label)
        layout.addWidget(self.editor)
        layout.addLayout(hor_layout)
        self.setLayout(layout)
        self.setWindowTitle("Ticket Details")

    def load_text(self):
        try:
            response = (
                self.client.table("SafetyManager")
                .select("Details")
                .eq("id", self.row_id)
                .single()
                .execute()
            )
            self.editor.setPlainText(str(response.data["Details"]))
        except Exception as e:
            print(e)
            pass
    
    def save_text(self):
        text = self.editor.toPlainText()
        self.client.table("SafetyManager").update({"Details": str(text)}).eq("id", self.row_id).execute()
        QMessageBox.information(None, "Save", "Details saved", QMessageBox.Ok)