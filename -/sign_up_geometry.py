import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Signup_page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sign Up')
        self.setGeometry(340, 110, 700, 650)  # x, y, w, h
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setWindowOpacity(1.0)
        self.import_style('124.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username = ''
        self.password = ''
        self.password_focus = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_up_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.username_input_box, self.password_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)


    def clear_focus_from_all(self):
        self.username_input_box.clearFocus()
        self.password_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)


    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def ui(self):
        # Main widget setup
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # *----------- SIGN_UP label ----------- #
        self.sign_up_label = QLabel('Sign Up', self)
        self.sign_up_label.setObjectName('sign_up_label')
        self.sign_up_label.setGeometry(730, 60, 100, 100)  # x, y, width, height

        # *----------- Username label and input box ----------- #
        self.username_label = QLabel('Username', self)
        self.username_label.setObjectName('username_label')
        self.username_label.setGeometry(620, 190, 100, 30)


        self.username_input_box = QLineEdit(self)
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText('Type your username')
        self.username_input_box.setGeometry(620, 240, 305, 40)
        self.username_input_box.returnPressed.connect(self.check_sign_up)

        # *----------- Username error label ----------- #
        self.username_error_label = QLabel('', self)
        self.username_error_label.setObjectName('username_error_label')
        self.username_error_label.setGeometry(620, 265, 305, 10)

        # *----------- Password label and input box ----------- #
        self.password_label = QLabel('Password', self)
        self.password_label.setObjectName('password_label')
        self.password_label.setGeometry(600, 350, 100, 30)

        self.password_input_box = QLineEdit(self)
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.setGeometry(620, 400, 305, 40)
        self.password_input_box.textChanged.connect(self.handle_text_change)
        self.password_input_box.returnPressed.connect(self.password_enter)

        # *----------- Password error label ----------- #
        self.password_error_label = QLabel('', self)
        self.password_error_label.setObjectName('password_error_label')
        self.password_error_label.setGeometry(620, 375, 305, 20)

        # *----------- Sign_up button ----------- #
        self.sign_up_button = QPushButton('Sign In', self)
        self.sign_up_button.setStyleSheet(
            'background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #43d9ff, stop:1 #ff56c7);')
        self.sign_up_button.setObjectName('sign_up_button')
        self.sign_up_button.setGeometry(240, 410, 230, 37)
        self.sign_up_button.clicked.connect(self.sign_up_clicked)

        # *----------- Forgot password link ----------- #
        self.forgot_password_label = QLabel(
            """<a href='#' style='
               width:200px;
               padding-left: 55px;
               text-decoration: none;
               outline: none !important;
               color: #767676;
               font-size: 12px;'>forgot password</a>""",
            self)
        self.forgot_password_label.setObjectName('forgot_password_label')
        self.forgot_password_label.setGeometry(240, 600, 230, 50)
        self.forgot_password_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.forgot_password_label.linkActivated.connect(self.open_forgot_password_page)

        # *----------- Sign up link ----------- #
        self.signup_label = QLabel(
            """<a href='#' style='
               text-decoration: none;
               outline: none !important;
               color: #767676;
               font-size: 12px;'>Sign Up</a>""",
            self)
        self.signup_label.setObjectName('signup_label')
        self.signup_label.setGeometry(240, 650, 230, 50)
        self.signup_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.signup_label.linkActivated.connect(self.open_signup_page)

    # * Rest of the code remains the same * #

    def handle_text_change(self, text):
        if self.timer.isActive():
            self.timer.stop()

        if len(text) > len(self.previous_text):
            self.password += text[-1]
            masked_password = '●' * (len(self.password) - 1) + self.password[-1]
        elif len(text) < len(self.previous_text):
            self.password = self.password[:len(text)]
            masked_password = '●' * len(self.password)

        self.previous_text = text
        self.password_input_box.blockSignals(True)
        self.password_input_box.setText(masked_password)
        self.password_input_box.blockSignals(False)
        self.password_input_box.setCursorPosition(len(masked_password))

        self.timer.start(700)

    def mask_last_character(self):
        self.timer.stop()
        masked_password = '●' * len(self.password)
        self.password_input_box.blockSignals(True)
        self.password_input_box.setText(masked_password)
        self.password_input_box.blockSignals(False)
        self.password_input_box.setCursorPosition(len(masked_password))


    # *---------- check password enter ---------- #
    def password_enter(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_sign_up()

    def sign_up_clicked(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_sign_up()


    # *---------- check sign_up ---------- #
    def check_sign_up(self):
        self.username = self.username_input_box.text()
        # password = self.password_input_box.text()
        valid = True

        if self.username == '':
            self.username_error_label.setText('Please enter your username')
            self.password_error_label.setText('')
            valid = False
        elif self.password == '':
            self.password_input_box.setFocus()
            if self.password_focus >= 1:
                self.password_error_label.setText('Please enter your password')
                self.password_focus = 0
            valid = False
        if not self.username == '':
            self.username_error_label.setText('')
            # valid = True
        if not self.password == '':
            self.password_error_label.setText('')
            # valid = True

        if len(self.password) > 0 and self.username == '':
            self.username_input_box.setFocus()
            self.username_error_label.setText('Please enter your username')
            self.password_error_label.setText('')
            valid = False


        if valid == True:
            if self.username == 'admin' and self.password == '1234':
                self.open_main_window()
            else:
                self.password_error_label.setText('Invalid username or password')


    # *---------- open main window if sign_up succesful ---------- #
    def open_main_window(self):
        from main_window import MainWindow
        self.main_window = MainWindow()
        self.main_window.showMaximized()
        self.close()


    # *---------- open_forgot_password_page ---------- #
    def open_forgot_password_page(self):
        from forgot_password import Forgot_password_page
        self.forgot_password_page = Forgot_password_page()
        self.forgot_password_page.showMaximized()
        self.close()


    # *---------- open sign up ---------- #
    def open_signup_page(self):
        from sign_up import Signup_page
        self.signup_page = Signup_page()
        self.signup_page.showMaximized()
        self.close()


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    sign_up = Signup_page()
    # sign_up.show()
    sign_up.showMaximized()
    app.exec()
