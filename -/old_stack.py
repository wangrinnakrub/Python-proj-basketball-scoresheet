from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

from sign_in import Signin_page

from sign_up import Signup_page
from create_account import Create_accountl

from forgot_password import Forgot_password_page
from reset_password import Reset_password
from main_window import MainWindow


class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.sign_in = Signin_page()

        self.sign_up = Signup_page()
        self.create_account = Create_account()

        self.forgot_password = Forgot_password_page()
        self.reset_password = Reset_password()

        self.main_window = MainWindow()

        # * ----------------------------------------- * #
        # add to stack
        self.addWidget(self.sign_in)
        self.addWidget(self.sign_up)
        self.addWidget(self.create_account)
        self.addWidget(self.forgot_password)
        self.addWidget(self.reset_password)
        self.addWidget(self.main_window)

        # * ----------------------------------------- * #
        # current widget
        self.setCurrentWidget(self.sign_in)
        self.setGeometry(360, 110, 700, 650)

        # self.sign_in.switch_to_forgot_password.connect(self.show_forgot_password)qwdqwd
        # self.sign_in.switch_to_main_window.connect(self.show_main_window)
        # self.sign_in.switch_to_sign_up.connect(self.show_sign_up)

        # self.sign_up.switch_to_sign_in.connect(self.show_sign_in)
        # self.sign_up.switch_to_create_account.connect(self.show_create_account)

        self.sign_in.switch_to_forgot_password.connect(lambda: self.switch_with_animation(self.forgot_password))
        self.sign_in.switch_to_main_window.connect(lambda: self.switch_with_animation(self.main_window))
        self.sign_in.switch_to_sign_up.connect(lambda: self.switch_with_animation(self.sign_up))
        self.sign_up.switch_to_sign_in.connect(lambda: self.switch_with_animation(self.sign_in))
        self.sign_up.switch_to_create_account.connect(lambda: self.switch_with_animation(self.create_account))

    def switch_with_animation(self, new_widget):
        # Set the initial position of the new widget (slide in from the right)
        new_widget.setGeometry(self.width(), 0, self.width(), self.height())

        # Add the new widget to the current stack
        self.setCurrentWidget(new_widget)

        # Create an animation for sliding in the widget
        animation = QPropertyAnimation(new_widget, b"pos")
        animation.setDuration(500)  # Animation duration in milliseconds
        animation.setStartValue(QPoint(self.width(), 0))  # Start from outside the right edge
        animation.setEndValue(QPoint(0, 0))  # End at the normal position
        animation.start()

    def show_sign_in(self):
        self.setCurrentWidget(self.sign_in)
        self.setGeometry(360, 110, 700, 650)

    def show_forgot_password(self):
        self.setCurrentWidget(self.forgot_password)
        self.setGeometry(360, 110, 700, 650)

    def show_sign_up(self):
        self.setCurrentWidget(self.sign_up)
        self.setGeometry(360, 110, 700, 650)

    def show_create_account(self):
        self.setCurrentWidget(self.create_account)
        self.setGeometry(360, 110, 700, 650)

    def show_reset_password(self):
        self.setCurrentWidget(self.reset_password)
        self.setGeometry(360, 110, 700, 650)

    def show_main_window(self):
        self.setCurrentWidget(self.main_window)
        self.setGeometry(360, 110, 700, 650)


app = QApplication(sys.argv)
main_app = MainApp()
main_app.show()
sys.exit(app.exec())
