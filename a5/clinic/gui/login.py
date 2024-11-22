# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginyBaDtO.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
                               QWidget)




class Ui_Login(object):
    def __init__(self, Login):
        self.main_window = None
        self.main_ui = None

        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(424, 243)
        font = QFont()
        font.setFamilies([u"Montserrat"])
        Login.setFont(font)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(Login)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(11)
        self.login_frame.setFont(font1)
        self.login_frame.setFrameShape(QFrame.Shape.Panel)
        self.login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.login_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.loginLayout = QVBoxLayout()
        self.loginLayout.setSpacing(0)
        self.loginLayout.setObjectName(u"loginLayout")
        self.loginLayout.setContentsMargins(2, 2, 2, 2)
        self.label_3 = QLabel(self.login_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"letter-spacing: 2px;\n"
                                   "color: rgb(85, 255, 255);")
        self.label_3.setTextFormat(Qt.TextFormat.PlainText)
        self.label_3.setMargin(5)
        self.label_3.setIndent(30)

        self.loginLayout.addWidget(self.label_3)

        self.login_fields_frame = QFrame(self.login_frame)
        self.login_fields_frame.setObjectName(u"login_fields_frame")
        self.login_fields_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
                                              "background-color: rgb(24, 24, 24);\n"
                                              "border-radius: 10px;")
        self.login_fields_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_fields_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.login_fields_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.loginForm = QVBoxLayout()
        self.loginForm.setSpacing(0)
        self.loginForm.setObjectName(u"loginForm")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.loginForm.addItem(self.verticalSpacer)

        self.username_box = QVBoxLayout()
        self.username_box.setObjectName(u"username_box")
        self.label = QLabel(self.login_fields_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Montserrat Medium"])
        font3.setItalic(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"padding: 0px;\n"
                                 "margin: 0px;\n"
                                 "letter-spacing: 1px;")
        self.label.setMargin(0)
        self.label.setIndent(25)

        self.username_box.addWidget(self.label)

        self.username_field = QLineEdit(self.login_fields_frame)
        self.username_field.setObjectName(u"lineEdit")
        self.username_field.setMinimumSize(QSize(350, 0))
        self.username_field.setFont(font)
        self.username_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                    "border: 1px solid #333;\n"
                                    "margin-left: 15px;\n"
                                    "margin-right: 40px;\n"
                                    "border-radius: 4px;\n"
                                    "padding: 10px;\n"
                                    "")

        self.username_box.addWidget(self.username_field)

        self.username_box.setStretch(0, 1)
        self.username_box.setStretch(1, 1)

        self.loginForm.addLayout(self.username_box)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.loginForm.addItem(self.verticalSpacer_2)

        self.password_box = QVBoxLayout()
        self.password_box.setObjectName(u"password_box")
        self.label_2 = QLabel(self.login_fields_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"padding: 0px;\n"
                                   "margin: 0px;\n"
                                   "letter-spacing: 1px;")
        self.label_2.setIndent(25)

        self.password_box.addWidget(self.label_2)

        self.password_field = QLineEdit(self.login_fields_frame)
        self.password_field.setObjectName(u"lineEdit_2")
        self.password_field.setMinimumSize(QSize(350, 0))
        self.password_field.setFont(font)
        self.password_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                      "border: 1px solid #333;\n"
                                      "margin-left: 15px;\n"
                                      "margin-right: 40px;\n"
                                      "border-radius: 4px;\n"
                                      "padding: 10px;\n"
                                      "")
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.password_box.addWidget(self.password_field)

        self.password_box.setStretch(0, 1)
        self.password_box.setStretch(1, 1)

        self.loginForm.addLayout(self.password_box)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.loginForm.addItem(self.verticalSpacer_3)

        self.login_button_box = QVBoxLayout()
        self.login_button_box.setObjectName(u"login_button_box")
        self.login_message = QLabel(self.login_fields_frame)
        self.login_message.setObjectName(u"label_4")
        font4 = QFont()
        font4.setItalic(True)
        self.login_message.setFont(font4)
        self.login_message.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.login_message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.login_button_box.addWidget(self.login_message)

        self.pushButton = QPushButton(self.login_fields_frame)

        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"""
    QPushButton {
        margin: 0px 120px 10px 120px;
        background-color: rgb(77, 77, 77);
        border: 1px solid rgba(255, 255, 255, 0);
        letter-spacing: 3px;
        border-radius: 11px;
        padding: 3px;
    }
    QPushButton:hover {
        background-color: rgb(100, 100, 100); /* Lighter background on hover */
        border: 1px solid rgba(255, 255, 255, 0.5); /* Visible border on hover */
    }
    QPushButton:pressed {
        background-color: rgb(66, 66, 66); /* Darker background when pressed */
    }
    """)

        self.login_button_box.addWidget(self.pushButton)

        self.login_button_box.setStretch(0, 1)
        self.login_button_box.setStretch(1, 1)

        self.loginForm.addLayout(self.login_button_box)

        self.loginForm.setStretch(0, 1)
        self.loginForm.setStretch(1, 2)
        self.loginForm.setStretch(2, 1)
        self.loginForm.setStretch(3, 2)
        self.loginForm.setStretch(4, 1)
        self.loginForm.setStretch(5, 2)

        self.verticalLayout_5.addLayout(self.loginForm)

        self.loginLayout.addWidget(self.login_fields_frame)

        self.loginLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.loginLayout)

        self.verticalLayout_2.addWidget(self.login_frame)

        self.login_message.setVisible(False)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)

    # setupUi


    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"LOGIN:", None))
        self.label.setText(QCoreApplication.translate("Login", u"USERNAME:", None))
        self.username_field.setText("")
        self.username_field.setPlaceholderText(QCoreApplication.translate("Login", u"username", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"PASSWORD:", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("Login", u"password", None))
        self.login_message.setText(QCoreApplication.translate("Login", u"login failed, incorrect username or password!", None))
        self.pushButton.setText(QCoreApplication.translate("Login", u"LOGIN", None))
    # retranslateUi
