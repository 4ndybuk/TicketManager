# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QLabel, QLineEdit, QMenuBar, QPushButton,
    QStackedWidget, QStatusBar, QTableWidget, QWidget)
import background_rc

# Stylesheet for the interface buttons

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 801, 601))
        font = QFont()
        font.setFamilies([u"JetBrains Mono NL"])
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        "background-repeat: no-repeat;\n"
        "background-image: url(:/1/background.png);\n"
        "color: black")
        ###############################################################
        # LOGIN PAGE 
        self.loginPage = QWidget()
        self.loginPage.setObjectName(u"loginPage")
        self.loginPage.setStyleSheet(u"background-color: transparent;")
        self.appTitle = QLabel(self.loginPage)
        self.appTitle.setObjectName(u"appTitle")
        self.appTitle.setGeometry(QRect(0, 0, 801, 131))
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono NL"])
        font1.setPointSize(42)
        font1.setBold(True)
        font1.setItalic(False)
        self.appTitle.setFont(font1)
        self.appTitle.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);\n"
        "color: black;\n"
        "background: none;\n")
        self.loginButton = QPushButton(self.loginPage)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(350, 350, 111, 31))
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet(buttonstyle)
        self.loginButton.setCheckable(True)
        self.loginButton.setChecked(False)
        self.loginButton.setAutoDefault(False)
        self.loginButton.setFlat(False)
        self.usernameLabel = QLabel(self.loginPage)
        self.usernameLabel.setObjectName(u"usernameLabel")
        self.usernameLabel.setGeometry(QRect(340, 198, 131, 31))
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet(u"border-radius: 8px;\n"
        "border: 0px solid #000000;\n"
        "background: transparent;\n"
        "background-color: rgba(177, 180, 180, 0.7);\n"
        "color: rgb(0, 0, 0);")
        self.passInput = QLineEdit(self.loginPage)
        self.passInput.setObjectName(u"passInput")
        self.passInput.setGeometry(QRect(290, 300, 231, 31))
        self.passInput.setFont(font)
        self.passInput.setStyleSheet(lineedit_style)
        self.passInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.passInput.setClearButtonEnabled(False)
        self.passwordLabel = QLabel(self.loginPage)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(340, 268, 131, 31))
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet(u"border-radius: 8px;\n"
        "border: 0px solid #000000;\n"
        "background: transparent;\n"
        "background-color: rgba(177, 180, 180, 0.7);\n"
        "color: rgb(0, 0, 0);")
        self.userInput = QLineEdit(self.loginPage)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setGeometry(QRect(290, 230, 231, 31))
        self.userInput.setFont(font)
        self.userInput.setStyleSheet(lineedit_style)
        self.userInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quitButton = QPushButton(self.loginPage)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setGeometry(QRect(350, 390, 111, 31))
        self.quitButton.setFont(font)
        self.quitButton.setStyleSheet(buttonstyle)
        self.quitButton.setAutoDefault(True)
        self.bottomTitle = QLabel(self.loginPage)
        self.bottomTitle.setObjectName(u"bottomTitle")
        self.bottomTitle.setGeometry(QRect(0, 480, 801, 71))
        self.bottomTitle.setFont(font1)
        self.bottomTitle.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
        "color: black;\n"
        "background: none;")
        self.stackedWidget.addWidget(self.loginPage)
        ################################################################
        # TABLE PAGE
        self.workPage = QWidget()
        self.workPage.setObjectName(u"workPage")
        self.tableWidget = QTableWidget(self.workPage)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-5, 1, 811, 501))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("""
                QTableWidget {
                    background: transparent;   
                    background-color: rgba(255, 255, 255, 0.7);
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
                """)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(["Ticket Name", "Ticket ID", "Urgency", 
                                                    "Location", "Status", "Details", "", "Report"])
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(114)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setFixedWidth(6)
        self.tableWidget.setShowGrid(False)
        header = self.tableWidget.horizontalHeader()
        header.setFont(font)
        self.createButton = QPushButton(self.workPage)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(200, 520, 161, 31))
        self.createButton.setFont(font)
        self.createButton.setStyleSheet(buttonstyle)
        self.createButton.setCheckable(True)
        self.createButton.setChecked(False)
        self.createButton.setAutoDefault(False)
        self.createButton.setFlat(False)
        self.refreshButton = QPushButton(self.workPage)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(435, 520, 121, 31))
        self.refreshButton.setFont(font)
        self.refreshButton.setStyleSheet(buttonstyle)
        self.refreshButton.setCheckable(True)
        self.refreshButton.setChecked(False)
        self.refreshButton.setAutoDefault(False)
        self.refreshButton.setFlat(False)
        self.logoutButton = QPushButton(self.workPage)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setGeometry(QRect(10, 520, 121, 31))
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet(buttonstyle)
        self.logoutButton.setCheckable(True)
        self.logoutButton.setChecked(False)
        self.logoutButton.setAutoDefault(False)
        self.logoutButton.setFlat(False)
        self.deleteButton = QPushButton(self.workPage)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(630, 520, 161, 31))
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet(buttonstyle)
        self.deleteButton.setCheckable(True)
        self.deleteButton.setChecked(False)
        self.deleteButton.setAutoDefault(False)
        self.deleteButton.setFlat(False)
        self.stackedWidget.addWidget(self.workPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Safety Manager", None))
        self.appTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt;\">SAFETY MANAGER</span></p></body></html>", None))
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.usernameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Username</span></p></body></html>", None))
        self.passInput.setText("")
        self.passwordLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Password</span></p></body></html>", None))
        self.userInput.setInputMask("")
        self.userInput.setText("")
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.bottomTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">University of Liverpool - LSDC - ATLAS ITk</span></p><p align=\"center\"><span style=\" font-size:14pt;\">v1.1.0</span></p></body></html>", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"Create Ticket", None))
        self.logoutButton.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Ticket", None))
    # retranslateUi