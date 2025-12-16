# List of CSS stylsheets used for main GUI widgets

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

# Stylesheet for the interface text displays
lineedit_style = """
                QLineEdit {
                    background: transparent;
                    background-color: rgba(177, 180, 180, 0.8);
                    border-radius: 10px;
                    border: 2px solid #000000;
                    color: rgb(0, 0, 0);
                }
                QMenu {
                    background-color: #F0F0F0;   
                    border: 2px solid #C0C0C0;   
                    border-radius: 6px;
                    padding: 3px;         
                }
                QMenu::item {
                    background-color: transparent; 
                }
                QMenu::item:selected { 
                    background-color: rgb(177, 180, 180);    
                    color: black;                
                    border-radius: 4px;
                }
                QMenu::separator {
                    height: 1px;                  
                    background: rgb(177, 180, 180);          
                    margin-left: 10px;
                    margin-right: 10px;
                }
                QMenu::indicator {
                    width: 16px;                  
                    height: 16px;
                }
                QMenu::indicator:checked {
                    background-color: rgb(177, 180, 180);    
                }
                QMenu::item:disabled {
                    color: #A0A0A0;                
                }
                """

table_style = """
                QTableWidget {
                    background: transparent;   
                    background-color: rgba(255, 255, 255, 0.8);
                    padding: 1px;
                }                    
                QTableWidget::item:selected {
                    background: transparent; 
                    background-color: rgba(177, 180, 180, 0.6);
                    padding: 2px
                }                 
                QTableWidget::item:focus {
                    background-color: rgba(177, 180, 180, 0.6);
                    outline: none;                      
                }                   
                QScrollBar:vertical {
                    background: transparent;
                    width: 8px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: rgba(0, 0, 0, 0.5);
                    border-radius: 4px;
                }
                QScrollBar::handle:vertical:hover {
                    background: rgba(0, 0, 0, 0.8);
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    border: none;
                    background: none;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                """

toolbar_style = """
                QToolBar {
                    background: none
                }
                QToolButton {
                    background-color: lightgray;
                    border: 1px lightgray;
                    padding: 2px;
                    background: none;
                    border-radius: 5px
                }
                QToolButton:hover {
                    background-color: darkgray;
                }
                """

textedit_style = """
            QTextEdit {
                background: transparent;
                background-color: rgba(255, 255, 255, 0.7);
                border: 1px solid #c0c0c0;
                border-radius: 8px;
                padding: 10px;
            }
            QScrollBar:vertical {
                background: transparent;
                width: 8px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: rgba(0, 0, 0, 0.5);
                border-radius: 4px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(0, 0, 0, 0.8);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
            QMenu {
                background-color: #F0F0F0;   
                border: 1px solid #C0C0C0;   
                border-radius: 6px;
                padding: 3px;        
            }
            QMenu::item {
                background-color: transparent; 
            }
            QMenu::item:selected { 
                background-color: lightgray;    
                color: black;                
                border-radius: 4px;
            }
            QMenu::separator {
                height: 1px;                  
                background: #F0F0F0;          
                margin-left: 10px;
                margin-right: 10px;
            }
            QMenu::indicator {
                width: 16px;                  
                height: 16px;
            }
            QMenu::indicator:checked {
                background-color: #bfd0e0;    
            }
            QMenu::item:disabled {
                color: #A0A0A0;                
            }
        """