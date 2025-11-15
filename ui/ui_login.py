# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(380, 220)
        self.verticalLayout = QVBoxLayout(LoginWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(LoginWindow)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setStyleSheet(u"font-size:18px; font-weight:bold;")

        self.verticalLayout.addWidget(self.labelTitle)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.labelUsername = QLabel(LoginWindow)
        self.labelUsername.setObjectName(u"labelUsername")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.labelUsername)

        self.input_username = QLineEdit(LoginWindow)
        self.input_username.setObjectName(u"input_username")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.input_username)

        self.labelPassword = QLabel(LoginWindow)
        self.labelPassword.setObjectName(u"labelPassword")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.labelPassword)

        self.input_password = QLineEdit(LoginWindow)
        self.input_password.setObjectName(u"input_password")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.input_password)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.btnLogin = QPushButton(LoginWindow)
        self.btnLogin.setObjectName(u"btnLogin")

        self.buttonLayout.addWidget(self.btnLogin)

        self.btnCancel = QPushButton(LoginWindow)
        self.btnCancel.setObjectName(u"btnCancel")

        self.buttonLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login Sistem", None))
        self.labelTitle.setText(QCoreApplication.translate("LoginWindow", u"Silakan Login", None))
        self.labelUsername.setText(QCoreApplication.translate("LoginWindow", u"Username:", None))
        self.labelPassword.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.btnCancel.setText(QCoreApplication.translate("LoginWindow", u"Batal", None))
    # retranslateUi

