# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setStyleSheet(u"font-size: 20px; font-weight: bold; margin: 10px;")
        self.labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.spacerTop = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerTop)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacerLeft)

        self.btnBarang = QPushButton(self.centralwidget)
        self.btnBarang.setObjectName(u"btnBarang")
        self.btnBarang.setMinimumSize(QSize(150, 40))

        self.buttonLayout.addWidget(self.btnBarang)

        self.btnBarangMasuk = QPushButton(self.centralwidget)
        self.btnBarangMasuk.setObjectName(u"btnBarangMasuk")
        self.btnBarangMasuk.setMinimumSize(QSize(150, 40))

        self.buttonLayout.addWidget(self.btnBarangMasuk)

        self.btnBarangKeluar = QPushButton(self.centralwidget)
        self.btnBarangKeluar.setObjectName(u"btnBarangKeluar")
        self.btnBarangKeluar.setMinimumSize(QSize(150, 40))

        self.buttonLayout.addWidget(self.btnBarangKeluar)

        self.btnInstansi = QPushButton(self.centralwidget)
        self.btnInstansi.setObjectName(u"btnInstansi")
        self.btnInstansi.setMinimumSize(QSize(150, 40))

        self.buttonLayout.addWidget(self.btnInstansi)

        self.btnKeluar = QPushButton(self.centralwidget)
        self.btnKeluar.setObjectName(u"btnKeluar")
        self.btnKeluar.setMinimumSize(QSize(150, 40))

        self.buttonLayout.addWidget(self.btnKeluar)

        self.horizontalSpacerRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacerRight)


        self.verticalLayout.addLayout(self.buttonLayout)

        self.spacerBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.spacerBottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 816, 27))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aplikasi Gudang - Main Window", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Dashboard Aplikasi Peralatan Kantor", None))
        self.btnBarang.setText(QCoreApplication.translate("MainWindow", u"Data Barang", None))
        self.btnBarangMasuk.setText(QCoreApplication.translate("MainWindow", u"Barang Masuk", None))
        self.btnBarangKeluar.setText(QCoreApplication.translate("MainWindow", u"Barang Keluar", None))
        self.btnInstansi.setText(QCoreApplication.translate("MainWindow", u"Data Instansi", None))
        self.btnKeluar.setText(QCoreApplication.translate("MainWindow", u"Keluar", None))
    # retranslateUi

