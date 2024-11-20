# -*- coding: utf-8 -*-
import re
from datetime import datetime
from typing import List, Optional

################################################################################
## Form generated from reading UI file 'main_windowRuSRPZ.ui'
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
                             QWidget, QHBoxLayout, QListWidgetItem, QListWidget, QGridLayout)

from clinic.controller import Controller
from clinic.patient import Patient


class Ui_MainScreen(object):
    def __init__(self, MainScreen, controller: Controller):
        self.controller = controller

        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.resize(1059, 921)
        MainScreen.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout_19 = QHBoxLayout(MainScreen)
        self.horizontalLayout_19.setSpacing(4)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(MainScreen)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setMaximumSize(QSize(16777215, 70))
        self.frame.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(43, 88, 118, 152), stop:1 rgba(78, 67, 118, 113));\n"
            "border-radius: 10px;\n"
            "")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setSizeIncrement(QSize(1, 1))
        self.label_2.setBaseSize(QSize(70, 70))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setPixmap(QPixmap(u"./clinic/gui/content/graphics/clinic_icon.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Montserrat SemiBold"])
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"letter-spacing: 4px;\n"
                                 "color: rgb(0, 212, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout_14.addWidget(self.frame)

        self.frame_2 = QFrame(MainScreen)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
                                   "border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, -1, 5, 5)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(14)
        font1.setBold(False)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(0, 212, 255);\n"
                                   "letter-spacing:1px;\n"
                                   "margin-top: 10px;")
        self.label_3.setMargin(0)
        self.label_3.setIndent(25)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.patient_search_field = QLineEdit(self.frame_3)
        self.patient_search_field.setObjectName(u"patient_search_field")
        self.patient_search_field.setMinimumSize(QSize(0, 32))
        self.patient_search_field.setMaximumSize(QSize(16777215, 32))
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        self.patient_search_field.setFont(font2)
        self.patient_search_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                                "border:1px solid rgb(59, 59, 59);\n"
                                                "padding: 6px;\n"
                                                "border-radius: 8px;")

        self.verticalLayout_2.addWidget(self.patient_search_field)

        self.patient_search_message = QLabel(self.frame_3)
        self.patient_search_message.setObjectName(u"patient_search_message")
        self.patient_search_message.setMinimumSize(QSize(0, 12))
        self.patient_search_message.setMaximumSize(QSize(16777215, 12))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setItalic(True)
        self.patient_search_message.setFont(font3)
        self.patient_search_message.setIndent(15)

        self.verticalLayout_2.addWidget(self.patient_search_message)

        self.patient_list = QListWidget(self.frame_3)
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))
        __qlistwidgetitem = QListWidgetItem(self.patient_list)
        __qlistwidgetitem.setFont(font2);
        __qlistwidgetitem.setIcon(icon);
        brush = QBrush(QColor(0, 0, 0, 255))

        __qlistwidgetitem1 = QListWidgetItem(self.patient_list)
        __qlistwidgetitem1.setFont(font2);
        __qlistwidgetitem1.setBackground(brush);
        __qlistwidgetitem1.setIcon(icon);

        self.patient_list.setObjectName(u"patient_list")

        self.verticalLayout_2.addWidget(self.patient_list)

        self.verticalLayout_2.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout.addWidget(self.frame_3)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Montserrat Light"])
        font4.setPointSize(12)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"margin-top: 10px;")
        self.label_5.setIndent(20)

        self.verticalLayout.addWidget(self.label_5)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.create_patient_btn = QPushButton(self.frame_4)
        self.create_patient_btn.setObjectName(u"create_patient_btn")
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        font5.setBold(True)
        self.create_patient_btn.setFont(font5)
        self.create_patient_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                              "padding:10px;\n"
                                              "border-radius: 15px;")

        self.horizontalLayout_7.addWidget(self.create_patient_btn)

        self.delete_patient_btn = QPushButton(self.frame_4)
        self.delete_patient_btn.setObjectName(u"delete_patient_btn")
        self.delete_patient_btn.setFont(font5)
        self.delete_patient_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                              "padding:10px;\n"
                                              "border-radius: 15px;")

        self.horizontalLayout_7.addWidget(self.delete_patient_btn)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.logout_btn = QPushButton(self.frame_4)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setFont(font5)
        self.logout_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                      "padding:10px;\n"
                                      "border-radius: 15px;")

        self.verticalLayout_3.addWidget(self.logout_btn)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout.addWidget(self.frame_4)

        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_14.addWidget(self.frame_2)

        self.horizontalLayout.addLayout(self.verticalLayout_14)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_5 = QFrame(MainScreen)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 70))
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
                                   "border: 0px solid rgba(255, 255, 255, 0);\n"
                                   "border-radius: 10px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.patient_details_title = QLabel(self.frame_5)
        self.patient_details_title.setObjectName(u"patient_details_title")
        font6 = QFont()
        font6.setFamilies([u"Montserrat Light"])
        font6.setPointSize(18)
        self.patient_details_title.setFont(font6)
        self.patient_details_title.setStyleSheet(u"color: rgb(0, 212, 255);")
        self.patient_details_title.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_8.addWidget(self.patient_details_title)

        self.verticalLayout_13.addWidget(self.frame_5)

        self.frame_6 = QFrame(MainScreen)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
                                   "border: 0px solid rgba(255, 255, 255, 0);\n"
                                   "border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(0, 212, 255);")
        self.label_7.setIndent(20)

        self.verticalLayout_4.addWidget(self.label_7)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 100))
        self.frame_7.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 15))
        font7 = QFont()
        font7.setFamilies([u"Montserrat Medium"])
        font7.setPointSize(10)
        self.label_8.setFont(font7)
        self.label_8.setStyleSheet(u"letter-spacing:1px;")

        self.verticalLayout_6.addWidget(self.label_8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.patient_first_name = QLabel(self.frame_7)
        self.patient_first_name.setObjectName(u"patient_first_name")
        self.patient_first_name.setFont(font5)
        self.patient_first_name.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.patient_first_name, 0, 1, 1, 1)

        self.patient_phn = QLabel(self.frame_7)
        self.patient_phn.setObjectName(u"patient_last_name")
        self.patient_phn.setFont(font5)
        self.patient_phn.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.patient_phn, 1, 1, 1, 1)

        self.patient_dob = QLabel(self.frame_7)
        self.patient_dob.setObjectName(u"patient_dob")
        self.patient_dob.setFont(font5)

        self.gridLayout.addWidget(self.patient_dob, 2, 1, 1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout)

        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_10.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(0, 15))
        self.label_15.setMaximumSize(QSize(16777215, 15))
        font8 = QFont()
        font8.setFamilies([u"Montserrat Medium"])
        font8.setBold(False)
        font8.setItalic(False)
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"letter-spacing:1px;")

        self.verticalLayout_7.addWidget(self.label_15)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.patient_home_address = QLabel(self.frame_7)
        self.patient_home_address.setObjectName(u"patient_home_address")
        self.patient_home_address.setFont(font5)

        self.gridLayout_2.addWidget(self.patient_home_address, 2, 1, 1, 1)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font5)

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_18 = QLabel(self.frame_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)

        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)

        self.patient_phone_number = QLabel(self.frame_7)
        self.patient_phone_number.setObjectName(u"patient_phone_number")
        self.patient_phone_number.setFont(font5)

        self.gridLayout_2.addWidget(self.patient_phone_number, 0, 1, 1, 1)

        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font5)

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)

        self.patient_email_address = QLabel(self.frame_7)
        self.patient_email_address.setObjectName(u"patient_email_address")
        self.patient_email_address.setFont(font5)

        self.gridLayout_2.addWidget(self.patient_email_address, 1, 1, 1, 1)

        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.verticalLayout_7.setStretch(1, 1)

        self.horizontalLayout_10.addLayout(self.verticalLayout_7)

        self.horizontalLayout_10.setStretch(0, 3)
        self.horizontalLayout_10.setStretch(1, 4)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)

        self.verticalLayout_4.addWidget(self.frame_7)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font4)
        self.label_22.setIndent(10)

        self.verticalLayout_4.addWidget(self.label_22)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.create_patient_record_note_btn = QPushButton(self.frame_8)
        self.create_patient_record_note_btn.setObjectName(u"create_patient_record_note_btn")
        font9 = QFont()
        font9.setBold(True)
        self.create_patient_record_note_btn.setFont(font9)
        self.create_patient_record_note_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                                          "padding: 10px;\n"
                                                          "border-radius: 15px;")

        self.horizontalLayout_12.addWidget(self.create_patient_record_note_btn)

        self.edit_patient_btn = QPushButton(self.frame_8)
        self.edit_patient_btn.setObjectName(u"edit_patient_btn")
        self.edit_patient_btn.setFont(font9)
        self.edit_patient_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                            "padding: 10px;\n"
                                            "border-radius: 15px;")

        self.horizontalLayout_12.addWidget(self.edit_patient_btn)

        self.delete_patient_btn_2 = QPushButton(self.frame_8)
        self.delete_patient_btn_2.setObjectName(u"delete_patient_btn_2")
        self.delete_patient_btn_2.setFont(font5)
        self.delete_patient_btn_2.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                                "padding: 10px;\n"
                                                "border-radius: 15px;")

        self.horizontalLayout_12.addWidget(self.delete_patient_btn_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)

        self.verticalLayout_4.addWidget(self.frame_8)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_9 = QFrame(MainScreen)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(24, 24, 24);\n"
                                   "border: 0px solid rgba(255, 255, 255, 0);\n"
                                   "border-radius: 10px;")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 20))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"color: rgb(0, 212, 255);")
        self.label_23.setIndent(20)

        self.verticalLayout_8.addWidget(self.label_23)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 20))
        font10 = QFont()
        font10.setFamilies([u"Montserrat Medium"])
        font10.setPointSize(10)
        font10.setBold(False)
        self.label_24.setFont(font10)
        self.label_24.setStyleSheet(u"letter-spacing:1px;")
        self.label_24.setIndent(15)

        self.verticalLayout_9.addWidget(self.label_24)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_25 = QLabel(self.frame_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 20))
        self.label_25.setFont(font2)
        self.label_25.setIndent(10)

        self.verticalLayout_10.addWidget(self.label_25)

        self.record_search_field = QLineEdit(self.frame_10)
        self.record_search_field.setObjectName(u"record_search_field")
        self.record_search_field.setMinimumSize(QSize(220, 0))
        self.record_search_field.setFont(font2)
        self.record_search_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                               "border:1px solid rgb(59, 59, 59);\n"
                                               "padding: 6px;\n"
                                               "border-radius: 8px;")

        self.verticalLayout_10.addWidget(self.record_search_field)

        self.record_search_message = QLabel(self.frame_10)
        self.record_search_message.setObjectName(u"record_search_message")
        self.record_search_message.setMaximumSize(QSize(16777215, 10))
        self.record_search_message.setFont(font3)
        self.record_search_message.setIndent(20)

        self.verticalLayout_10.addWidget(self.record_search_message)

        self.record_list = QListWidget(self.frame_10)
        icon1 = QIcon(QIcon.fromTheme(u"format-justify-left"))
        __qlistwidgetitem2 = QListWidgetItem(self.record_list)
        __qlistwidgetitem2.setFont(font2);
        __qlistwidgetitem2.setIcon(icon1);
        __qlistwidgetitem3 = QListWidgetItem(self.record_list)
        __qlistwidgetitem3.setFont(font2);
        __qlistwidgetitem3.setIcon(icon1);
        self.record_list.setObjectName(u"record_list")

        self.verticalLayout_10.addWidget(self.record_list)

        self.horizontalLayout_15.addLayout(self.verticalLayout_10)

        self.verticalLayout_9.addWidget(self.frame_10)

        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        font11 = QFont()
        font11.setFamilies([u"Montserrat Light"])
        font11.setPointSize(10)
        font11.setBold(True)
        self.label_26.setFont(font11)
        self.label_26.setIndent(15)

        self.verticalLayout_9.addWidget(self.label_26)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.edit_note_btn = QPushButton(self.frame_11)
        self.edit_note_btn.setObjectName(u"edit_note_btn")
        self.edit_note_btn.setFont(font5)
        self.edit_note_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                         "padding: 10px;\n"
                                         "border-radius: 15px;")

        self.horizontalLayout_17.addWidget(self.edit_note_btn)

        self.delete_note_btn = QPushButton(self.frame_11)
        self.delete_note_btn.setObjectName(u"delete_note_btn")
        self.delete_note_btn.setFont(font5)
        self.delete_note_btn.setStyleSheet(u"background-color: rgb(62, 62, 62);\n"
                                           "padding: 10px;\n"
                                           "border-radius: 15px;")

        self.horizontalLayout_17.addWidget(self.delete_note_btn)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)

        self.verticalLayout_9.addWidget(self.frame_11)

        self.horizontalLayout_14.addLayout(self.verticalLayout_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_27 = QLabel(self.frame_9)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(16777215, 20))
        self.label_27.setFont(font10)
        self.label_27.setIndent(15)

        self.verticalLayout_11.addWidget(self.label_27)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(15, 15, 15);\n"
                                    "margin-top: 5px;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.label_28 = QLabel(self.frame_12)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(16777215, 20))
        self.label_28.setFont(font5)
        self.label_28.setIndent(10)

        self.verticalLayout_12.addWidget(self.label_28)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"background-color: rgb(32, 32, 32);\n"
                                    "margin-top: 5px;\n"
                                    "margin-bottom: 5px;")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.note_content = QLabel(self.frame_13)
        self.note_content.setObjectName(u"note_content")
        self.note_content.setFont(font5)
        self.note_content.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.note_content.setWordWrap(True)

        self.horizontalLayout_20.addWidget(self.note_content)

        self.verticalLayout_12.addWidget(self.frame_13)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 15))
        self.label_29.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_29)

        self.note_date = QLabel(self.frame_12)
        self.note_date.setObjectName(u"note_date")
        self.note_date.setMaximumSize(QSize(16777215, 15))
        font12 = QFont()
        font12.setFamilies([u"Montserrat"])
        font12.setPointSize(8)
        font12.setBold(True)
        self.note_date.setFont(font12)

        self.verticalLayout_12.addWidget(self.note_date)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer)

        self.label_31 = QLabel(self.frame_12)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 15))
        self.label_31.setFont(font5)

        self.verticalLayout_12.addWidget(self.label_31)

        self.note_number = QLabel(self.frame_12)
        self.note_number.setObjectName(u"note_number")
        self.note_number.setMaximumSize(QSize(16777215, 15))
        font13 = QFont()
        font13.setFamilies([u"Montserrat"])
        font13.setBold(True)
        font13.setItalic(False)
        self.note_number.setFont(font13)

        self.verticalLayout_12.addWidget(self.note_number)

        self.verticalLayout_12.setStretch(1, 7)
        self.verticalLayout_12.setStretch(4, 1)

        self.horizontalLayout_18.addLayout(self.verticalLayout_12)

        self.verticalLayout_11.addWidget(self.frame_12)

        self.horizontalLayout_14.addLayout(self.verticalLayout_11)

        self.horizontalLayout_14.setStretch(1, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.verticalLayout_13.addWidget(self.frame_9)

        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_13.setStretch(2, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_13)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)

        self.horizontalLayout_19.addLayout(self.horizontalLayout)

        self.retranslate_ui(MainScreen)
        self.init_ui_components()

        self.patient_search_field.textChanged.connect(self.handle_patient_search)
        self.patient_list.itemClicked.connect(self.switch_current_patient)

        QMetaObject.connectSlotsByName(MainScreen)

    def retranslate_ui(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainScreen", u"CLINIC", None))
        self.label_3.setText(QCoreApplication.translate("MainScreen", u"SEARCH:", None))
        self.patient_search_field.setPlaceholderText(
            QCoreApplication.translate("MainScreen", u"Search Patient by Name or by PHN", None))
        self.patient_search_message.setText(QCoreApplication.translate("MainScreen", u"10 Results Matching Name", None))

        __sortingEnabled = self.patient_list.isSortingEnabled()
        self.patient_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.patient_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainScreen", u"Jane Doe", None));
        ___qlistwidgetitem1 = self.patient_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainScreen", u"Jhonny Appleseed", None));
        self.patient_list.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainScreen", u"OPTIONS:", None))
        self.create_patient_btn.setText(QCoreApplication.translate("MainScreen", u"CREATE PATIENT", None))
        self.delete_patient_btn.setText(QCoreApplication.translate("MainScreen", u"DELETE PATIENT", None))
        self.logout_btn.setText(QCoreApplication.translate("MainScreen", u"LOGOUT", None))
        self.patient_details_title.setText(QCoreApplication.translate("MainScreen", u"CURRENT PATIENT: JANE DOE", None))
        self.label_7.setText(QCoreApplication.translate("MainScreen", u"PATIENT DETAILS:", None))
        self.label_8.setText(QCoreApplication.translate("MainScreen", u"PERSONAL INFORMATION:", None))
        self.label_9.setText(QCoreApplication.translate("MainScreen", u"PHN:", None))
        self.label_10.setText(QCoreApplication.translate("MainScreen", u"NAME:", None))
        self.label_11.setText(QCoreApplication.translate("MainScreen", u"DATE OF BIRTH:", None))
        self.patient_first_name.setText(QCoreApplication.translate("MainScreen", u"JANE", None))
        self.patient_phn.setText(QCoreApplication.translate("MainScreen", u"123456789", None))
        self.patient_dob.setText(QCoreApplication.translate("MainScreen", u"JAN 1, 2000", None))
        self.label_15.setText(QCoreApplication.translate("MainScreen", u"CONTACT INFORMATION:", None))
        self.patient_home_address.setText(QCoreApplication.translate("MainScreen", u"1 Maple Lake Dr.", None))
        self.label_17.setText(QCoreApplication.translate("MainScreen", u"HOME ADDRESS:", None))
        self.label_18.setText(QCoreApplication.translate("MainScreen", u"PHONE NUMBER:", None))
        self.patient_phone_number.setText(QCoreApplication.translate("MainScreen", u"012-345-3789", None))
        self.label_20.setText(QCoreApplication.translate("MainScreen", u"EMAIL ADDRESS:", None))
        self.patient_email_address.setText(QCoreApplication.translate("MainScreen", u"janedoe@gmail.com", None))
        self.label_22.setText(QCoreApplication.translate("MainScreen", u"OPTIONS:", None))
        self.create_patient_record_note_btn.setText(
            QCoreApplication.translate("MainScreen", u"CREATE RECORD NOTE", None))
        self.edit_patient_btn.setText(QCoreApplication.translate("MainScreen", u"EDIT PATIENT", None))
        self.delete_patient_btn_2.setText(QCoreApplication.translate("MainScreen", u"DELETE PATIENT", None))
        self.label_23.setText(QCoreApplication.translate("MainScreen", u"PATIENT RECORD:", None))
        self.label_24.setText(QCoreApplication.translate("MainScreen", u"RECORDS:", None))
        self.label_25.setText(QCoreApplication.translate("MainScreen", u"SEARCH:", None))
        self.record_search_field.setText("")
        self.record_search_field.setPlaceholderText(
            QCoreApplication.translate("MainScreen", u"Search by Note Content or by Number", None))
        self.record_search_message.setText(
            QCoreApplication.translate("MainScreen", u"10 Results Matching Content", None))

        __sortingEnabled1 = self.record_list.isSortingEnabled()
        self.record_list.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.record_list.item(0)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainScreen", u"1: Patient Arrives with....", None));
        ___qlistwidgetitem3 = self.record_list.item(1)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainScreen", u"2: Patient Arrives with...", None));
        self.record_list.setSortingEnabled(__sortingEnabled1)

        self.label_26.setText(QCoreApplication.translate("MainScreen", u"OPTIONS:", None))
        self.edit_note_btn.setText(QCoreApplication.translate("MainScreen", u"EDIT NOTE", None))
        self.delete_note_btn.setText(QCoreApplication.translate("MainScreen", u"DELETE NOTE", None))
        self.label_27.setText(QCoreApplication.translate("MainScreen", u"CURRENT NOTE:", None))
        self.label_28.setText(QCoreApplication.translate("MainScreen", u"NOTE CONTENTS:", None))
        self.note_content.setText(QCoreApplication.translate("MainScreen",
                                                             u"Patient arrives with extreme pain in left nut complaining about testicular tortion.",
                                                             None))
        self.label_29.setText(QCoreApplication.translate("MainScreen", u"NOTE DATE:", None))
        self.note_date.setText(QCoreApplication.translate("MainScreen", u"January 1st, 2020", None))
        self.label_31.setText(QCoreApplication.translate("MainScreen", u"NOTE NUMBER:", None))
        self.note_number.setText(QCoreApplication.translate("MainScreen", u"Note Number 1", None))

    def init_ui_components(self):
        self.handle_patient_search()
        self.fill_patient_details(None)

    def handle_patient_search(self):
        search_term = self.patient_search_field.text()
        search_term.strip()

        # SEARCH TERM EMPTY - SHOW ALL PATIENTS
        if len(search_term) == 0:
            self.fill_patient_list(self.controller.list_patients())
            self.patient_search_message.setText("showing all patients")
        # SEARCH TERM CONTAINS DIGIT - SEARCH BY PHN
        elif re.search(r'\d', search_term):
            patient = self.controller.search_patient(int(search_term))

            if patient:
                self.patient_search_message.setText("patient with matching PHN found")
                self.fill_patient_list([patient])
            else:
                self.patient_search_message.setText("no patient with mentioned PHN")
                self.fill_patient_list([])
        # SEARCH TERM CONTAINS STRING - SEARCH BY NAME
        else:
            patients = self.controller.retrieve_patients(search_term)
            self.patient_search_message.setText(f"{len(patients)} matching patients found")
            self.fill_patient_list(patients)

    def fill_patient_list(self, patients: List[Patient]):
        # STYLING OPTIONS
        font = QFont()
        font.setFamilies([u"Montserrat"])
        icon = QIcon(QIcon.fromTheme(u"address-book-new"))

        self.patient_list.clear()

        for patient in patients:
            item = QListWidgetItem(self.patient_list)
            item.setFont(font)
            item.setIcon(icon)

            item.setText(patient.name)
            item.setData(32, patient)

    def fill_patient_details(self, patient: Optional[Patient]):
        if patient:
            # Parse the date
            date_obj = datetime.strptime(patient.birthdate, "%Y-%m-%d")
            dob = date_obj.strftime("%b %d, %Y").upper()
            dob = dob.replace(" 0", " ")

            self.patient_details_title.setText(f"CURRENT PATIENT: {patient.name.upper()}")
            self.patient_first_name.setText(patient.name)
            self.patient_phn.setText(str(patient.phn))
            self.patient_dob.setText(dob)
            self.patient_phone_number.setText(patient.phone)
            self.patient_email_address.setText(patient.email)
            self.patient_home_address.setText(patient.address)
        else:
            self.patient_details_title.setText(f"CURRENT PATIENT: NONE")
            self.patient_first_name.setText(" ")
            self.patient_phn.setText(" ")
            self.patient_dob.setText(" ")
            self.patient_phone_number.setText(" ")
            self.patient_email_address.setText(" ")
            self.patient_home_address.setText(" ")

    def switch_current_patient(self, item):
        patient = item.data(32)

        self.controller.unset_current_patient()
        self.controller.set_current_patient(patient.phn)
        self.fill_patient_details(patient)
