# main.py
import sys
from PySide6.QtWidgets import QApplication
from views.login import LoginWindow
from views.mainwindow import MainWindow   # sesuaikan path lu

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginWindow()
    if login.exec() == LoginWindow.Accepted:
        current_user = login.logged_in_user    # ⬅️ AMBIL USER DARI LOGIN

        window = MainWindow(current_user)      # ⬅️ KIRIM KE MAINWINDOW
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit(0)
