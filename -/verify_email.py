
# * -------------------------------------- Forgot Password ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Verify_email_page(QMainWindow):
    switch_to_sign_up = pyqtSignal()
    switch_to_otp_check = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Basketball Score Sheet - Forgot Password')
        self.setGeometry(360, 120, 700, 400) # x,y   w,h
        self.import_style('style_verify_email.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.email = ''
        self.email_focus = 0

        self.send_clicked = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)


    # *---------- clear focus ---------- #
    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.email_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.email_input_box.clearFocus()
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


    # *---------- verify email page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to forgot password -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        self.back_button.clicked.connect(self.switch_to_sign_up.emit)
        ui.addWidget(self.back_button ,alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        ui.addStretch(1)

        # *----------- verify email ----------- #
        # verify email label
        self.verify_email_label = QLabel('Verify Your Email')
        self.verify_email_label.setObjectName('verify_email_label')
        self.verify_email_label.setFixedHeight(100)

        # forgot password layout
        verify_email_layout = QHBoxLayout()
        verify_email_layout.addStretch()
        verify_email_layout.addWidget(self.verify_email_label,alignment=Qt.AlignmentFlag.AlignTop)
        verify_email_layout.addStretch()
        ui.addLayout(verify_email_layout)



        # *----------- Enter e-mail that link with email ----------- #

        self.enter_email_label = QLabel('Please enter an email that link with  "email"')
        self.enter_email_label.setObjectName('enter_email_label')
        self.enter_email_label.setFixedHeight(25)

        enter_email_layout = QHBoxLayout()
        enter_email_layout.addStretch()
        enter_email_layout.addWidget(self.enter_email_label,alignment=Qt.AlignmentFlag.AlignTop)
        enter_email_layout.addStretch()
        ui.addLayout(enter_email_layout)

        ui.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))



        # *----------- Email ----------- #
        # email label
        self.email_label = QLabel('Email')
        self.email_label.setObjectName('email_label')
        self.email_label.setFixedSize(350,60)

        # email label layout
        email_layout = QHBoxLayout()
        email_layout.addStretch()
        email_layout.addWidget(self.email_label,alignment=Qt.AlignmentFlag.AlignTop)
        email_layout.addStretch()
        ui.addLayout(email_layout)

        # email input box
        self.email_input_box = QLineEdit()
        self.email_input_box.setObjectName('email_input_box')
        self.email_input_box.setPlaceholderText('Type your email')
        self.email_input_box.returnPressed.connect(self.check_send)
        self.email_input_box.setFixedSize(305, 40)

        # email input box layout
        email_input_box_layout = QHBoxLayout()
        email_input_box_layout.setObjectName('email_input_box_layout')
        email_input_box_layout.addStretch()
        email_input_box_layout.addWidget(self.email_input_box,alignment=Qt.AlignmentFlag.AlignTop)
        email_input_box_layout.addStretch()
        ui.addLayout(email_input_box_layout)

        # todo email error label
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


        # *---------- Send button ----------- #
        # send button
        self.send_button = QPushButton('Send')
        # self.send_button.setStyleSheet('background: black;')
        self.send_button.setObjectName('send_button')
        self.send_button.setFixedSize(230,37)
        self.send_button.clicked.connect(self.send_clicked)

        # send button layout
        send_button_layout = QHBoxLayout()
        send_button_layout.setObjectName('send_button_layout')
        send_button_layout.setContentsMargins(0,10,0,65)
        send_button_layout.addStretch()
        send_button_layout.addWidget(self.send_button,alignment=Qt.AlignmentFlag.AlignTop)
        send_button_layout.addStretch()
        ui.addLayout(send_button_layout)

        ui.addStretch(2)

    # *---------- check email enter ---------- #
    def email_enter(self):
        self.email_focus += 1
        if self.email_focus >= 1:
            self.check_send()


    # *---------- check send clicked ---------- #
    def send_clicked(self):
        self.email_enter()


    # *---------- check send ---------- #
    def check_send(self):
        self.email = self.email_input_box.text()
        valid = True

        if self.email == '':
            self.email_error_label.setText('Please enter an email')
            valid = False

        if self.email != '':
            self.setFocus(Qt.FocusReason.OtherFocusReason)
            self.switch_to_otp_check.emit()
            self.email_error_label.setText('')



#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    verify_email = Verify_email_page()
    # verify_email.showMaximized()
    verify_email.show()
    app.exec()
