
# todo ter yu nai jai nan gwa yu kang gun eab fun tueng ter yu 💫

# * ---------------------------------------- sign_in ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from test4 import *

class Signin_page(QMainWindow):
    switch_to_sign_up = pyqtSignal()
    switch_to_forgot_password = pyqtSignal()
    switch_to_main_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Sign In')
        self.setGeometry(360, 110, 700, 650)
        self.import_style('style_sign_in.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username = ''
        self.password = ''
        self.username_focus = 0
        self.password_focus = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_in_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

    # *---------- clear focus ---------- #
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


    # *---------- import style from qss ---------- #
    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")


    # *---------- layout ---------- #
    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)


    # *---------- sign_in page widget ---------- #
    def addWidgetsToLayout(self, ui):

        ui.addStretch()
        # # *----------- SIGN_IN ----------- #
        # sign_in label
        self.sign_in_label = QLabel('Sign In')
        self.sign_in_label.setObjectName('sign_in_label')
        self.sign_in_label.setFixedHeight(100)

        # sign_in layout
        sign_in_layout = QHBoxLayout()
        sign_in_layout.addStretch()
        sign_in_layout.addWidget(self.sign_in_label)
        sign_in_layout.addStretch()
        ui.addLayout(sign_in_layout)

        ui.addStretch()

        # *----------- Username ----------- #
        # username label
        self.username_label = QLabel('Username')
        self.username_label.setObjectName('username_label')
        self.username_label.setFixedSize(350,90)

        # username label layout
        username_layout = QHBoxLayout()
        username_layout.addStretch()
        username_layout.addWidget(self.username_label)
        username_layout.addStretch()
        ui.addLayout(username_layout)

        # username input box
        self.username_input_box = QLineEdit()
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText(' Type your username')
        self.username_input_box.returnPressed.connect(self.username_enter)
        self.username_input_box.setFixedSize(305, 40)

        # username input box layout
        username_input_box_layout = QHBoxLayout()
        username_input_box_layout.setObjectName('username_input_box_layout')
        username_input_box_layout.addStretch()
        username_input_box_layout.addWidget(self.username_input_box)
        username_input_box_layout.addStretch()
        ui.addLayout(username_input_box_layout)

        # todo username error label
        self.username_error_label = QLabel('')
        self.username_error_label.setObjectName('username_error_label')
        self.username_error_label.setFixedHeight(25)

        # todo username error label layout
        username_error_label_layout = QHBoxLayout()
        username_error_label_layout.setObjectName('username_error_label_layout')
        username_error_label_layout.addStretch()
        username_error_label_layout.addWidget(self.username_error_label)
        username_error_label_layout.addStretch()
        ui.addLayout(username_error_label_layout)

        # *----------- Password ----------- #
        # password label
        self.password_label = QLabel('Password')
        self.password_label.setObjectName('password_label')
        self.password_label.setFixedSize(350,30)

        # password label layout
        password_label_layout = QHBoxLayout()
        password_label_layout.addStretch()
        password_label_layout.addWidget(self.password_label)
        password_label_layout.addStretch()
        ui.addLayout(password_label_layout)

        # password input box
        self.password_input_box = QLineEdit()
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText(' Type your password')
        self.password_input_box.textChanged.connect(self.handle_text_change)
        self.password_input_box.returnPressed.connect(self.password_enter)
        self.password_input_box.setFixedSize(305,50)
        self.previous_text = ''

        # password input box layout
        password_input_box_layout = QHBoxLayout()
        password_input_box_layout.setObjectName('password_input_box_layout')
        password_input_box_layout.addStretch()
        password_input_box_layout.addWidget(self.password_input_box)
        password_input_box_layout.addStretch()
        ui.addLayout(password_input_box_layout)

        # todo Password error label
        self.password_error_label = QLabel('')
        self.password_error_label.setObjectName('password_error_label')
        self.password_error_label.setFixedHeight(25)
        # self.password_error_label.setStyleSheet('color: red')

        # todo password error label layout
        password_error_label_layout = QHBoxLayout()
        password_error_label_layout.setObjectName('password_error_label_layout')
        password_error_label_layout.addStretch()
        password_error_label_layout.addWidget(self.password_error_label)
        password_error_label_layout.addStretch()
        ui.addLayout(password_error_label_layout)


        # *---------- forgot password ----------#
        # forgot password label
        self.forgot_password_label = QLabel("""<a href='#' style='

                                   width:200px;
                                   text-decoration: none;
                                   outline: none !important;
                                   color:#767676;
                                   font-size: 12px;

                                   '>forgot password</a>""")
        # self.forgot_password_label = QLabel('<a href="#">forgot password</a>')
        self.forgot_password_label.setObjectName('forgot_password_label')
        # self.forgot_password_label.setFixedSize(200,80)
        # self.forgot_password_label.setMinimumHeight(30)
        self.forgot_password_label.setFixedHeight(20)
        self.forgot_password_label.setContentsMargins(210,0,0,0)
        self.forgot_password_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.forgot_password_label.linkActivated.connect(self.switch_to_forgot_password.emit)

        # forgot password label layout
        forgot_password_label_layout = QHBoxLayout()
        forgot_password_label_layout.addStretch()
        forgot_password_label_layout.addWidget(self.forgot_password_label)
        forgot_password_label_layout.addStretch()
        ui.addLayout(forgot_password_label_layout)

        ui.addStretch()
        ui.addSpacing(30)

        # *---------- Sign_in button ----------- #
        # sign_in button
        # self.sign_in_button = QPushButton('Sign In',self)
        self.sign_in_button = AnimatedBackgroundButton('Sign in',self)
        # self.sign_in_button.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #43d9ff, stop:1 #ff56c7);')
        # self.sign_in_button.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #846cf3, stop:1 #82dae5);')
        self.sign_in_button.setObjectName('sign_in_button')
        self.sign_in_button.setFixedSize(230,37)
        self.sign_in_button.clicked.connect(self.check_sign_in)

        # sign_in button layout
        sign_in_button_layout = QHBoxLayout()
        sign_in_button_layout.setObjectName('sign_in_button_layout')
        # sign_in_button_layout.setContentsMargins(0,0,0,20)
        sign_in_button_layout.addStretch()
        sign_in_button_layout.addWidget(self.sign_in_button)
        sign_in_button_layout.addStretch()
        ui.addLayout(sign_in_button_layout)

        # *---------- sign up ----------#
        # sign up label
        # self.signup_label = QLabel('SIGN UP')
        self.signup_label = QLabel("""<a href='#' style='

                                   text-decoration: none;
                                   outline: none !important;
                                   color: #767676;
                                   font-size: 12px;

                                   '>Sign Up</a>""")
        # self.signup_label = QLabel('<a href="#">Sign Up</a>')
        self.signup_label.setObjectName('signup_label')
        # self.signup_label.setFixedSize(80,80)
        # self.signup_label.setMinimumHeight(50)
        self.signup_label.setFixedHeight(70)
        # self.signup_label.setMargin(21)
        self.signup_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        self.signup_label.linkActivated.connect(self.switch_to_sign_up.emit)

        # sign up label layout
        signup_label_layout = QHBoxLayout()
        signup_label_layout.addStretch()
        signup_label_layout.addWidget(self.signup_label)
        signup_label_layout.addStretch()
        ui.addLayout(signup_label_layout)

        ui.addStretch()

    # *---------- password to ● ---------- #
    # show current password but if not type longer than 500 millisec it will change to dot
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


    # *---------- check username enter ---------- #
    def username_enter(self):
        self.username_focus += 1
        if self.username_focus >= 1:
            self.check_sign_in()

        self.username = self.username_input_box.text()
        if self.username != '':
            self.password_input_box.setFocus()

    # *---------- check password enter ---------- #
    def password_enter(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_sign_in()

    def sign_in_clicked(self):
        self.username = self.username_input_box.text()

        if self.username == '':
            self.username_enter()
        elif self.password == '':
            self.password_enter()
        else:
            self.check_sign_in()


    # *---------- check sign in ---------- #
    def check_sign_in(self):
        self.username = self.username_input_box.text()
        valid = True

        if self.username == '':
            self.username_error_label.setText('Please enter your username')
            self.password_error_label.setText('')

        elif self.password == '':
            self.username_error_label.setText('')
            if self.password_focus >= 1:
                self.password_error_label.setText('Please enter your password')

        if self.username != '':
            self.username_error_label.setText('')
        if self.password != '':
            self.password_error_label.setText('')

        if self.username != '' and self.password != '':
            if self.username == 'admin' and self.password == '1234':
                self.switch_to_main_window.emit()
            else:
                self.password_error_label.setText('Invalid username or password')


    # # *---------- open main window if sign_in succesful ---------- #
    # def open_main_window(self):
    #     from main_window import MainWindow
    #     self.main_window = MainWindow()
    #     self.main_window.show()
    #     self.close()


    # # *---------- open forgot password page ---------- #
    # def open_forgot_password_page(self):
    #     from forgot_password import Forgot_password_page
    #     self.forgot_password_page = Forgot_password_page()
    #     self.forgot_password_page.show()
    #     self.close()


    # # *---------- open sign up ---------- #
    # def open_signup_page(self):
    #     from sign_up import Signup_page
    #     self.sign_up = Signup_page()
    #     # self.signup_page.showMaximized()
    #     self.sign_up.show()
    #     self.close()


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    sign_in = Signin_page()
    # sign_in.show()
    sign_in.showMaximized()
    app.exec()
