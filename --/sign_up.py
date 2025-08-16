# * -------------------------------------- sign up ----------------------------------------- #

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sqlite3

from syntax_check import is_valid_email
# from send_otp import *

class Signup_page(QMainWindow):
    switch_to_sign_in = pyqtSignal()
    switch_to_otp_check = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Sign Up')
        self.setGeometry(360, 80, 700, 650)
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_sign_up.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.original_fullname = ''
        self.original_phone_number = ''
        self.original_email = ''

        self.fullname = ''
        self.phone_number = ''
        self.email = ''

        self.fullname_focus = 0
        self.phone_number_focus = 0
        self.email_focus = 0

        self.active_input_box = None

        self.timer = QTimer(self)

        self.sign_up_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.debug_count = 0
        self.valid_count = 0
        self.button_valid = 0

    # *---------- clear focus ---------- #
    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.fullname_input_box, self.phone_number_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.fullname_input_box.clearFocus()
        self.phone_number_input_box.clearFocus()
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


    # *---------- sign_up page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign in -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_in')
        self.back_button.clicked.connect(self.switch_to_sign_in.emit)
        ui.addWidget(self.back_button,alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        ui.addStretch()
        # *----------- SIGN UP ----------- #
        # sign up label
        self.sign_up_label = QLabel('Sign Up')
        self.sign_up_label.setObjectName('sign_up_label')
        self.sign_up_label.setFixedHeight(100)

        # sign up layout
        sign_up_layout = QHBoxLayout()
        sign_up_layout.addStretch()
        sign_up_layout.addWidget(self.sign_up_label,alignment=Qt.AlignmentFlag.AlignTop)
        sign_up_layout.addStretch()
        ui.addLayout(sign_up_layout)


        # *----------- Fullname ----------- #
        # fullname label
        self.fullname_label = QLabel('Full name')
        self.fullname_label.setObjectName('fullname_label')
        self.fullname_label.setFixedSize(350,50)

        # fullname label layout
        fullname_layout = QHBoxLayout()
        fullname_layout.addStretch()
        fullname_layout.addWidget(self.fullname_label,alignment=Qt.AlignmentFlag.AlignBottom)
        fullname_layout.addStretch()
        ui.addLayout(fullname_layout)

        # fullname input box
        self.fullname_input_box = QLineEdit()
        self.fullname_input_box.setObjectName('fullname_input_box')
        self.fullname_input_box.setPlaceholderText('Type your full name')
        self.fullname_input_box.returnPressed.connect(self.fullname_enter)
        self.fullname_input_box.textChanged.connect(self.check_button_style_change)
        # self.fullname_input_box.textChanged.connect(self.validate_fullname)
        self.fullname_input_box.setFixedSize(305, 40)
        self.fullname_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

        # fullname input box layout
        fullname_input_box_layout = QHBoxLayout()
        fullname_input_box_layout.setObjectName('fullname_input_box_layout')
        fullname_input_box_layout.addStretch()
        fullname_input_box_layout.addWidget(self.fullname_input_box,alignment=Qt.AlignmentFlag.AlignBottom)
        fullname_input_box_layout.addStretch()
        ui.addLayout(fullname_input_box_layout)

        # todo fullname error label
        self.fullname_error_label = QLabel('')
        self.fullname_error_label.setObjectName('fullname_error_label')
        self.fullname_error_label.setFixedHeight(25)

        # todo fullname error label layout
        fullname_error_label_layout = QHBoxLayout()
        fullname_error_label_layout.setObjectName('fullname_error_label_layout')
        fullname_error_label_layout.addStretch()
        fullname_error_label_layout.addWidget(self.fullname_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        fullname_error_label_layout.addStretch()
        ui.addLayout(fullname_error_label_layout)


        # *----------- Phone_number ----------- #
        # phone_number label
        self.phone_number_label = QLabel('Phone number')
        self.phone_number_label.setObjectName('phone_number_label')
        self.phone_number_label.setFixedSize(350,50)

        # phone_number label layout
        phone_number_layout = QHBoxLayout()
        phone_number_layout.addStretch()
        phone_number_layout.addWidget(self.phone_number_label,alignment=Qt.AlignmentFlag.AlignTop)
        phone_number_layout.addStretch()
        ui.addLayout(phone_number_layout)

        # phone_number input box
        self.phone_number_input_box = QLineEdit()
        self.phone_number_input_box.setObjectName('phone_number_input_box')
        self.phone_number_input_box.setPlaceholderText('Type your phone number')
        self.phone_number_input_box.returnPressed.connect(self.phone_number_enter)
        self.phone_number_input_box.textChanged.connect(self.check_button_style_change)
        # self.phone_number_input_box.textChanged.connect(self.validate_phone_number)
        self.phone_number_input_box.setFixedSize(305, 40)
        self.phone_number_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

        # phone_number input box layout
        phone_number_input_box_layout = QHBoxLayout()
        phone_number_input_box_layout.setObjectName('phone_number_input_box_layout')
        phone_number_input_box_layout.addStretch()
        phone_number_input_box_layout.addWidget(self.phone_number_input_box,alignment=Qt.AlignmentFlag.AlignTop)
        phone_number_input_box_layout.addStretch()
        ui.addLayout(phone_number_input_box_layout)
        self.previous_text = ''

        # todo phone_number error label
        self.phone_number_error_label = QLabel('')
        self.phone_number_error_label.setObjectName('phone_number_error_label')
        self.phone_number_error_label.setFixedHeight(25)

        # todo phone_number error label layout
        phone_number_error_label_layout = QHBoxLayout()
        phone_number_error_label_layout.setObjectName('phone_number_error_label_layout')
        phone_number_error_label_layout.addStretch()
        phone_number_error_label_layout.addWidget(self.phone_number_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        phone_number_error_label_layout.addStretch()
        ui.addLayout(phone_number_error_label_layout)


        # *----------- Email ----------- #
        # email label
        self.email_label = QLabel('E-mail')
        self.email_label.setObjectName('email_label')
        self.email_label.setFixedSize(350,50)

        # email label layout
        email_label_layout = QHBoxLayout()
        email_label_layout.addStretch()
        email_label_layout.addWidget(self.email_label,alignment=Qt.AlignmentFlag.AlignTop)
        email_label_layout.addStretch()
        ui.addLayout(email_label_layout)

        # email input box
        self.email_input_box = QLineEdit()
        self.email_input_box.setObjectName('email_input_box')
        self.email_input_box.setPlaceholderText('Type your e-mail')
        self.email_input_box.returnPressed.connect(self.email_enter)
        self.email_input_box.textChanged.connect(self.check_button_style_change)
        self.email_input_box.setFixedSize(305,40)
        self.email_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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
        self.previous_email = ''

        # email input box layout
        email_input_box_layout = QHBoxLayout()
        email_input_box_layout.setObjectName('email_input_box_layout')
        email_input_box_layout.addStretch()
        email_input_box_layout.addWidget(self.email_input_box,alignment=Qt.AlignmentFlag.AlignTop)
        email_input_box_layout.addStretch()
        ui.addLayout(email_input_box_layout)

        # todo Email error label
        self.email_error_label = QLabel('')
        self.email_error_label.setObjectName('email_error_label')
        self.email_error_label.setFixedHeight(25)

        # todo email error label layout
        email_error_label_layout = QHBoxLayout()
        email_error_label_layout.setObjectName('email_error_label_layout')
        email_error_label_layout.addStretch()
        email_error_label_layout.addWidget(self.email_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        email_error_label_layout.addStretch()
        ui.addLayout(email_error_label_layout)

        ui.addSpacing(25)


        # *---------- Next button ----------- #
        # next button
        self.next_button = QPushButton('Next')
        self.next_button.setObjectName('next_button')
        self.next_button.setFixedSize(230,37)
        self.next_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.next_button.clicked.connect(self.next_clicked)

        # next button layout
        next_button_layout = QHBoxLayout()
        next_button_layout.setObjectName('next_button_layout')
        next_button_layout.setContentsMargins(0,0,0,80)
        next_button_layout.addStretch()
        next_button_layout.addWidget(self.next_button,alignment=Qt.AlignmentFlag.AlignTop)
        next_button_layout.addStretch()
        ui.addLayout(next_button_layout)

        ui.addStretch()


    # *---------- check fullname enter ---------- #
    def fullname_enter(self):
        self.fullname = self.fullname_input_box.text()

        self.fullname_focus += 1
        if self.fullname_focus >= 1:
            self.check_next()

        if self.valid_count == 0 and self.existing_user and self.existing_user[3] == self.fullname:
            self.check_next()
        elif self.fullname != '' and len(self.fullname) <= 747:
            self.phone_number_input_box.setFocus()

    # *---------- check phone_number enter ---------- #
    def phone_number_enter(self):
        self.phone_number = self.phone_number_input_box.text()

        self.phone_number_focus += 1
        if self.phone_number_focus >= 1:
            self.check_next()

        if self.existing_user and self.existing_user[4] == self.phone_number:
            self.check_next()
        elif self.phone_number.isdigit() and self.phone_number != '' and len(self.phone_number) == 10 and self.fullname != '':
            self.email_input_box.setFocus()
        else: self.check_next()

    # *---------- check email enter ---------- #
    def email_enter(self):
        self.email_focus += 1
        if self.email_focus >= 1:
            self.check_next()

    # *---------- check next button clicked ---------- #
    def next_clicked(self):
        self.fullname = self.fullname_input_box.text()
        self.phone_number = self.phone_number_input_box.text()
        self.email = self.email_input_box.text()

        if self.fullname == '':
            self.fullname_enter()
        elif self.phone_number == '':
            self.phone_number_enter()
        elif self.email == '':
            self.email_enter()
        else:
            self.check_next()


    # *---------- check next ---------- #
    def check_next(self):
        self.fullname = self.fullname_input_box.text()
        self.phone_number = self.phone_number_input_box.text()
        self.email = self.email_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE fullname = ? OR email = ? OR phone_number = ?", (self.fullname, self.email, self.phone_number))
        self.existing_user = self.cursor.fetchone()

        self.valid = False
        self.valid_fullname = False
        self.valid_phone_number = False
        self.valid_email = False

        if self.fullname == '':
            self.valid = False
            # self.phone_number_error_label.setText('')
            # self.email_error_label.setText('')
            self.fullname_error_label.setText('Please enter your fullname')
            self.fullname_input_box_red_border()


        elif self.phone_number == '':
            self.valid = False
            # self.email_error_label.setText('')
            # self.fullname_error_label.setText('')
            if self.phone_number_focus >= 1:
                self.phone_number_error_label.setText('Please enter your phone number')
                self.phone_number_input_box_red_border()

        elif self.email == '':
            self.valid = False
            # self.fullname_error_label.setText('')
            # self.phone_number_error_label.setText('')
            if self.email_focus >= 1:
                self.email_error_label.setText('Please enter your e-mail')
                self.email_input_box_red_border()

        if self.fullname != '' and len(self.fullname) <= 747:
            if self.existing_user:
                if self.existing_user[3] == self.fullname:
                    self.fullname_error_label.setText('This fullname is already exits')
                    self.fullname_input_box_red_border()
                self.valid = False
            elif len(self.fullname) > 747:
                self.fullname_error_label.setText('Full name must not exceed 747 charactors')
                self.fullname_input_box_red_border()
                self.valid = False
            else:
                self.fullname_error_label.setText('')
                self.fullname_input_box_normal_border()
                self.valid_fullname = True

        if self.phone_number != '' and self.valid_fullname :
            if len(self.phone_number) > 0 and self.phone_number[0] >= '1':
                self.phone_number_error_label.setText(f'Phone number can\'t start with {self.phone_number[0]}')
                self.phone_number_input_box_red_border()
                self.valid = False
            elif not self.phone_number.isdigit():
                self.phone_number_error_label.setText('Phone number can only include numbers from 0 to 9')
                self.phone_number_input_box_red_border()
                self.valid = False
            elif len(self.phone_number) != 10:
                self.phone_number_error_label.setText('Phone number must contain exactly 10 digit')
                self.phone_number_input_box_red_border()
                self.valid = False
            elif self.existing_user:
                if self.existing_user[4] == self.phone_number:
                    self.phone_number_error_label.setText('This phone number is already exits')
                    self.phone_number_input_box_red_border()
                self.valid = False
            else:
                self.phone_number_error_label.setText('')
                self.phone_number_input_box_normal_border()
                self.valid_phone_number = True

        if self.email != '' and self.valid_phone_number and self.valid_fullname:
            if not is_valid_email(self.email):
                self.email_error_label.setText('Invalid e-mail')
                self.email_input_box_red_border()
                self.valid = False
            elif self.existing_user:
                if self.existing_user[5] == self.email:
                    self.email_error_label.setText('This email is already exits')
                    self.email_input_box_red_border()
                self.valid = False
            else:
                self.email_error_label.setText('')
                self.email_input_box_normal_border()
                self.valid = True

        if self.valid:
            self.switch_to_otp_check.emit()
            self.clear_focus_from_all()
            print('Data sent successfully')


        self.debug_count += 1
        print(f'--- round {self.debug_count} ---')
        print('fullname : ',self.fullname)
        print('phone number : ',self.phone_number)
        print('email : ',self.email)
        print('valid :',self.valid)
        print('button valid :',self.button_valid)


    def change_button_style_successful(self):
        self.next_button.setStyleSheet('''
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
        self.next_button.setStyleSheet('''
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
        self.fullname = self.fullname_input_box.text()
        self.phone_number = self.phone_number_input_box.text()
        self.email = self.email_input_box.text()

        self.cursor.execute("SELECT * FROM user_account WHERE fullname = ? OR email = ? OR phone_number = ?", (self.fullname, self.email, self.phone_number))
        self.existing_user = self.cursor.fetchone()


        self.button_valid = False
        self.button_valid_fullname = False
        self.button_valid_phone_number = False
        self.button_valid_email = False

        if self.fullname == '':
            self.fullname_error_label.setText('')
            self.fullname_input_box_normal_border()
        if self.phone_number == '':
            self.phone_number_error_label.setText('')
            self.phone_number_input_box_normal_border()
        if self.email == '':
            self.email_error_label.setText('')
            self.email_input_box_normal_border()

        if self.fullname != '' and len(self.fullname) <= 747:
            if self.existing_user:
                if self.existing_user[3] == self.fullname:
                    self.fullname_error_label.setText('This fullname is already exits')
                    self.fullname_input_box_red_border()
                    self.button_valid = False
            elif len(self.fullname) > 747:
                self.fullname_error_label.setText('Full name must not exceed 747 characters')
                self.fullname_input_box_red_border()
                self.button_valid = False
            else:
                self.fullname_error_label.setText('')
                self.fullname_input_box_normal_border()
                self.button_valid_fullname = True

        if self.phone_number != '':
            if len(self.phone_number) > 0 and self.phone_number[0] == '1':
                self.phone_number_error_label.setText('Phone number can\'t start with 1')
                self.phone_number_input_box_red_border()
                self.valid = False
            elif self.phone_number.isdigit() and len(self.phone_number) < 10:
                self.phone_number_error_label.setText('')
                self.phone_number_input_box_normal_border()
                self.button_valid = False
            elif not self.phone_number.isdigit():
                self.phone_number_error_label.setText('Phone number can only include numbers from 0 to 9')
                self.phone_number_input_box_red_border()
                self.button_valid = False
            elif len(self.phone_number) > 10:
                self.phone_number_error_label.setText('Phone number must contain exactly 10 digit')
                self.phone_number_input_box_red_border()
                self.button_valid = False
            elif len(self.phone_number) != 10:
                self.button_valid = False
            elif self.existing_user:
                if self.existing_user[4] == self.phone_number:
                    self.phone_number_error_label.setText('This phone number is already exits')
                    self.phone_number_input_box_red_border()
                    self.button_valid = False
            else:
                self.phone_number_error_label.setText('')
                self.phone_number_input_box_normal_border()
                self.button_valid_phone_number = True

        if self.email != '':
            if not is_valid_email(self.email):
                self.button_valid = False
            elif self.existing_user:
                if self.existing_user[5] == self.email:
                    self.email_error_label.setText('This email is already exits')
                    self.email_input_box_red_border()
                    self.button_valid = False
            else:
                self.email_error_label.setText('')
                if self.button_valid_fullname and self.button_valid_phone_number:
                    self.email_input_box_normal_border()
                    self.button_valid = True

        self.change_button_style_successful() if self.button_valid else self.change_back_button_style()

    def fullname_input_box_red_border(self):
        self.fullname_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #ff7777;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def fullname_input_box_normal_border(self):
        self.fullname_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def phone_number_input_box_red_border(self):
        self.phone_number_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #ff7777;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def phone_number_input_box_normal_border(self):
        self.phone_number_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def email_input_box_red_border(self):
        self.email_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #ff7777;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def email_input_box_normal_border(self):
        self.email_input_box.setStyleSheet('''
            QLineEdit#fullname_input_box,QLineEdit#phone_number_input_box,QLineEdit#email_input_box{

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


            QLineEdit#fullname_input_box:hover, QLineEdit#phone_number_input_box:hover,QLineEdit#email_input_box:hover,QLineEdit#fullname_input_box:focus:hover, QLineEdit#phone_number_input_box:focus:hover,QLineEdit#email_input_box:focus:hover  {

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

            QLineEdit#fullname_input_box:focus,QLineEdit#name_input_box:focus,  QLineEdit#password_input_box:focus, QLineEdit#phone_number_input_box:focus,QLineEdit#email_input_box:focus {

                border-color: #2a2a2a;

            }

            QLineEdit#fullname_input_box::placeholder, QLineEdit#name_input_box::placeholder,#password_input_box::placeholder, QLineEdit#phone_number_input_box::placeholder,QLineEdit#email_input_box::placeholder {

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

    def fetch_user_data(self):
        email =  self.email_input_box.text()
        return email


    def fetch_all_user_data(self):
        fullname = self.fullname_input_box.text()
        phonenumber = self.phone_number_input_box.text()
        email =  self.email_input_box.text()

        return fullname, phonenumber, email

    def clear_input_boxs(self):
        self.fullname_input_box.clear()
        self.phone_number_input_box.clear()
        self.email_input_box.clear()

#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    sign_up = Signup_page()
    # sign_up.showMaximized()
    sign_up.show()
    app.exec()
