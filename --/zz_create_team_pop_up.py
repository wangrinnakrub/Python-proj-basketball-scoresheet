import sys,sqlite3,re
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from datetime import datetime
from zzz_inner_popup import InnerPopup

class HoverButton(QPushButton):
    def __init__(self, file_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setObjectName('player_add_image')

        if file_name == 'c:\pic\plus_icon.png':
            self.file_name = file_name
            self.file_name_hover = r'C:\pic\plus_icon_hover_white.png'
            self.setIcon(QIcon(self.file_name))
            self.setIconSize(QSize(127,127))
        else:
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\change_image_label.png'

            self.setContentsMargins(0, 0, 0, 0)
            self.setIcon(QIcon())
            self.setStyleSheet(f"""
                    QPushButton#player_add_image {{
                        border: none;
                        background: transparent;
                        border-image: url('{self.file_name}');
                        margin: 0;
                        padding: 0;
                    }}
                    """)

    def enterEvent(self, event):
        if self.file_name == 'c:\pic\plus_icon.png':
            self.setStyleSheet('''
                            background-color: #d3d3d3;
                            border: none;
                                ''')
            self.setIconSize(QSize(127,127))
        else:
            self.setContentsMargins(0, 0, 0, 0)
            self.setIcon(QIcon())
            self.setStyleSheet(f"""
                    QPushButton#player_add_image {{
                        border: none;
                        background: transparent;
                        border-image: url('{self.file_name}');
                        margin: 0;
                        padding: 0;
                    }}
                    """)

        # self.setIcon(QIcon(self.file_name))
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.file_name == 'c:\pic\plus_icon.png':
            self.setIcon(QIcon(self.file_name))
            self.setIconSize(QSize(127,127))
            self.setStyleSheet("")
        else:
            self.setContentsMargins(0, 0, 0, 0)
            self.setIcon(QIcon())
            self.setStyleSheet(f"""
                    QPushButton#player_add_image {{
                        border: none;
                        background: transparent;
                        border-image: url('{self.file_name}');
                        margin: 0;
                        padding: 0;
                    }}
                    """)
        super().leaveEvent(event)

class AddPlayer(QDialog):
    def __init__(self,information=None):
        super().__init__()
        self.setWindowTitle(' ')
        self.setFixedSize(390, 730)
        # self.setFixedSize(390, 570)
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_zz_create_team_pop_up.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()
        QTimer.singleShot(0, self.clear_focus_from_all)

        self.installEventFilter(self)

        if information is not None:
            self.set_information(information)

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def clear_focus_from_all(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.player_name_input_box, self.player_number_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        self.setLayout(self.layout)

    def addWidgetsToLayout(self, ui):

        # *---------- add image button ----------* #
        self.player_add_image = HoverButton('c:\pic\plus_icon.png')
        self.player_add_image.setIcon(QIcon(r'c:\pic\plus_icon.png'))
        self.player_add_image.setIconSize(QSize(127,127))
        self.player_add_image.setObjectName('player_add_image')
        self.player_add_image.setFixedSize(120,140)
        self.player_add_image.clicked.connect(self.add_image)

        self.player_add_image_layout = QHBoxLayout()
        self.player_add_image_layout.addWidget(self.player_add_image)


        # *---------- Player number under image ----------* #
        self.player_number_under_image_label = QLabel('')
        self.player_number_under_image_label.setObjectName('player_number_under_image_label')
        self.player_number_under_image_label.setFixedSize(335,40)
        self.player_number_under_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player_number_under_image_label_layout = QHBoxLayout()
        self.player_number_under_image_label_layout.addWidget(self.player_number_under_image_label)


        # ?-------------------------- 1st layout --------------------------* #

        # *---------- Player name ----------* #
        self.player_name_label = QLabel('Name')
        self.player_name_label.setObjectName('player_name_label')
        self.player_name_label.setFixedSize(345,20)
        self.player_name_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_name_label_layout = QHBoxLayout()
        self.player_name_label_layout.addWidget(self.player_name_label)

        self.player_name_input_box = QLineEdit()
        self.player_name_input_box.setObjectName('player_name_input_box')
        self.player_name_input_box.setPlaceholderText('Type your player name')
        self.player_name_input_box.setFixedHeight(40)
        self.player_name_input_box.setMinimumWidth(350)
        self.player_name_input_box_layout = QHBoxLayout()
        self.player_name_input_box_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.player_name_input_box_layout.addWidget(self.player_name_input_box)
        self.player_name_input_box_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))


        # ?-------------------------- 2nd layout --------------------------* #
        self.player_number_tall_weight_layout = QHBoxLayout()

        # *---------- Player number ----------* #
        self.player_number_label = QLabel('No.')
        self.player_number_label.setObjectName('player_number_label')
        self.player_number_label.setFixedHeight(30)
        self.player_number_label.setFixedWidth(100)
        # self.player_number_label.setFixedSize(350,30)
        self.player_number_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_number_label_layout = QHBoxLayout()
        self.player_number_label_layout.addWidget(self.player_number_label)

        self.player_number_input_box = QLineEdit()
        self.player_number_input_box.setObjectName('player_number_input_box')
        self.player_number_input_box.setPlaceholderText('No.')
        self.player_number_input_box.setFixedHeight(40)
        self.player_number_input_box.setFixedWidth(110)

        self.player_number_input_box_layout = QHBoxLayout()
        self.player_number_input_box_layout.addWidget(self.player_number_input_box)
        self.player_number_input_box.textChanged.connect(self.player_number_under_image_real_time_change)
        self.player_number_input_box.setValidator(QIntValidator(0, 99))

        self.player_number_layout = QVBoxLayout()
        self.player_number_layout.addLayout(self.player_number_label_layout)
        self.player_number_layout.addLayout(self.player_number_input_box_layout)


        # *---------- Player height ----------* #
        self.player_height_label = QLabel('Height')
        self.player_height_label.setObjectName('player_height_label')
        self.player_height_label.setFixedHeight(30)
        self.player_height_label.setFixedWidth(100)
        self.player_height_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_height_label_layout = QHBoxLayout()
        self.player_height_label_layout.addWidget(self.player_height_label)

        self.player_height_input_box = QLineEdit()
        self.player_height_input_box.setObjectName('player_height_input_box')
        self.player_height_input_box.setPlaceholderText('cm.')
        self.player_height_input_box.setFixedHeight(40)
        self.player_height_input_box.setFixedWidth(110)
        # self.player_height_input_box.setFixedSize(305,40)
        self.player_height_input_box_layout = QHBoxLayout()
        self.player_height_input_box_layout.addWidget(self.player_height_input_box)
        self.player_height_input_box.setValidator(QIntValidator(0, 999))

        self.player_height_layout = QVBoxLayout()
        self.player_height_layout.addLayout(self.player_height_label_layout)
        self.player_height_layout.addLayout(self.player_height_input_box_layout)


        # *---------- Player weight ----------* #
        self.player_weight_label = QLabel('Weight')
        self.player_weight_label.setObjectName('player_weight_label')
        self.player_weight_label.setFixedHeight(30)
        self.player_weight_label.setFixedWidth(100)
        self.player_weight_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_weight_label_layout = QHBoxLayout()
        self.player_weight_label_layout.addWidget(self.player_weight_label)

        self.player_weight_input_box = QLineEdit()
        self.player_weight_input_box.setObjectName('player_weight_input_box')
        self.player_weight_input_box.setPlaceholderText('kg.')
        self.player_weight_input_box.setFixedHeight(40)
        self.player_weight_input_box.setFixedWidth(110)
        # self.player_weight_input_box.setFixedSize(305,40)
        self.player_weight_input_box_layout = QHBoxLayout()
        self.player_weight_input_box_layout.addWidget(self.player_weight_input_box)
        self.player_weight_input_box.setValidator(QIntValidator(0, 99))

        self.player_weight_layout = QVBoxLayout()
        self.player_weight_layout.addLayout(self.player_weight_label_layout)
        self.player_weight_layout.addLayout(self.player_weight_input_box_layout)


        # self.player_number_tall_weight_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.player_number_tall_weight_layout.addLayout(self.player_number_layout)
        self.player_number_tall_weight_layout.addLayout(self.player_height_layout)
        self.player_number_tall_weight_layout.addLayout(self.player_weight_layout)
        # self.player_number_tall_weight_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # ?-------------------------- 3rd layout --------------------------* #
        self.player_birthday_status_layout = QHBoxLayout()

        # *---------- Player birthday ----------* #
        self.player_birthday_label = QLabel('Birthday')
        self.player_birthday_label.setObjectName('player_birthday_label')
        self.player_birthday_label.setFixedHeight(30)
        self.player_birthday_label.setFixedWidth(162)
        self.player_birthday_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_birthday_label_layout = QHBoxLayout()
        self.player_birthday_label_layout.addWidget(self.player_birthday_label)

        self.player_birthday_input_box = QLineEdit()
        self.player_birthday_input_box.setObjectName('player_birthday_input_box')
        self.player_birthday_input_box.setPlaceholderText('00 / 00 / 0000')
        self.player_birthday_input_box.setFixedHeight(40)
        self.player_birthday_input_box.setFixedWidth(165)
        self.player_birthday_input_box_layout = QHBoxLayout()
        self.player_birthday_input_box_layout.addWidget(self.player_birthday_input_box)
        self.player_birthday_input_box.setValidator(QIntValidator(0, 99999999))
        self.player_birthday_input_box.textChanged.connect(self.player_birthday_input_box_auto_slash)


        self.player_birthday_layout = QVBoxLayout()
        self.player_birthday_layout.addLayout(self.player_birthday_label_layout)
        self.player_birthday_layout.addLayout(self.player_birthday_input_box_layout)


        # *---------- Player status ----------* #
        self.player_status_label = QLabel('status')
        self.player_status_label.setObjectName('player_status_label')
        self.player_status_label.setFixedHeight(30)
        self.player_status_label.setFixedWidth(162)
        self.player_status_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.player_status_label_layout = QHBoxLayout()
        self.player_status_label_layout.addWidget(self.player_status_label)

        self.player_status_combobox = QComboBox()
        self.player_status_combobox.setObjectName('player_status_combobox')
        self.player_status_combobox.addItems(['High School', 'Undergraduate', 'Graduate'])
        self.player_status_combobox.setFixedHeight(35)
        self.player_status_combobox.setFixedWidth(162)
        self.player_status_combobox.setCurrentIndex(-1)
        self.player_status_combobox_layout = QHBoxLayout()
        self.player_status_combobox_layout.addWidget(self.player_status_combobox)

        self.player_status_layout = QVBoxLayout()
        self.player_status_layout.addLayout(self.player_status_label_layout)
        self.player_status_layout.addLayout(self.player_status_combobox_layout)

        self.player_birthday_status_layout.addLayout(self.player_birthday_layout)
        self.player_birthday_status_layout.addLayout(self.player_status_layout)

        # ?-------------------------- 4th layout --------------------------* #

        self.student_id_thai_id_layout = QHBoxLayout()

        # *---------- student id ----------* #
        self.student_id_label = QLabel('Student ID')
        self.student_id_label.setObjectName('student_id_label')
        self.student_id_label.setFixedHeight(30)
        self.student_id_label.setFixedWidth(162)
        self.student_id_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.student_id_label_layout = QHBoxLayout()
        self.student_id_label_layout.addWidget(self.student_id_label)

        self.student_id_input_box = QLineEdit()
        self.student_id_input_box.setObjectName('student_id_input_box')
        self.student_id_input_box.setPlaceholderText('xxxxxxxxxx')
        self.student_id_input_box.setFixedHeight(40)
        self.student_id_input_box.setFixedWidth(165)
        self.student_id_input_box_layout = QHBoxLayout()
        self.student_id_input_box_layout.addWidget(self.student_id_input_box)
        self.student_id_input_box.setValidator(QRegularExpressionValidator(QRegularExpression(r'\d{10}'), self.student_id_input_box))
        # self.student_id_input_box.textChanged.connect(self.)

        self.student_id_layout = QVBoxLayout()
        self.student_id_layout.addLayout(self.student_id_label_layout)
        self.student_id_layout.addLayout(self.student_id_input_box_layout)


        # *---------- thai id ----------* #
        self.thai_id_label = QLabel('Thai ID')
        self.thai_id_label.setObjectName('thai_id_label')
        self.thai_id_label.setFixedHeight(30)
        self.thai_id_label.setFixedWidth(162)
        self.thai_id_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.thai_id_label_layout = QHBoxLayout()
        self.thai_id_label_layout.addWidget(self.thai_id_label)

        self.thai_id_input_box = QLineEdit()
        self.thai_id_input_box.setObjectName('thai_id_input_box')
        self.thai_id_input_box.setPlaceholderText('xxxxxxxxxxxxx')
        self.thai_id_input_box.setFixedHeight(40)
        self.thai_id_input_box.setFixedWidth(165)
        self.thai_id_input_box_layout = QHBoxLayout()
        self.thai_id_input_box_layout.addWidget(self.thai_id_input_box)
        self.thai_id_input_box.setValidator((QRegularExpressionValidator(QRegularExpression(r'\d{13}'), self.thai_id_input_box)))
        # self.thai_id_input_box.textChanged.connect(self.)

        self.thai_id_layout = QVBoxLayout()
        self.thai_id_layout.addLayout(self.thai_id_label_layout)
        self.thai_id_layout.addLayout(self.thai_id_input_box_layout)

        self.student_id_thai_id_layout.addLayout(self.student_id_layout)
        self.student_id_thai_id_layout.addLayout(self.thai_id_layout)


        # ?-------------------------- 5th layout --------------------------* #

        # *---------- Phone number ----------* #
        self.phone_number_label = QLabel('Phone Number')
        self.phone_number_label.setObjectName('phone_number_label')
        self.phone_number_label.setFixedSize(345,30)
        self.phone_number_label.setAlignment(Qt.AlignmentFlag.AlignBottom)
        self.phone_number_label_layout = QHBoxLayout()
        self.phone_number_label_layout.addWidget(self.phone_number_label)

        self.phone_number_input_box = QLineEdit()
        self.phone_number_input_box.setObjectName('phone_number_input_box')
        self.phone_number_input_box.setPlaceholderText('Type your phone number')
        # self.phone_number_input_box.setFixedSize(305,40)
        self.phone_number_input_box.setFixedHeight(40)
        self.phone_number_input_box.setMinimumWidth(350)
        self.phone_number_input_box_layout = QHBoxLayout()
        self.phone_number_input_box_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.phone_number_input_box_layout.addWidget(self.phone_number_input_box)
        self.phone_number_input_box_layout.addSpacerItem(QSpacerItem(10, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.phone_number_input_box.setValidator((QRegularExpressionValidator(QRegularExpression(r'\d{10}'), self.phone_number_input_box)))
        # self.phone_number_input_box.textChanged.connect(self.)

        # ?-------------------------- button layout --------------------------* #

        # *---------- cancel button ----------* #
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setObjectName('cancel_button')
        self.cancel_button.setFixedSize(145,40)
        self.cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.cancel_button.clicked.connect(self.reject)

        self.cancel_button_layout = QHBoxLayout()
        self.cancel_button_layout.setObjectName('cancel_button_layout')
        self.cancel_button_layout.addStretch()
        self.cancel_button_layout.addWidget(self.cancel_button)

        self.cancel_button_layout.addSpacing(10)

        # *---------- ok button ----------* #
        self.ok_button = QPushButton('Ok')
        self.ok_button.setObjectName('ok_button')
        self.ok_button.setFixedSize(145,40)
        self.ok_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.ok_button.clicked.connect(self.ok_button_clicked)
        self.cancel_button_layout.addWidget(self.ok_button)
        self.cancel_button_layout.addStretch()


        #?-------------------------  manage layouts  -------------------------#*

        ui.addStretch()
        ui.addLayout(self.player_add_image_layout)
        ui.addStretch()
        ui.addLayout(self.player_number_under_image_label_layout)

        ui.addLayout(self.player_name_label_layout)
        ui.addLayout(self.player_name_input_box_layout)

        ui.addLayout(self.player_number_tall_weight_layout)

        ui.addLayout(self.player_birthday_status_layout)

        ui.addLayout(self.student_id_thai_id_layout)

        ui.addLayout(self.phone_number_label_layout)
        ui.addLayout(self.phone_number_input_box_layout)

        ui.addStretch()
        ui.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        ui.addLayout(self.cancel_button_layout)
        ui.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        ui.addStretch()

        #?------------------------------------------------------------------------#*

    def add_image(self):
        try:
            file_name, _ = QFileDialog.getOpenFileName(
                self,
                "Select Image",
                "",
                "Image Files (*.png *.jpg *.bmp)"
            )
            if file_name:
                self.player_add_image.deleteLater()
                self.player_add_image = HoverButton(file_name)
                self.player_add_image.setObjectName('player_add_image')
                self.player_add_image.setFixedSize(120, 140)
                # self.player_add_image.setEnabled(False)
                # self.player_add_image.clicked.connect(self.add_image)
                self.player_add_image.disconnect()

                self.player_add_image_layout.addWidget(self.player_add_image)
        except Exception as e:
            print(f"Error loading image: {e}")


    def player_number_under_image_real_time_change(self):
        text = self.player_number_input_box.text()

        if len(text) > 2:
            text = text[:2]

        zero_count = text.count('0')
        if zero_count > 2:
            text = text.rstrip('0')
        elif zero_count == 2 and len(text) > 2:
            text = text.rstrip('0')

        if zero_count > 1 and any(char != '0' for char in text):
            text = text.lstrip('0')

        self.player_number_input_box.setText(text)
        self.player_number_under_image_label.setText(text)

    def player_birthday_input_box_auto_slash(self):
        text = self.player_birthday_input_box.text()
        self.new_text = text

        self.new_text = self.new_text.replace("/", "").replace(" ", "")

        if len(self.new_text) > 8:
            self.new_text = self.new_text[:8]

        if len(self.new_text) > 2:
            self.new_text = self.new_text[:2] + ' / ' + self.new_text[2:]
        if len(self.new_text) > 7:
            self.new_text = self.new_text[:7] + ' / ' + self.new_text[7:]

        self.player_birthday_input_box.blockSignals(True)
        self.player_birthday_input_box.setText(self.new_text)
        self.player_birthday_input_box.setCursorPosition(len(self.new_text))
        self.player_birthday_input_box.blockSignals(False)

    def validate_birthday(self, text):
        if len(text) == 14:
            try:
                day, month, year = int(text[:2]), int(text[5:7]), int(text[10:])
                birth_date = datetime(year, month, day)
                today = datetime.today()
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                if age < 7:
                    raise ValueError("Age must be at least 7 years")
                if age > 123:
                    raise ValueError("Age must be at most 123 years")
                if month < 1 or month > 12:
                    raise ValueError("Invalid month")
                if day < 1 or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or (month in [4, 6, 9, 11] and day > 30) or (month == 2 and day > (29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28)):
                    raise ValueError("Invalid day for the given month")
            except ValueError as e:
                # self.player_birthday_input_box.blockSignals(True)
                # self.player_birthday_input_box.setText("")
                # self.player_birthday_input_box.blockSignals(False)
                return e
            return True

    def validate_phone_number(self, phone_number):
        if len(phone_number) != 10:
            return False
        if phone_number[0] != '0':
            return False
        if phone_number[1] not in ['6', '8', '9']:
            return False
        return True

    def get_player_image_path(self):
        style_sheet = self.player_add_image.styleSheet()
        match = re.search(r'border-image:\s*url\((.*?)\)', style_sheet)
        if match:
            return match.group(1)
        return None

    def get_player_name(self):
        return self.player_name_input_box.text()

    def get_player_name_styled(self):
        return self.player_number_under_image_label.styleSheet()

    def ok_button_clicked(self):

        # inner_popup = InnerPopup()
        # inner_popup.setWindowModality(Qt.WindowModality.ApplicationModal)
        # inner_popup.move(self.geometry().center() - inner_popup.rect().center())

        # if self.player_name_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the player name')
        #     inner_popup.exec()
        #     return
        # elif self.player_number_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the player number')
        #     inner_popup.exec()
        #     return
        # elif self.player_height_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the player height')
        #     inner_popup.exec()
        #     return
        # elif self.player_weight_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the player weight')
        #     inner_popup.exec()
        #     return
        # elif self.player_birthday_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the player birthday')
        #     inner_popup.exec()
        #     return
        # elif self.player_status_combobox.currentText() == '':
        #     inner_popup.change_label_to('Please fill in the player status')
        #     inner_popup.exec()
        #     return
        # elif self.student_id_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the student id')
        #     inner_popup.exec()
        #     return
        # elif self.thai_id_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the thai id')
        #     inner_popup.exec()
        #     return
        # elif self.phone_number_input_box.text() == '':
        #     inner_popup.change_label_to('Please fill in the phone number')
        #     inner_popup.exec()
        #     return
        # elif self.validate_birthday(self.new_text) != True:
        #     inner_popup.change_label_to(self.validate_birthday(self.new_text))
        #     inner_popup.exec()
        #     self.player_birthday_input_box.blockSignals(True)
        #     self.player_birthday_input_box.setText("")
        #     self.player_birthday_input_box.blockSignals(False)
        #     return
        # elif int(self.student_id_input_box.text()) < 10:
        #     inner_popup.change_label_to('Student ID must be 10 digits')
        #     inner_popup.exec()
        #     return
        # elif int(self.thai_id_input_box.text()) < 13:
        #     inner_popup.change_label_to('Thai ID must be 13 digits')
        #     inner_popup.exec()
        #     return
        # elif not self.validate_phone_number(self.phone_number_input_box.text()):
        #     inner_popup.change_label_to('Invalid phone number')
        #     inner_popup.exec()
        #     return

        self.accept()

    def get_information(self):
        return {
            'player_image_path': self.get_player_image_path(),
            'player_name': self.get_player_name(),
            'player_number': self.player_number_input_box.text(),
            'player_height': self.player_height_input_box.text(),
            'player_weight': self.player_weight_input_box.text(),
            'player_birthday': self.player_birthday_input_box.text(),
            'player_status': self.player_status_combobox.currentText(),
            'student_id': self.student_id_input_box.text(),
            'thai_id': self.thai_id_input_box.text(),
            'phone_number': self.phone_number_input_box.text()
        }

    def cleanup_player_add_image(self):
        if hasattr(self, 'player_add_image'):
            self.player_add_image_layout.removeWidget(self.player_add_image)
            self.player_add_image.hide()  # Hide before deletion
            self.player_add_image.deleteLater()
            delattr(self, 'player_add_image')  # Remove reference

        while self.player_add_image_layout.count():
            item = self.player_add_image_layout.takeAt(0)
            if item.widget():
                item.widget().hide()
                item.widget().deleteLater()

    def set_information(self, information):
        cleaned_path = information['player_image_path'].replace("'", "")
        information['player_image_path'] = cleaned_path

        self.cleanup_player_add_image()

        print('img path',information['player_image_path'])
        self.player_add_image = HoverButton(information['player_image_path'])
        self.player_add_image.setObjectName('player_add_image')
        self.player_add_image.setFixedSize(120, 140)
        # self.player_add_image.clicked.connect(self.add_image)
        self.player_add_image.disconnect()
        self.player_add_image_layout.addWidget(self.player_add_image)

        self.player_name_input_box.setText(information['player_name'])
        self.player_name_input_box.setEnabled(False)

        self.player_number_input_box.setText(information['player_number'])
        self.player_number_input_box.setEnabled(False)

        self.player_height_input_box.setText(information['player_height'])
        self.player_height_input_box.setEnabled(False)

        self.player_weight_input_box.setText(information['player_weight'])
        self.player_weight_input_box.setEnabled(False)

        self.player_birthday_input_box.setText(information['player_birthday'])
        self.player_birthday_input_box.setEnabled(False)

        self.player_status_combobox.setCurrentText(information['player_status'])
        self.player_status_combobox.setEnabled(False)

        self.student_id_input_box.setText(information['student_id'])
        self.student_id_input_box.setEnabled(False)

        self.thai_id_input_box.setText(information['thai_id'])
        self.thai_id_input_box.setEnabled(False)

        self.phone_number_input_box.setText(information['phone_number'])
        self.phone_number_input_box.setEnabled(False)


    def remove_player_image_button(self, button_name: str, layout_name: str):
        if hasattr(self, button_name) and getattr(self, button_name):
            target_layout = getattr(self, layout_name)
            target_button = getattr(self, button_name)
            index = target_layout.indexOf(target_button)
            target_layout.removeWidget(target_button)
            target_button.deleteLater()

            self.remove_spacing(target_layout, index)


    def remove_spacing(self, layout, index):
        item = layout.itemAt(index)
        if item is not None:
            layout.takeAt(index)
            if item.spacerItem() is not None:
                layout.removeItem(item.spacerItem())
            elif item.widget() is not None:
                item.widget().deleteLater()
            else:
                layout.removeItem(item)
            print(f'remove_spacing at index {index}')
        else:
            print('no item at index', index)



class AddPlayerOnlyOK(AddPlayer):
    def __init__(self, information=None):
        super().__init__(information)
        self.remove_cancel_button()

    def remove_cancel_button(self):
        if hasattr(self, 'player_add_image'):
            self.cancel_button_layout.removeWidget(self.cancel_button)
            self.cancel_button.hide()
            self.cancel_button.deleteLater()
            delattr(self, 'cancel_button')

            self.cancel_button_layout.setContentsMargins(0, 0, 0, 0)





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(490, 90, 700, 650)

        popup = AddPlayer()
        popup.move(425,33)
        result = popup.exec()
        if result:
            popup.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.close()
    sys.exit(app.exec())
