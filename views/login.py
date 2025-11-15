# views/login.py

from PySide6.QtWidgets import QDialog, QMessageBox
from ui.ui_login import Ui_LoginWindow
from models.user_model import UserModel


class LoginWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.user_model = UserModel()
        self.logged_in_user = None   # ⬅️ penting

        self.ui.btnLogin.clicked.connect(self.handle_login)
        self.ui.btnCancel.clicked.connect(self.reject)
        self.ui.input_username.setFocus()

    def handle_login(self):
        username = self.ui.input_username.text().strip()
        password = self.ui.input_password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Peringatan", "Username dan password harus diisi!")
            return

        # pastikan check_login() return dict: {"id_user": .., "user": .., "nama": ..}
        user = self.user_model.check_login(username, password)

        if user:
            QMessageBox.information(self, "Sukses", f"Selamat datang, {user['nama']}!")
            self.logged_in_user = user        # ⬅️ SIMPAN DI SINI
            self.accept()
        else:
            QMessageBox.critical(self, "Gagal", "Username atau password salah.")
