# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_notePmJkio.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PyQt6.QtGui import (QFont)
from PyQt6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
                             QPlainTextEdit, QPushButton, QVBoxLayout)


class Ui_create_note(object):
    def __init__(self, create_note):
        if not create_note.objectName():
            create_note.setObjectName(u"create_note")
        create_note.resize(400, 300)
        create_note.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(create_note)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(create_note)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(15, 15, 15);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(18)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"letter-spacing: 2px;")

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
                                   "border-radius:10px;\n"
                                   "margin-left: 15px;\n"
                                   "margin-right: 15px;\n"
                                   "margin-bottom:5px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 15, 0, 15)
        self.note_content_field = QPlainTextEdit(self.frame_2)
        self.note_content_field.setObjectName(u"note_content_field")
        self.note_content_field.setFont(font)
        self.note_content_field.setStyleSheet(u"border: 1px solid rgb(82, 82, 82);\n"
                                              "padding:10px;")

        self.horizontalLayout_3.addWidget(self.note_content_field)

        self.verticalLayout.addWidget(self.frame_2)

        self.create_note_msg = QLabel(self.frame)
        self.create_note_msg.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Montserrat Medium"])
        font2.setItalic(True)
        self.create_note_msg.setFont(font2)
        self.create_note_msg.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.create_note_msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.create_note_msg)

        self.create_note_btn = QPushButton(self.frame)
        self.create_note_btn.setObjectName(u"create_note_btn")
        self.create_note_btn.setFont(font)
        self.create_note_btn.setStyleSheet(u"""
    QPushButton {
        background-color: rgb(77, 77, 77);
        border: 1px solid rgba(255, 255, 255, 0);
        letter-spacing: 1px;
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

        self.verticalLayout.addWidget(self.create_note_btn)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(create_note)

        QMetaObject.connectSlotsByName(create_note)

    # setupUi

    def retranslateUi(self, create_note):
        create_note.setWindowTitle(QCoreApplication.translate("create_note", u"Form", None))
        self.label.setText(QCoreApplication.translate("create_note", u"CREATE NOTE:", None))
        self.note_content_field.setPlaceholderText(
            QCoreApplication.translate("create_note", u"enter note content here", None))
        self.create_note_msg.setText("")
        self.create_note_btn.setText(QCoreApplication.translate("create_note", u"CREATE", None))
    # retranslateUi
