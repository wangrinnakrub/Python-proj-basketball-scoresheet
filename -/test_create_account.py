
# * -------------------------------------- Create Account ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3
from syntax_check import *
from pop_up import PopupWindow
from otp_check import *
from sign_up import Signup_page
class Create_account(QMainWindow):
    switch_to_sign_up = pyqtSignal()
    switch_to_sign_in = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Create Account')
        # self.setGeometry(360, 80, 700, 650) # x,y   w,h
        self.setGeometry(280, 90, 700, 650) # x,y   w,h
        self.import_style('style_create_account.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username = ''
        self.password = ''
        self.confirm_password = ''

        self.real_password = ''
        self.real_confirm_password = ''

        self.username_focus = 0
        self.password_focus = 0
        self.confirm_password_focus = 0

        self.valid_real_confirm_password = False

        self.active_input_box = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_up_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        # self.cursor.execute("SELECT * FROM user_account WHERE username = ? ", (self.username))
        # self.existing_user = self.cursor.fetchone()

        self.i = 0
        self.accept_style_changed = False
        self.valid_count = 0
        self.button_valid = False

        self.signup = Signup_page()

    def clear_input_boxs(self):
        self.username_input_box.clear()
        self.password_input_box.clear()
        self.confirm_password_input_box.clear()
        self.clear_focus_from_all()

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


    # *---------- create account page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign up -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        # self.back_button.setIcon(QIcon("C:\pic\go-back.png"))
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        # self.back_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_button.clicked.connect(self.go_back_to_sign_up)
        ui.addWidget(self.back_button)

        ui.addStretch()
        # *----------- create account ----------- #
        # create account label
        self.create_account_label = QLabel('Create Account')
        self.create_account_label.setObjectName('create_account_label')
        self.create_account_label.setFixedHeight(100)

        # create account layout
        create_account_layout = QHBoxLayout()
        create_account_layout.addStretch()
        create_account_layout.addWidget(self.create_account_label)
        create_account_layout.addStretch()
        ui.addLayout(create_account_layout)


        # *----------- Username ----------- #
        # username label
        self.username_label = QLabel('Username')
        self.username_label.setObjectName('username_label')
        self.username_label.setFixedSize(350,50)

        # username label layout
        username_layout = QHBoxLayout()
        username_layout.addStretch()
        username_layout.addWidget(self.username_label)
        username_layout.addStretch()
        ui.addLayout(username_layout)

        # username input box
        self.username_input_box = QLineEdit()
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText('Type your username')
        self.username_input_box.returnPressed.connect(self.username_enter)
        self.username_input_box.textChanged.connect(self.check_button_style_change)
        self.username_input_box.setFixedSize(305, 40)
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')

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
        self.username_error_label.setFixedHeight(20)

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
        self.password_label.setFixedSize(350,50)

        # password label layout
        password_layout = QHBoxLayout()
        password_layout.addStretch()
        password_layout.addWidget(self.password_label)
        password_layout.addStretch()
        ui.addLayout(password_layout)

        # password input box
        self.password_input_box = QLineEdit()
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.returnPressed.connect(self.password_enter)
        self.password_input_box.textChanged.connect(lambda: self.handle_text_change(self.password_input_box, self.password_input_box.text(), is_password=True))
        self.password_input_box.textChanged.connect(self.check_button_style_change)
        self.password_input_box.setFixedSize(305, 40)
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')

        # password input box layout
        password_input_box_layout = QHBoxLayout()
        password_input_box_layout.setObjectName('password_input_box_layout')
        password_input_box_layout.addStretch()
        password_input_box_layout.addWidget(self.password_input_box)
        password_input_box_layout.addStretch()
        ui.addLayout(password_input_box_layout)
        self.previous_text = ''

        # todo password error label
        self.password_error_label = QLabel('')
        self.password_error_label.setObjectName('password_error_label')
        self.password_error_label.setFixedHeight(20)

        # todo password error label layout
        password_error_label_layout = QHBoxLayout()
        password_error_label_layout.setObjectName('password_error_label_layout')
        password_error_label_layout.addStretch()
        password_error_label_layout.addWidget(self.password_error_label)
        password_error_label_layout.addStretch()
        ui.addLayout(password_error_label_layout)


        # *----------- Confirm_password ----------- #
        # confirm_password label
        self.confirm_password_label = QLabel('Confirm Password')
        self.confirm_password_label.setObjectName('confirm_password_label')
        self.confirm_password_label.setFixedSize(350,50)

        # confirm_password label layout
        confirm_password_label_layout = QHBoxLayout()
        confirm_password_label_layout.addStretch()
        confirm_password_label_layout.addWidget(self.confirm_password_label)
        confirm_password_label_layout.addStretch()
        ui.addLayout(confirm_password_label_layout)

        # confirm_password input box
        self.confirm_password_input_box = QLineEdit()
        self.confirm_password_input_box.setObjectName('confirm_password_input_box')
        self.confirm_password_input_box.setPlaceholderText('Type your confirm password')
        self.confirm_password_input_box.returnPressed.connect(self.confirm_password_enter)
        self.confirm_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.confirm_password_input_box, self.confirm_password_input_box.text(), is_password=False))
        self.confirm_password_input_box.textChanged.connect(self.check_button_style_change)
        self.confirm_password_input_box.setFixedSize(305,50)
        self.confirm_password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')
        self.previous_confirm_password = ''

        # confirm_password input box layout
        confirm_password_input_box_layout = QHBoxLayout()
        confirm_password_input_box_layout.setObjectName('confirm_password_input_box_layout')
        confirm_password_input_box_layout.addStretch()
        confirm_password_input_box_layout.addWidget(self.confirm_password_input_box)
        confirm_password_input_box_layout.addStretch()
        ui.addLayout(confirm_password_input_box_layout)

        # todo Confirm_password error label
        self.confirm_password_error_label = QLabel('')
        self.confirm_password_error_label.setObjectName('confirm_password_error_label')
        self.confirm_password_error_label.setFixedHeight(20)

        # todo confirm_password error label layout
        confirm_password_error_label_layout = QHBoxLayout()
        confirm_password_error_label_layout.setObjectName('confirm_password_error_label_layout')
        confirm_password_error_label_layout.addStretch()
        confirm_password_error_label_layout.addWidget(self.confirm_password_error_label)
        confirm_password_error_label_layout.addStretch()
        ui.addLayout(confirm_password_error_label_layout)

        ui.addSpacing(25)


        # *---------- Create account button ----------- #
        # sign_up button
        self.create_account_button = QPushButton('Create Account')
        # self.create_account_button.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #43d9ff, stop:1 #ff56c7);')
        self.create_account_button.setObjectName('create_account_button')
        self.create_account_button.setFixedSize(230,37)
        self.create_account_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.create_account_button.clicked.connect(self.create_account_clicked)

        # create_account button layout
        create_account_button_layout = QHBoxLayout()
        create_account_button_layout.setObjectName('create_account_button_layout')
        create_account_button_layout.setContentsMargins(0,10,0,65)
        create_account_button_layout.addStretch()
        create_account_button_layout.addWidget(self.create_account_button)
        create_account_button_layout.addStretch()
        ui.addLayout(create_account_button_layout)

        ui.addStretch()

    # * -------------------- handle password masking -------------------- * #
    def handle_text_change(self, input_box, text, is_password=True):
        if self.timer.isActive():
            self.timer.stop()

        self.active_input_box = input_box
        is_typing = len(text) > (len(self.previous_text) if is_password else len(self.previous_confirm_password))

        if is_password:
            if is_typing:
                self.real_password += text[-1]
            else:
                self.real_password = self.real_password[:-1]

            if is_typing:
                masked_password = '●' * (len(self.real_password) - 1) + self.real_password[-1]
                self.timer.start(700)
            else:
                masked_password = '●' * len(self.real_password)

            self.previous_text = self.real_password
            input_box.blockSignals(True)
            input_box.setText(masked_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_password))

        else:
            if is_typing:
                self.real_confirm_password += text[-1]
            else:
                self.real_confirm_password = self.real_confirm_password[:-1]

            if is_typing:
                masked_confirm_password = '●' * (len(self.real_confirm_password) - 1) + self.real_confirm_password[-1]
                self.timer.start(700)
            else:
                masked_confirm_password = '●' * len(self.real_confirm_password)

            self.previous_confirm_password = self.real_confirm_password
            input_box.blockSignals(True)
            input_box.setText(masked_confirm_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_confirm_password))


    # *---------- mask last character after timeout ---------- #

    def mask_last_character(self):
        self.timer.stop()
        if self.active_input_box is not None:
            if self.active_input_box == self.password_input_box:
                masked_password = '●' * len(self.real_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_password))

            elif self.active_input_box == self.confirm_password_input_box:
                masked_confirm_password = '●' * len(self.real_confirm_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_confirm_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_confirm_password))


    # *---------- check username enter ---------- #
    def username_enter(self):
        self.username = self.username_input_box.text()

        self.username_focus += 1
        if self.username_focus >= 1:
            self.check_create_account()

        if self.valid_count == 0 and self.existing_user and self.existing_user[1] == self.username:
            self.check_create_account()
        if is_valid_username(self.username) and len(self.username) >=5 and len(self.username) <= 30:
            self.password_input_box.setFocus()

    # *---------- check password enter ---------- #
    def password_enter(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_create_account()

        if self.username != '':
            if is_valid_password(self.real_password) and len(self.real_password) >= 8 and len(self.real_password) <= 20 :
                self.confirm_password_input_box.setFocus()

    # *---------- check confirm password enter ---------- #
    def confirm_password_enter(self):
        self.confirm_password_focus += 1
        if self.confirm_password_focus >= 1:
            self.check_create_account()

    # *---------- check create account clicked ---------- #
    def create_account_clicked(self):
        self.username = self.username_input_box.text()

        if self.username == '':
            self.username_enter()
        elif self.real_password == '':
            self.password_enter()
        elif self.real_confirm_password == '':
            self.confirm_password_enter()
        else:
            self.check_create_account()

    # *---------- check create account ---------- #
    def check_create_account(self):
        self.username = self.username_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE username = ?", (self.username,))
        self.existing_user = self.cursor.fetchone()

        self.valid = False
        self.valid_username = False
        self.valid_real_password = False
        self.valid_real_confirm_password = False

        if self.username == '':
            self.valid = False
            self.username_error_label.setText('Please enter your username')
            # self.username_input_box_red_border()
            self.username_input_box_red_border()

        elif self.real_password == '':
            self.valid = False
            if self.password_focus >= 1:
                self.password_error_label.setText('Please enter your password')
                # self.password_input_box_red_border()
                self.password_input_box_red_border()

        elif self.real_confirm_password == '':
            self.valid = False
            if self.confirm_password_focus >= 1:
                self.confirm_password_error_label.setText('Please enter your confirm password')
                # self.confirm_password_input_box_red_border()
                self.confirm_password_input_box_red_border()


        # if self.username != '' and is_valid_username(self.username) and len(self.username) >=5 and len(self.username) <= 30:
        if self.username != '':
            if len(self.username) > 30:
                self.username_error_label.setText('Username must not exceed 30 characters')
                self.username_input_box_red_border()
                self.valid = False
            elif not is_valid_username(self.username):
                self.username_error_label.setText('Username can include A-Z , a-z , 0-9 , . and _')
                self.username_input_box_red_border()
                self.valid = False
            elif len(self.username) > 0 and len(self.username) < 5:
                self.username_error_label.setText('Username must contain at least 5 characters')
                self.username_input_box_red_border()
                self.valid = False
            elif self.existing_user:
                if self.existing_user[1] == self.username:
                    self.username_error_label.setText('This username is already exits')
                    self.username_input_box_red_border()
            else:
                self.username_error_label.setText('')
                # self.username_input_box_normal_border()
                self.username_input_box_normal_border()
                self.valid_username  = True

        if self.real_password != '' and self.valid_username:
            if len(self.real_password) > 20:
                self.password_error_label.setText('Password must not exceed 20 charactors')
                self.password_input_box_red_border()
                self.valid = False
            elif len(self.real_password) > 0 and len(self.real_password) < 8:
                self.password_error_label.setText('Password must contain at least 8 characters')
                self.password_input_box_red_border()
                self.valid = False
            elif not is_valid_password(self.real_password):
                self.password_error_label.setText('Password must have 1 lowercase, 1 uppercase and 1 digit')
                self.password_input_box_red_border()
                self.valid = False
            else:
                self.password_error_label.setText('')
                # self.password_input_box_normal_border()
                self.password_input_box_normal_border()
                self.valid_real_password = True

        if self.real_confirm_password != '' and self.valid_username and self.valid_real_password:
            if self.real_confirm_password != self.real_password:
                self.confirm_password_error_label.setText('Password does not match')
                self.confirm_password_input_box_red_border()
                self.change_back_button_style()
                self.valid = False
            else:
                if is_valid_password(self.real_password) and self.button_valid_username and len(self.real_password) > 7 and len(self.real_confirm_password) > 7 and self.real_confirm_password == self.real_password:
                    self.clear_focus_from_all()
                    # self.confirm_password_input_box_normal_border()
                    self.confirm_password_input_box_normal_border()
                    self.confirm_password_error_label.setText('')
                    self.valid_real_confirm_password = True
                    self.valid = True

        if self.valid:
            self.insert()
            print('inserted')
            self.switch_to_sign_in.emit()

        # debug
        self.i+=1
        print(f'--- Test {self.i} ---')
        print('Username:', self.username)
        print('Real Password:', self.real_password)
        print('Confirm Password:', self.real_confirm_password)
        print('accpet', self.accept_style_changed)

    def change_button_style_successful(self):
        self.create_account_button.setStyleSheet('''
            QPushButton{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #f203ff, stop:1 #0099ff);
            color: white;
            }
            QPushButton:hover{
            background: #ffffff;
            color: #d83aff;
            }
        ''')

    def change_back_button_style(self):
        self.create_account_button.setStyleSheet('''
            QPushButton{
            background-color: #2a2a2a;
            color:#ffffff;
            }
            QPushButton:hover{
            background-color: #ffffff;
            color:#2a2a2a;
            }
        ''')

    def check_button_style_change(self):
        self.username = self.username_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE username = ?", (self.username,))
        self.existing_user = self.cursor.fetchone()

        self.button_valid = False
        self.button_valid_username = False
        self.button_valid_real_password = False
        self.button_valid_real_confirm_password = False

        if self.username == '':
            self.username_error_label.setText('')
            self.username_input_box_normal_border()
        if self.real_password == '':
            self.password_error_label.setText('')
            self.password_input_box_normal_border()
        if self.real_confirm_password == '':
            self.confirm_password_error_label.setText('')
            self.confirm_password_input_box_normal_border()


        if self.username != '':
                if len(self.username) > 30:
                    self.username_error_label.setText('Username must not exceed 30 characters')
                    self.username_input_box_red_border()
                    self.button_valid = False
                elif not is_valid_username(self.username):
                    self.username_error_label.setText('Username can include A-Z , a-z , 0-9 , . and _')
                    self.username_input_box_red_border()
                    self.button_valid = False
                elif self.existing_user:
                    if self.existing_user[1] == self.username:
                        self.username_error_label.setText('This username is already exits')
                        self.username_input_box_red_border()
                else:
                    if is_valid_username(self.username) and len(self.username) > 4:
                        self.username_error_label.setText('')
                        self.username_input_box_normal_border()
                        self.button_valid_username = True

        if self.real_password != '':
            if len(self.real_password) > 20:
                self.password_error_label.setText('Password must not exceed 20 charactors')
                # self.password_input_box.setStyleSheet('border-color: #ff7777')
                self.password_input_box_red_border()
                self.button_valid = False
            elif is_valid_password(self.real_password):
                self.password_error_label.setText('')
                # self.password_input_box.setStyleSheet('border-color: #dfdfdf')
                self.password_input_box_normal_border()
                self.button_valid_real_password = True
            else:
                self.password_error_label.setText('')
                # self.password_input_box.setStyleSheet('border-color: #dfdfdf')
                self.password_input_box_normal_border()

        if self.real_confirm_password != '':
            if  is_valid_password(self.real_password) and self.button_valid_username and len(self.real_password) > 7 and len(self.real_confirm_password) > 7 and self.real_confirm_password == self.real_password:
                self.confirm_password_error_label.setText('')
                # self.confirm_password_input_box.setStyleSheet('border-color: #dfdfdf')
                self.password_input_box_normal_border()
                self.button_valid = True
            else:
                # pass
                # self.confirm_password_input_box.setStyleSheet('border-color: #dfdfdf')
                self.password_input_box_normal_border()
                self.confirm_password_error_label.setText('')

        self.change_button_style_successful() if self.button_valid else self.change_back_button_style()

    def insert(self):
        print('test variable')
        print(self.fullname,self.phone_number,self.email)

        self.cursor.execute("""
            INSERT INTO user_account (username, password, fullname, phone_number, email)
            VALUES (?, ?, ?, ?, ?)
        """, (self.username,self.real_password,self.fullname,self.phone_number,self.email))

        self.connection.commit()
        print('\ninserted\n')

    def receive_data_from_sign_up_in_create_account(self,fullname,phonenumber,email):
        self.fullname = fullname
        self.phone_number = phonenumber
        self.email = email

    def go_back_to_sign_up(self):
        popup = PopupWindow()
        parent_pos = self.mapToGlobal(QPoint(0, 0))
        main_window_geometry = QRect(parent_pos, self.size())

        x = main_window_geometry.left() + (main_window_geometry.width() - popup.width()) // 2
        y = main_window_geometry.top() + (main_window_geometry.height()*9//20) - popup.height() // 2
        popup.move(x, y)

        result = popup.exec()
        print(result)
        if result:
            self.switch_to_sign_up.emit()
        else: popup.close()

    def username_input_box_red_border(self):
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #ff7777;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')

    def username_input_box_normal_border(self):
        self.username_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                                      ''')

    def password_input_box_red_border(self):
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #ff7777;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')

    def password_input_box_normal_border(self):
        self.password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                                      ''')

    def confirm_password_input_box_red_border(self):
        self.confirm_password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff7777 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #ff7777;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                              ''')

    def confirm_password_input_box_normal_border(self):
        self.confirm_password_input_box.setStyleSheet('''
QLineEdit#username_input_box,QLineEdit#name_input_box, QLineEdit#password_input_box, QLineEdit#phone_number_input_box,QLineEdit#confirm_password_input_box {

    padding-left: 25px;
    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box{

    color: #767676;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}


QLineEdit#username_input_box:hover, QLineEdit#password_input_box:hover,QLineEdit#confirm_password_input_box:hover,QLineEdit#username_input_box:focus:hover, QLineEdit#password_input_box:focus:hover,QLineEdit#confirm_password_input_box:focus:hover  {

    padding-left: 25px;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #ff56c7 !important;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}

QLineEdit#username_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#confirm_password_input_box:focus {

    border-color: #2a2a2a;

}

QLineEdit#username_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#confirm_password_input_box::placeholder {

    padding-left: 25px;
    color: #dedede;
    background-color: transparent;
    border-top: transparent;
    border-bottom: 2px solid;
    border-left: transparent;
    border-right: transparent;
    border-color: #dfdfdf;
    font-family: TeX Gyre Adventor;
    font-weight: 620;

}
                                                      ''')


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    create_account = Create_account()
    # Create_account.showMaximized()
    create_account.show()
    app.exec()
