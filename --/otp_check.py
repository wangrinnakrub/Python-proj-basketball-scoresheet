from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

from sign_up import *
from send_otp import *



class OtpInputBox(QLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaxLength(1)
        self.setValidator(QIntValidator(0, 9, self))

    def keyPressEvent(self, event):
        if event.key() in [Qt.Key.Key_0, Qt.Key.Key_1, Qt.Key.Key_2, Qt.Key.Key_3, Qt.Key.Key_4,
                    Qt.Key.Key_5, Qt.Key.Key_6, Qt.Key.Key_7, Qt.Key.Key_8, Qt.Key.Key_9,
                    Qt.Key.Key_Backspace, Qt.Key.Key_Delete, Qt.Key.Key_Left, Qt.Key.Key_Right]:
            super().keyPressEvent(event)
        else:
            event.ignore()

        main_widget = self.parentWidget().parentWidget()
        if main_widget:
            otp_boxes = main_widget.otp_input_boxes
            current_index = otp_boxes.index(self)

        if event.key() == Qt.Key.Key_Backspace:

            if not self.text() and current_index > 0:
                otp_boxes[current_index - 1].setFocus()
            else:
                super().keyPressEvent(event)

        elif event.key() in [Qt.Key.Key_0, Qt.Key.Key_1, Qt.Key.Key_2, Qt.Key.Key_3, Qt.Key.Key_4,
                 Qt.Key.Key_5, Qt.Key.Key_6, Qt.Key.Key_7, Qt.Key.Key_8, Qt.Key.Key_9]:
            super().keyPressEvent(event)
            if self.text():
                if current_index < len(otp_boxes) - 1:
                    otp_boxes[current_index + 1].setFocus()
        else:
            super().keyPressEvent(event)


class otp_check(QMainWindow):
    switch_to_sign_up = pyqtSignal()
    switch_to_create_account = pyqtSignal()
    switch_to_reset_password = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Verify OTP')
        self.setGeometry(360, 180, 700, 400)
        self.import_style('style_otp_check.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        self.wrong_attempts = 0  # เก็บจำนวนครั้งที่กรอก OTP ผิด
        self.lock_time = None
        self.page = ''

    def clear_input_boxs(self):
        for otp_box in self.otp_input_boxes:
            otp_box.clearFocus()
            otp_box.clear()

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)


    def addWidgetsToLayout(self, ui):
        # *------- back -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back')
        self.back_button.clicked.connect(self.switch_to_sign_up.emit)
        ui.addWidget(self.back_button)

        ui.addStretch(1)

        # *----------- OTP ----------- #
        self.otp_label = QLabel('Verify your email')
        self.otp_label.setObjectName('otp_label')
        self.otp_label.setFixedHeight(100)

        otp_label_layout = QHBoxLayout()
        otp_label_layout.addStretch()
        otp_label_layout.addWidget(self.otp_label)
        otp_label_layout.addStretch()
        ui.addLayout(otp_label_layout)

        # *----------- OTP has been sent to email ----------- #
        self.sent_to_label = QLabel('Please wait...')
        self.sent_to_label.setObjectName('sent_to_label')
        self.sent_to_label.setFixedHeight(25)

        sent_tolabel_layout = QHBoxLayout()
        sent_tolabel_layout.addStretch()
        sent_tolabel_layout.addWidget(self.sent_to_label,alignment=Qt.AlignmentFlag.AlignTop)
        sent_tolabel_layout.addStretch()
        ui.addLayout(sent_tolabel_layout)

        # ui.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        ui.addSpacing(30)

        # *---------- otp input box ---------- #
        self.otp_input_boxes = []

        for i in range(6):
            otp_input_box = OtpInputBox()
            otp_input_box.setObjectName(f'otp_input_box_{i+1}')
            otp_input_box.setFixedSize(50, 52)
            otp_input_box.setContentsMargins(0, 3, 4, 0)
            otp_input_box.textChanged.connect(self.on_text_changed)
            self.otp_input_boxes.append(otp_input_box)

        otp_input_box_layout = QHBoxLayout()
        otp_input_box_layout.setObjectName('otp_input_box_layout')
        otp_input_box_layout.addStretch()

        for box in self.otp_input_boxes:
            otp_input_box_layout.addWidget(box, alignment=Qt.AlignmentFlag.AlignTop)

        otp_input_box_layout.addStretch()
        ui.addLayout(otp_input_box_layout)

        ui.addSpacing(20)

        # *----------- OTP error label ----------- #
        self.otp_error_label = QLabel('')
        self.otp_error_label.setObjectName('otp_error_label')
        self.otp_error_label.setFixedHeight(25)

        otp_error_label_layout = QHBoxLayout()
        otp_error_label_layout.addStretch()
        otp_error_label_layout.addWidget(self.otp_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        otp_error_label_layout.addStretch()
        ui.addLayout(otp_error_label_layout)

        ui.addSpacing(10)

        # *----------- resend cooldown label ----------- #
        self.resend_cooldown_error_label = QLabel('')
        self.resend_cooldown_error_label.setObjectName('resend_cooldown_error_label')
        self.resend_cooldown_error_label.setFixedHeight(25)

        resend_cooldown_error_label_layout = QHBoxLayout()
        resend_cooldown_error_label_layout.addStretch()
        resend_cooldown_error_label_layout.addWidget(self.resend_cooldown_error_label,alignment=Qt.AlignmentFlag.AlignTop)
        resend_cooldown_error_label_layout.addStretch()
        ui.addLayout(resend_cooldown_error_label_layout)

        ui.addSpacing(25)

        # *---------- Resend button ----------- #
        self.resend_button = QPushButton('Resend')
        self.resend_button.setObjectName('resend_button')
        self.resend_button.setFixedSize(230,37)
        self.resend_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.resend_button.clicked.connect(self.start_resend_cooldown)

        # send button layout
        resend_button_layout = QHBoxLayout()
        resend_button_layout.setObjectName('resend_button_layout')
        resend_button_layout.setContentsMargins(0,0,0,90)
        resend_button_layout.addStretch()
        resend_button_layout.addWidget(self.resend_button,alignment=Qt.AlignmentFlag.AlignTop)
        resend_button_layout.addStretch()
        ui.addLayout(resend_button_layout)

        ui.addStretch(2)


    def start_resend_cooldown(self):
        self.resend_cooldown_seconds = int(time_until_next_request(self.recipient_email))
        if self.resend_cooldown_seconds > 0:
            self.resend_button.setEnabled(False)
            self.timer.start(1000)
        else:
            self.resend_button.setEnabled(False)
            self.change_back_button_style()
            message = send_otp_email(self.recipient_email)
            if message == 'OTP email sent successfully':
                self.sent_again_count += 1
                self.otp_error_label.setText('')
                self.sent_to_label.setText(f'OTP has been sent tooo {self.mask_email(self.recipient_email)} ({self.sent_again_count}/3)')
            elif message == 'Failed to send OTP email':
                pass
            elif message == 'Please wait before requesting a new OTP.':
                pass
            else:
                self.sent_again_count = 0
                self.change_back_button_style()
                self.resend_cooldown_seconds = message*60
                self.timer.start(1000)


            if message == 'OTP email sent successfully':
                print('OTP has been sent again')
                # self.resend_button.setEnabled(False)
                self.resend_cooldown_seconds = 30
                self.change_back_button_style()
                self.timer.start(1000)
            else:
                self.resend_button.setEnabled(True)
                self.change_button_style_successful()

    def update_timer(self):
        if self.resend_cooldown_seconds > 0:
            self.resend_cooldown_seconds -= 1

            minutes = self.resend_cooldown_seconds // 60
            seconds = self.resend_cooldown_seconds % 60

            if minutes > 0:
                self.resend_cooldown_error_label.setText(f'Request limit reached. Try again after {minutes} minutes')
                print(self.sent_again_count)
                self.resend_button.setEnabled(False)
            else:
                self.resend_cooldown_error_label.setText(f'Please wait {seconds} seconds before requesting a new OTP')
            self.change_back_button_style()
        else:
            self.timer.stop()
            self.resend_button.setEnabled(True)
            self.change_button_style_successful()
            self.resend_cooldown_error_label.setText('')


    def on_text_changed(self):
        all_empty = True

        for i, box in enumerate(self.otp_input_boxes):
            if box.text():
                all_empty = False

        if all_empty:
            self.otp_error_label.setText('')
        else:
            if all(box.text() for box in self.otp_input_boxes):
                otp = ''.join(box.text() for box in self.otp_input_boxes)
                self.verify_otp2(otp)


    def verify_otp2(self, otp_input):
        current_time = time.time()
        result = verify_otp(self.recipient_email, otp_input)
        print(self.recipient_email)
        print(otp_input)

        # หากมีการล็อกอินเนื่องจากการกรอก OTP ผิดเกิน 3 ครั้ง
        if self.wrong_attempts >= 3:
            # ตรวจสอบว่าเวลาผ่านไป 3 นาทีแล้วหรือยัง
            if current_time - self.lock_time < 180:
                remaining_time = 180 - (current_time - self.lock_time)
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                self.otp_error_label.setText(f'You have exceeded the maximum attempts. Please wait {int(minutes)}:{int(seconds)} minutes.')
                self.resend_button.setEnabled(False)
                self.change_back_button_style()
                return
            else:
                # รีเซ็ตการล็อคหลังจากครบ 3 นาที
                self.wrong_attempts = 0
                self.lock_time = None
                self.change_button_style_successful()
                self.resend_button.setEnabled(True)

        # กรอก OTP ผิด
        if result == 'Invalid OTP.':  # ตรวจสอบว่า OTP ที่กรอกไม่ถูกต้อง
            self.wrong_attempts += 1
            if self.wrong_attempts >= 3:
                self.lock_time = current_time  # บันทึกเวลาเมื่อกรอกผิดเกิน 3 ครั้ง
                self.otp_error_label.setText('Too many wrong attempts. Please wait 3 minutes before trying again.')
            else:
                self.otp_error_label.setText('Invalid OTP. Please try again.')
        elif result == 'No OTP found for this email.':
            self.otp_error_label.setText('No OTP found for this email')
        elif result == 'OTP has expired.':
            self.otp_error_label.setText('OTP has expired')
        else:
            self.otp_error_label.setText('OTP is valid!')
            if self.page == 'create_account':
                self.switch_to_create_account.emit()
                print('create_acoount')
            if self.page == 'reset_password':
                self.switch_to_reset_password.emit()
                print('reset_password')

    def receive_data_from_sign_up(self,email):
        self.recipient_email = email
        self.sent_again_count = get_otp_request_count(self.recipient_email)

        self.start_resend_cooldown()
        send_otp_email(self.recipient_email)
        print('otp sent')
        self.sent_to_label.setText(f'OTP has been sent to {self.mask_email(self.recipient_email)} ({self.sent_again_count}/3)')
        self.otp_input_boxes[0].setFocus()
        self.page = 'create_account'

    def receive_data_from_forgot_password(self,email):
        self.recipient_email = email
        self.sent_again_count = get_otp_request_count(self.recipient_email)

        self.start_resend_cooldown()
        send_otp_email(self.recipient_email)
        print('otp sent')
        self.sent_to_label.setText(f'OTP has been sent to {self.mask_email(self.recipient_email)} ({self.sent_again_count}/3)')
        self.otp_input_boxes[0].setFocus()
        self.page = 'reset_password'

    def mask_email(self,email):
        try:
            local, domain = email.split('@')
            if len(local) > 3:
                masked_local = local[:3] + '*' * (len(local) - 3)
            else:
                masked_local = '*' * len(local)
            return f"{masked_local}@{domain}"
        except ValueError:
            return email


    def change_button_style_successful(self):
        self.resend_button.setStyleSheet('''
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
        self.resend_button.setStyleSheet('''
            QPushButton{
            background-color: #2a2a2a;
            color:#ffffff;
            }
            QPushButton:hover{
            background-color: #ffffff;
            color:#2a2a2a;
            }
        ''')



# ! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    Otp_check = otp_check()
    Otp_check.show()
    app.exec()
