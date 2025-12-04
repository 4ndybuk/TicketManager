"""
Login module to access the database
Uses Supabase database to control and monitor data
"""

import os
import json
from supabase import create_client, Client
from dotenv import load_dotenv
from PySide6.QtWidgets import QMessageBox

def message_box(title,text):
        messagebox = QMessageBox()
        messagebox.setWindowTitle(title)
        messagebox.setText(text)
        messagebox.setIcon(QMessageBox.Critical)
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.setStandardButtons(QMessageBox.Ok)
        messagebox.exec()

# Load URL and KEY for the database
load_dotenv("./.env")
if "SUPABASE_URL" in os.environ and "SUPABASE_KEY" in os.environ:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
else:
    message_box("Initialising Error",
                "Missing URL and API Key for the database\n")

def login(username: str, password: str, page):
        try:
            # Sing-in to the database
            response = supabase.auth.sign_in_with_password(
                {
                    "email": username,
                    "password": password
                }
            )
            # Send to the next page
            page.setCurrentIndex(1)
            # Return client
            return supabase
        except Exception as e:
            print(e)
            message_box("Login Error",
                        "Incorrect login credentials\n\nPlease try again")
            return
    
def logout(page):
     supabase.auth.sign_out()
     message_box("Logout",
                 "You have been logged out")
     page.setCurrentIndex(0)
