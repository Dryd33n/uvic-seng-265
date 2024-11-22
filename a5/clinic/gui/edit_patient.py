# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_patientuANjhh.ui'
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
                             QWidget, QHBoxLayout, QGridLayout)


class Ui_EditPatient(object):

    def __init__(self, CreatePatient):
        if not CreatePatient.objectName():
            CreatePatient.setObjectName(u"CreatePatient")
        CreatePatient.resize(710, 548)
        CreatePatient.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(CreatePatient)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(CreatePatient)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(15, 15, 15);\n"
                                 "border-radius:10px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 212, 255);\n"
                                 "letter-spacing:1px;")
        self.label.setIndent(25)

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
                                   "border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(14)
        self.label_2.setFont(font1)
        self.label_2.setIndent(10)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(22, 22, 22);\n"
                                   "margin-left:15px;\n"
                                   "margin-right:15px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.old_name_label = QLabel(self.frame_3)
        self.old_name_label.setObjectName(u"old_name_label")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        self.old_name_label.setFont(font2)

        self.gridLayout.addWidget(self.old_name_label, 4, 1, 1, 1)

        self.phone_field = QLineEdit(self.frame_3)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setFont(font2)
        self.phone_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                       "border:1px solid rgb(59, 59, 59);\n"
                                       "padding: 6px;\n"
                                       "border-radius: 8px;")

        self.gridLayout.addWidget(self.phone_field, 10, 2, 1, 1)

        self.old_address_label = QLabel(self.frame_3)
        self.old_address_label.setObjectName(u"old_address_label")
        self.old_address_label.setFont(font2)

        self.gridLayout.addWidget(self.old_address_label, 12, 1, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dob_field_message = QLabel(self.frame_3)
        self.dob_field_message.setObjectName(u"dob_field_message")
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        font3.setItalic(True)
        self.dob_field_message.setFont(font3)
        self.dob_field_message.setStyleSheet(u"color:rgb(170, 0, 0);")

        self.verticalLayout_4.addWidget(self.dob_field_message)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.gridLayout.addLayout(self.verticalLayout_4, 7, 2, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.phone_field_msg = QLabel(self.frame_3)
        self.phone_field_msg.setObjectName(u"phone_field_msg")
        font4 = QFont()
        font4.setFamilies([u"Montserrat Medium"])
        font4.setItalic(True)
        self.phone_field_msg.setFont(font4)
        self.phone_field_msg.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.verticalLayout_5.addWidget(self.phone_field_msg)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.gridLayout.addLayout(self.verticalLayout_5, 11, 2, 1, 1)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setFont(font2)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout.addWidget(self.label_11, 12, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 9, 2, 1, 1)

        self.old_dob_label = QLabel(self.frame_3)
        self.old_dob_label.setObjectName(u"old_dob_label")
        self.old_dob_label.setFont(font2)

        self.gridLayout.addWidget(self.old_dob_label, 6, 1, 1, 1)

        self.old_email_label = QLabel(self.frame_3)
        self.old_email_label.setObjectName(u"old_email_label")
        self.old_email_label.setFont(font2)

        self.gridLayout.addWidget(self.old_email_label, 8, 1, 1, 1)

        self.email_field = QLineEdit(self.frame_3)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setFont(font2)
        self.email_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                       "border:1px solid rgb(59, 59, 59);\n"
                                       "padding: 6px;\n"
                                       "border-radius: 8px;")

        self.gridLayout.addWidget(self.email_field, 8, 2, 1, 1)

        self.dob_field = QLineEdit(self.frame_3)
        self.dob_field.setObjectName(u"dob_field")
        self.dob_field.setFont(font2)
        self.dob_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                     "border:1px solid rgb(59, 59, 59);\n"
                                     "padding: 6px;\n"
                                     "border-radius: 8px;")

        self.gridLayout.addWidget(self.dob_field, 6, 2, 1, 1)

        self.old_phn_label = QLabel(self.frame_3)
        self.old_phn_label.setObjectName(u"old_phn_label")
        self.old_phn_label.setFont(font2)

        self.gridLayout.addWidget(self.old_phn_label, 2, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 2, 1, 1)

        self.old_phone_label = QLabel(self.frame_3)
        self.old_phone_label.setObjectName(u"old_phone_label")
        self.old_phone_label.setFont(font2)

        self.gridLayout.addWidget(self.old_phone_label, 10, 1, 1, 1)

        self.name_field = QLineEdit(self.frame_3)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setFont(font2)
        self.name_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                      "border:1px solid rgb(59, 59, 59);\n"
                                      "padding: 6px;\n"
                                      "border-radius: 8px;")

        self.gridLayout.addWidget(self.name_field, 4, 2, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 40))
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.phn_field_message = QLabel(self.frame_3)
        self.phn_field_message.setObjectName(u"phn_field_message")
        self.phn_field_message.setFont(font3)
        self.phn_field_message.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.verticalLayout_3.addWidget(self.phn_field_message)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout.addLayout(self.verticalLayout_3, 3, 2, 1, 1)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout.addWidget(self.label_9, 0, 1, 1, 1)

        self.phn_field = QLineEdit(self.frame_3)
        self.phn_field.setObjectName(u"phn_field")
        self.phn_field.setFont(font2)
        self.phn_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                     "border:1px solid rgb(59, 59, 59);\n"
                                     "padding: 6px;\n"
                                     "border-radius: 8px;")

        self.gridLayout.addWidget(self.phn_field, 2, 2, 1, 1)

        self.address_field = QLineEdit(self.frame_3)
        self.address_field.setObjectName(u"address_field")
        self.address_field.setFont(font2)
        self.address_field.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
                                         "border:1px solid rgb(59, 59, 59);\n"
                                         "padding: 6px;\n"
                                         "border-radius: 8px;")

        self.gridLayout.addWidget(self.address_field, 12, 2, 1, 1)

        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        font5 = QFont()
        font5.setFamilies([u"Montserrat Medium"])
        font5.setPointSize(8)
        font5.setItalic(True)
        self.label_17.setFont(font5)

        self.gridLayout.addWidget(self.label_17, 1, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 1)

        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout.addWidget(self.frame_2)

        self.create_patient_msg = QLabel(self.frame)
        self.create_patient_msg.setObjectName(u"create_patient_msg")
        self.create_patient_msg.setFont(font4)
        self.create_patient_msg.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.create_patient_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.create_patient_msg)

        self.edit_patient_button = QPushButton(self.frame)
        self.edit_patient_button.setObjectName(u"edit_patient_button")
        font6 = QFont()
        font6.setFamilies([u"Montserrat Medium"])
        font6.setPointSize(11)
        font6.setBold(False)
        self.edit_patient_button.setFont(font6)
        self.edit_patient_button.setStyleSheet(u"""
    QPushButton {
        background-color: rgb(77, 77, 77);
        border: 1px solid rgba(255, 255, 255, 0);
        letter-spacing: 2px;
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

        self.verticalLayout.addWidget(self.edit_patient_button)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.phn_field, self.name_field)
        QWidget.setTabOrder(self.name_field, self.dob_field)
        QWidget.setTabOrder(self.dob_field, self.email_field)
        QWidget.setTabOrder(self.email_field, self.phone_field)
        QWidget.setTabOrder(self.phone_field, self.address_field)
        QWidget.setTabOrder(self.address_field, self.edit_patient_button)

        self.retranslateUi(CreatePatient)

        QMetaObject.connectSlotsByName(CreatePatient)
        # setupUi

    def retranslateUi(self, CreatePatient):
        CreatePatient.setWindowTitle(QCoreApplication.translate("CreatePatient", u"Form", None))
        self.label.setText(QCoreApplication.translate("CreatePatient", u"EDIT PATIENT:", None))
        self.label_2.setText(QCoreApplication.translate("CreatePatient", u"PATIENT DETAILS:", None))
        self.old_name_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.phone_field.setPlaceholderText(QCoreApplication.translate("CreatePatient", u"Patient Phone Number", None))
        self.old_address_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("CreatePatient", u"PHN:", None))
        self.dob_field_message.setText("")
        self.phone_field_msg.setText("")
        self.label_7.setText(QCoreApplication.translate("CreatePatient", u"NAME:", None))
        self.label_11.setText(QCoreApplication.translate("CreatePatient", u"HOME ADDRESS:", None))
        self.label_3.setText(QCoreApplication.translate("CreatePatient", u"DATE OF BIRTH:", None))
        self.label_8.setText(QCoreApplication.translate("CreatePatient", u"EMAIL ADDRESS:", None))
        self.label_10.setText(QCoreApplication.translate("CreatePatient", u"PHONE NUMBER:", None))
        self.old_dob_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.old_email_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.email_field.setPlaceholderText(QCoreApplication.translate("CreatePatient", u"Patient Email Address", None))
        self.dob_field.setPlaceholderText(
            QCoreApplication.translate("CreatePatient", u"Patient Date Of Birth YYYY-MM-DD", None))
        self.old_phn_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.old_phone_label.setText(QCoreApplication.translate("CreatePatient", u"TextLabel", None))
        self.name_field.setPlaceholderText(QCoreApplication.translate("CreatePatient", u"Patient Full Name", None))
        self.label_5.setText(QCoreApplication.translate("CreatePatient", u"UPDATED INFORMATION:", None))
        self.phn_field_message.setText("")
        self.label_9.setText(QCoreApplication.translate("CreatePatient", u"PATIENT INFORMATION:", None))
        self.phn_field.setPlaceholderText(QCoreApplication.translate("CreatePatient", u"Personal Health Number", None))
        self.address_field.setText("")
        self.address_field.setPlaceholderText(
            QCoreApplication.translate("CreatePatient", u"Patient Home Address", None))
        self.label_17.setText(
            QCoreApplication.translate("CreatePatient", u"Fields Left Empty will Remain Unchanged", None))
        self.create_patient_msg.setText("")
        self.edit_patient_button.setText(QCoreApplication.translate("CreatePatient", u"EDIT PATIENT", None))
    # retranslateUi

