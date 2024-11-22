# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warningluJMQS.ui'
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
from PyQt6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QVBoxLayout, QWidget)


class Ui_Warning(object):
    def __init__(self, Warning):
        if not Warning.objectName():
            Warning.setObjectName(u"Form")
        Warning.resize(334, 214)
        Warning.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(Warning)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(Warning)
        self.frame.setObjectName(u"frame")
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
        font = QFont()
        font.setFamilies([u"Montserrat SemiBold"])
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet(u"letter-spacing: 2px;")

        self.verticalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(31, 31, 31);\n"
                                   "border-radius:10px;\n"
                                   "margin-left:15px;\n"
                                   "margin-right:15px;\n"
                                   "margin-bottom:5px;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.warning_label = QLabel(self.frame_2)
        self.warning_label.setObjectName(u"warning_label")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(10)
        self.warning_label.setFont(font1)
        self.warning_label.setAlignment(
            Qt.AlignmentFlag.AlignLeading | Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.warning_label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.warning_label)

        self.verticalLayout.addWidget(self.frame_2)

        self.button = QPushButton(self.frame)
        self.button.setObjectName(u"button")
        font2 = QFont()
        font2.setFamilies([u"Montserrat SemiBold"])
        font2.setPointSize(12)
        self.button.setFont(font2)
        self.button.setStyleSheet(u"""
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

        self.verticalLayout.addWidget(self.button)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Warning)

        QMetaObject.connectSlotsByName(Warning)
        # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"WARNING:", None))
        self.warning_label.setText(QCoreApplication.translate("Form",
                                                              u"Cannot edit patient without selecting patient first, please select patient from search panel.",
                                                              None))
        self.button.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi
