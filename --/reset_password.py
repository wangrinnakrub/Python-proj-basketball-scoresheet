
# * -------------------------------------- Reset_password ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from syntax_check import *
from pop_up import *
import sqlite3

class Reset_password(QMainWindow):
    switch_to_forgot_password =  pyqtSignal()
    switch_to_sign_in = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Reset_password')
        self.setGeometry(360, 80, 700, 650) # x,y   w,h
        self.import_style('style_reset_password.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.email = ''

        self.new_password = ''
        self.confirm_new_password = ''

        self.real_new_password = ''
        self.real_confirm_new_password = ''

        self.new_password_focus = 0
        self.confirm_new_password_focus = 0

        self.active_input_box = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_up_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)

        self.connection = sqlite3.connect(r'C:\Users\ASUS\OneDrive\Desktop\Dabest\basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.i = 0


    # *---------- clear focus ---------- #
    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.new_password_input_box, self.confirm_new_password_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.new_password_input_box.clearFocus()
        self.confirm_new_password_input_box.clearFocus()
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


    # *---------- reset_password page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign up -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        self.back_button.clicked.connect(self.go_back_to_forgot_password)
        ui.addWidget(self.back_button)

        ui.addStretch()

        # *----------- reset password ----------- #
        # reset_password label
        self.reset_password_label = QLabel('Reset Password')
        self.reset_password_label.setObjectName('reset_password_label')
        self.reset_password_label.setFixedHeight(100)

        # reset_password layout
        reset_password_layout = QHBoxLayout()
        reset_password_layout.addStretch()
        reset_password_layout.addWidget(self.reset_password_label)
        reset_password_layout.addStretch()
        ui.addLayout(reset_password_layout)


        # *----------- new_Password ----------- #
        # new_password label
        self.new_password_label = QLabel('New Password')
        self.new_password_label.setObjectName('new_password_label')
        self.new_password_label.setFixedSize(350,50)

        # new_password label layout
        new_password_layout = QHBoxLayout()
        new_password_layout.addStretch()
        new_password_layout.addWidget(self.new_password_label)
        new_password_layout.addStretch()
        ui.addLayout(new_password_layout)

        # new_password input box
        self.new_password_input_box = QLineEdit()
        self.new_password_input_box.setObjectName('new_password_input_box')
        self.new_password_input_box.setPlaceholderText('Type your new password')
        self.new_password_input_box.returnPressed.connect(self.new_password_enter)
        self.new_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.new_password_input_box, self.new_password_input_box.text(), is_new_password=True))
        self.new_password_input_box.textChanged.connect(self.check_button_style_change)
        self.new_password_input_box.setFixedSize(305, 40)
        self.new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #2a2a2a;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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

        # new_password input box layout
        new_password_input_box_layout = QHBoxLayout()
        new_password_input_box_layout.setObjectName('new_password_input_box_layout')
        new_password_input_box_layout.addStretch()
        new_password_input_box_layout.addWidget(self.new_password_input_box)
        new_password_input_box_layout.addStretch()
        ui.addLayout(new_password_input_box_layout)
        self.previous_text = ''

        # todo new_password error label
        self.new_password_error_label = QLabel('')
        self.new_password_error_label.setObjectName('new_password_error_label')
        self.new_password_error_label.setFixedHeight(20)

        # todo new_password error label layout
        new_password_error_label_layout = QHBoxLayout()
        new_password_error_label_layout.setObjectName('new_password_error_label_layout')
        new_password_error_label_layout.addStretch()
        new_password_error_label_layout.addWidget(self.new_password_error_label)
        new_password_error_label_layout.addStretch()
        ui.addLayout(new_password_error_label_layout)


        # *----------- Confirm new password ----------- #
        # confirm_new_password label
        self.confirm_new_password_label = QLabel('Confirm New Password')
        self.confirm_new_password_label.setObjectName('confirm_new_password_label')
        self.confirm_new_password_label.setFixedSize(350,50)

        # confirm_new_password label layout
        confirm_new_password_label_layout = QHBoxLayout()
        confirm_new_password_label_layout.addStretch()
        confirm_new_password_label_layout.addWidget(self.confirm_new_password_label)
        confirm_new_password_label_layout.addStretch()
        ui.addLayout(confirm_new_password_label_layout)

        # confirm_new_password input box
        self.confirm_new_password_input_box = QLineEdit()
        self.confirm_new_password_input_box.setObjectName('confirm_new_password_input_box')
        self.confirm_new_password_input_box.setPlaceholderText('Type your confirm new password')
        self.confirm_new_password_input_box.returnPressed.connect(self.confirm_new_password_enter)
        self.confirm_new_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.confirm_new_password_input_box, self.confirm_new_password_input_box.text(), is_new_password=False))
        self.confirm_new_password_input_box.textChanged.connect(self.check_button_style_change)
        self.confirm_new_password_input_box.setFixedSize(305,50)
        self.confirm_new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #2a2a2a;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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
        self.previous_confirm_new_password = ''

        # confirm_new_password input box layout
        confirm_new_password_input_box_layout = QHBoxLayout()
        confirm_new_password_input_box_layout.setObjectName('confirm_new_password_input_box_layout')
        confirm_new_password_input_box_layout.addStretch()
        confirm_new_password_input_box_layout.addWidget(self.confirm_new_password_input_box)
        confirm_new_password_input_box_layout.addStretch()
        ui.addLayout(confirm_new_password_input_box_layout)

        # todo Confirm_new_password error label
        self.confirm_new_password_error_label = QLabel('')
        self.confirm_new_password_error_label.setObjectName('confirm_new_password_error_label')
        self.confirm_new_password_error_label.setFixedHeight(20)

        # todo confirm_new_password error label layout
        confirm_new_password_error_label_layout = QHBoxLayout()
        confirm_new_password_error_label_layout.setObjectName('confirm_new_password_error_label_layout')
        confirm_new_password_error_label_layout.addStretch()
        confirm_new_password_error_label_layout.addWidget(self.confirm_new_password_error_label)
        confirm_new_password_error_label_layout.addStretch()
        ui.addLayout(confirm_new_password_error_label_layout)

        ui.addSpacing(25)

        # *---------- Reset password button ----------- #
        # sign_up button
        self.confirm_button = QPushButton('Confirm')
        self.confirm_button.setObjectName('confirm_button')
        self.confirm_button.setFixedSize(230,37)
        self.confirm_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.confirm_button.clicked.connect(self.reset_password_clicked)

        # reset_password button layout
        confirm_layout = QHBoxLayout()
        confirm_layout.setObjectName('confirm_layout')
        confirm_layout.setContentsMargins(0,10,0,65)
        confirm_layout.addStretch()
        confirm_layout.addWidget(self.confirm_button)
        confirm_layout.addStretch()
        ui.addLayout(confirm_layout)

        ui.addStretch()


    def handle_text_change(self, input_box, text, is_new_password=True):
        if self.timer.isActive():
            self.timer.stop()

        self.active_input_box = input_box
        is_typing = len(text) > (len(self.previous_text) if is_new_password else len(self.previous_confirm_new_password))

        if is_new_password:
            if is_typing:
                self.real_new_password += text[-1]
            else:
                self.real_new_password = self.real_new_password[:-1]

            if is_typing:
                masked_password = '●' * (len(self.real_new_password) - 1) + self.real_new_password[-1]
                self.timer.start(700)
            else:
                masked_password = '●' * len(self.real_new_password)

            self.previous_text = self.real_new_password
            input_box.blockSignals(True)
            input_box.setText(masked_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_password))

        else:
            if is_typing:
                self.real_confirm_new_password += text[-1]
            else:
                self.real_confirm_new_password = self.real_confirm_new_password[:-1]

            if is_typing:
                masked_confirm_password = '●' * (len(self.real_confirm_new_password) - 1) + self.real_confirm_new_password[-1]
                self.timer.start(700)
            else:
                masked_confirm_password = '●' * len(self.real_confirm_new_password)

            self.previous_confirm_new_password = self.real_confirm_new_password
            input_box.blockSignals(True)
            input_box.setText(masked_confirm_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_confirm_password))

    # *---------- mask last character after timeout ---------- #
    def mask_last_character(self):
        self.timer.stop()
        if self.active_input_box is not None:
            if self.active_input_box == self.new_password_input_box:
                masked_password = '●' * len(self.real_new_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_password))

            elif self.active_input_box == self.confirm_new_password_input_box:
                masked_confirm_password = '●' * len(self.real_confirm_new_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_confirm_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_confirm_password))

    # *---------- check new password enter ---------- #
    def new_password_enter(self):
        self.new_password_input_box.textChanged.connect(self.validate_password)
        self.new_password_focus += 1
        if self.new_password_focus >= 1:
            self.check_reset_password()

        if is_valid_password(self.real_new_password) and len(self.real_new_password) >= 8 and len(self.real_new_password) <= 20 :
            self.confirm_new_password_input_box.setFocus()

    # *---------- check confirm new password enter ---------- #
    def confirm_new_password_enter(self):
        self.confirm_new_password_focus += 1
        if self.confirm_new_password_focus >= 1:
            self.check_reset_password()

    # *---------- check reset password clicked ---------- #
    def reset_password_clicked(self):
        if self.real_new_password == '':
            self.new_password_enter()
        elif self.real_confirm_new_password == '':
            self.confirm_new_password_enter()
        else:
            self.check_reset_password()

    #*---------- password realtime check ----------- #
    def validate_password(self):
        if len(self.real_new_password) > 20:
            self.new_password_error_label.setText('Password must not exceed 20 characters')
        elif is_valid_password(self.real_new_password) and len(self.real_new_password) >= 8:
            self.new_password_error_label.setText('')
        elif self.real_new_password == '':
            self.new_password_error_label.setText('')
        elif not is_valid_password(self.real_new_password) and len(self.real_new_password) >= 8:
            self.new_password_error_label.setText('Password must have 1 lowercase, 1 uppercase and 1 digit')

    # *---------- check reset_password ---------- #
    def check_reset_password(self):
        self.valid = False

        if self.real_new_password == '':
            self.valid = False
            self.confirm_new_password_error_label.setText('')
            if self.new_password_focus >= 1:
                self.new_password_error_label.setText('Please enter your password')
                self.new_password_input_box_red_border()

        elif self.real_confirm_new_password == '':
            self.valid = False
            self.new_password_error_label.setText('')
            if self.confirm_new_password_focus >= 1:
                self.confirm_new_password_error_label.setText('Please enter your confirm password')
                self.confirm_new_password_input_box_red_border()

        if self.real_new_password != '':
            if len(self.real_new_password) > 20:
                self.new_password_error_label.setText('Password must not exceed 20 charactors')
                self.new_password_input_box_red_border()
                self.valid = False
            elif len(self.real_new_password) > 0 and len(self.real_new_password) < 8:
                self.new_password_error_label.setText('Password must contain at least 8 characters')
                self.new_password_input_box_red_border()
                self.valid = False
            elif not is_valid_password(self.real_new_password):
                self.new_password_error_label.setText('Password must have 1 lowercase, 1 uppercase and 1 digit')
                self.new_password_input_box_red_border()
                self.confirm_new_password_error_label.setText('')
                self.valid = True
            else:
                self.new_password_input_box_normal_border()
                self.new_password_error_label.setText('')

        if self.real_confirm_new_password != '' and self.real_new_password != '':
            if self.real_confirm_new_password != self.real_new_password:
                self.confirm_new_password_error_label.setText('Password does not match')
                self.confirm_new_password_input_box_red_border()
                self.valid = False
            elif is_valid_password(self.real_new_password) and self.real_confirm_new_password == self.real_new_password:
                self.confirm_new_password_error_label.setText('')
                self.confirm_new_password_input_box_normal_border()
                self.clear_focus_from_all()
                self.update_password()
                self.switch_to_sign_in.emit()
                self.valid = True


        # debug
        self.i+=1
        print(f'--- Test {self.i} ---')
        print("Real Password:", self.real_new_password)
        print("Confirm Password:", self.real_confirm_new_password)


    def change_button_style_successful(self):
        self.confirm_button.setStyleSheet('''
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
        self.confirm_button.setStyleSheet('''
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


        if self.real_new_password == '': self.new_password_input_box_normal_border()
        if self.real_confirm_new_password == '': self.confirm_new_password_input_box_normal_border()

        if self.real_new_password != '':
            if len(self.real_new_password) > 20:
                self.new_password_error_label.setText('Password must not exceed 20 charactors')
                self.new_password_input_box_red_border()
                self.valid = False
            elif not is_valid_password(self.real_new_password) and len(self.real_new_password) >= 8:
                self.new_password_error_label.setText('Password must have 1 lowercase, 1 uppercase and 1 digit')
                self.new_password_input_box_normal_border()
                self.valid = False
            else:
                self.new_password_error_label.setText('')
                self.new_password_input_box_normal_border()

        if self.real_confirm_new_password != '':
            if is_valid_password(self.real_new_password):
                self.change_button_style_successful() if self.real_new_password == self.real_confirm_new_password else self.change_back_button_style()
                self.confirm_new_password_input_box_normal_border()
                self.new_password_input_box_normal_border()

    def receive_data_from_forgot_password(self,email):
        self.email = email
        print(self.email)

    def update_password(self):
        self.cursor.execute("SELECT * FROM user_account WHERE email = ?", (self.email,))
        self.existing_user = self.cursor.fetchone()

        if self.existing_user:
            self.cursor.execute("""
                UPDATE user_account
                SET password = ?
                WHERE id = (SELECT MAX(id) FROM user_account)
            """, (self.real_new_password,))
            print('password updated')
        else:
            print('can\'t update password')

        self.connection.commit()

    def go_back_to_forgot_password(self):
        popup = PopupWindow()
        popup.change_label()
        parent_pos = self.mapToGlobal(QPoint(0, 0))
        main_window_geometry = QRect(parent_pos, self.size())

        x = main_window_geometry.left() + (main_window_geometry.width() - popup.width()) // 2
        y = main_window_geometry.top() + (main_window_geometry.height()*9//20) - popup.height() // 2
        popup.move(x, y)

        result = popup.exec()
        print(result)
        if result: self.switch_to_forgot_password.emit()
        else: popup.close()

    def clear_input_boxs(self):
        self.new_password_input_box.clear()
        self.confirm_new_password_input_box.clear()

    def new_password_input_box_normal_border(self):
        self.new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #2a2a2a;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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

    def confirm_new_password_input_box_normal_border(self):
        self.confirm_new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #2a2a2a;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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

    def new_password_input_box_red_border(self):
        self.new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #ff7777;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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

    def confirm_new_password_input_box_red_border(self):
        self.confirm_new_password_input_box.setStyleSheet('''
QLineEdit#new_password_input_box,QLineEdit#confirm_new_password_input_box {

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


QLineEdit#new_password_input_box:hover,QLineEdit#confirm_new_password_input_box:hover,QLineEdit#new_password_input_box:focus:hover, QLineEdit#confirm_new_password_input_box:focus:hover  {

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
QLineEdit#new_password_input_box:focus,QLineEdit#confirm_new_password_input_box:focus {

    border-color: #ff7777;

}
QLineEdit#new_password_input_box::placeholder,QLineEdit#confirm_new_password_input_box::placeholder {

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
    reset_password = Reset_password()
    # Reset_password.showMaximized()
    reset_password.show()
    app.exec()
