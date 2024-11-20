import sys

from PyQt6 import QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

from clinic.controller import Controller
from clinic.exception.invalid_login_exception import InvalidLoginException
from clinic.gui.login import Ui_Login
from clinic.gui.main_window import Ui_MainScreen

controller = Controller()
app = QApplication(sys.argv)


class LoginGUI(QMainWindow):
    def __init__(self, application: QApplication):
        super().__init__()

        # Create a central widget and set it for the main window
        self.main_window = None
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_Login(self.central_widget, controller)

        self.app = application

        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.username_field.text()
        password = self.ui.password_field.text()
        try:
            # Try to log in using the provided credentials
            controller.login(username, password)
            print("LOGGED IN SUCCESSFULLY")
            self.switch_to_main_window()
        except InvalidLoginException:
            self.ui.login_message.setVisible(True)
            print("LOG IN FAILED")

    def switch_to_main_window(self):
        # Create the Main Window only after login succeeds
        self.main_window = MainGUI(controller, self)
        self.main_window.setWindowTitle("Clinic - Manager")
        self.main_window.show()  # Show the main window
        self.hide()  # Hide the login window


class MainGUI(QMainWindow):
    def __init__(self, con: Controller, login_window: 'LoginGUI'):
        super().__init__()
        # Create a central widget and set it for the main window
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the central widget
        self.ui = Ui_MainScreen(self.central_widget, con)
        self.setMinimumSize(800, 600)

        self.login_window = login_window

        self.ui.logout_btn.clicked.connect(self.logout)

    def logout(self):
        # When logging out, destroy the main window and return to the login window
        controller.isLogged = False
        self.login_window.ui.username_field.clear()
        self.login_window.ui.password_field.clear()
        self.close()  # Close the MainGUI
        self.login_window.show()  # Show the LoginGUI again


def main():
    font = QFont("Montserrat", 10)
    app.setFont(font)

    QtGui.QFontDatabase.addApplicationFont("./clinic/gui/content/fonts/Montserrat-VariableFont_wght.ttf")
    QtGui.QFontDatabase.addApplicationFont("./clinic/gui/content/fonts/Montserrat-Italic-VariableFont_wght.ttf")

    login_window = LoginGUI(app)
    login_window.setWindowTitle("Clinic - Login")
    login_window.show()

    sys.exit(app.exec())
