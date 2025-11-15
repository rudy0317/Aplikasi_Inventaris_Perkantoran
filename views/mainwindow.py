# views/mainwindow.py

import os

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from models.barang_model import BarangModel
from views.barang_form import BarangForm
from views.barang_masuk_form import BarangMasukForm
from views.barang_keluar_form import BarangKeluarForm
from views.instansi_form import InstansiForm


class MainWindow(QMainWindow):
    def __init__(self, current_user, parent=None):
        super().__init__(parent)

        # Path absolut ke mainwindow.ui
        ui_path = os.path.join(os.path.dirname(__file__), "..", "ui", "mainwindow.ui")
        abs_path = os.path.abspath(ui_path)

        if not os.path.exists(abs_path):
            QMessageBox.critical(self, "Error", f"File UI mainwindow tidak ditemukan:\n{abs_path}")
            return

        loader = QUiLoader()
        ui_file = QFile(abs_path)
        ui_file.open(QFile.ReadOnly)
        form = loader.load(ui_file, self)
        ui_file.close()

        # Tempel UI ke dalam QMainWindow (hindari blank / nested QMainWindow)
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.addWidget(form)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(container)
        self.setWindowTitle("Aplikasi Gudang - Main Window")

        self.ui = form
        self.barang_model = BarangModel()  # kalau nanti mau dipakai di dashboard, udah ready
        self.current_user = current_user

        # Hubungkan tombol Data Barang
        try:
            self.ui.btnBarang.clicked.connect(self.buka_barang_form)
        except AttributeError:
            QMessageBox.critical(self, "Error", "ObjectName tombol di mainwindow.ui harus 'btnBarang'")

        # Hubungkan tombol Barang Masuk
        try:
            self.ui.btnBarangMasuk.clicked.connect(self.buka_barang_masuk_form)
        except AttributeError:
            QMessageBox.critical(self, "Error", "ObjectName tombol di mainwindow.ui harus 'btnBarangMasuk'")

        # Hubungkan tombol Barang Keluar
        try:
            self.ui.btnBarangKeluar.clicked.connect(self.buka_barang_keluar_form)
        except AttributeError:
            QMessageBox.critical(self, "Error", "ObjectName tombol di mainwindow.ui harus 'btnBarangKeluar'")

        # Hubungkan tombol Instansi
        try:
            self.ui.btnInstansi.clicked.connect(self.buka_instansi_form)
        except AttributeError:
            QMessageBox.critical(self, "Error", "ObjectName tombol di mainwindow.ui harus 'btnInstansi'")

        # Hubungkan tombol Keluar
        try:
            self.ui.btnKeluar.clicked.connect(self.close)
        except AttributeError:
            QMessageBox.critical(self, "Error", "ObjectName tombol di mainwindow.ui harus 'btnKeluar'")

    def buka_barang_form(self):
        # Buka jendela form CRUD barang
        self.formBarang = BarangForm(self.current_user)
        self.formBarang.show()

    def buka_barang_masuk_form(self):
        # Buka jendela form CRUD barang masuk
        self.formBarangMasuk = BarangMasukForm(self.current_user)
        self.formBarangMasuk.show()

    def buka_barang_keluar_form(self):
        # Buka jendela form CRUD barang keluar
        self.formBarangKeluar = BarangKeluarForm(self.current_user)
        self.formBarangKeluar.show()

    def buka_instansi_form(self):
        # Buka jendela form CRUD instansi
        self.formInstansi = InstansiForm(self.current_user)
        self.formInstansi.show()
