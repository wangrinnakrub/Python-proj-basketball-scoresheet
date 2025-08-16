from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys, sqlite3


class CustomMenu(QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255)))
        painter.setPen(Qt.PenStyle.NoPen)

        # Draw drop shape
        path = QPainterPath()
        path.moveTo(self.width() / 2, 10)
        path.quadTo(self.width(), 10, self.width(), self.height() - 10)
        path.quadTo(self.width(), self.height(), self.width() / 2, self.height())
        path.quadTo(0, self.height(), 0, self.height() - 10)
        path.quadTo(0, 10, self.width() / 2, 10)
        painter.drawPath(path)

        super().paintEvent(event)

class Main_window(QMainWindow):
    switch_to_tournament_32 = pyqtSignal()
    switch_to_sign_in = pyqtSignal()
    switch_to_history = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 60, 1000, 700)
        self.setMinimumSize(766, 600)
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_z_main_window.qss')
        self.ui()

        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.sidebar_visible = False
        self.previous_mouse_position = QPoint()

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

        self.sidebar = QFrame(self)
        self.sidebar.setGeometry(self.width(), 0, 360, self.height())
        self.sidebar.setObjectName('sidebar')

        self.sidebar_layout = QVBoxLayout()
        self.sidebar.setLayout(self.sidebar_layout)

        self.contact_us_widget = QWidget(self.sidebar)
        self.contact_us_widget.setObjectName('contact_us_widget')
        self.contact_us_widget_layout = QVBoxLayout(self.contact_us_widget)

        self.contact_us_button = QPushButton('Contact Us')
        self.contact_us_button.setFixedSize(110, 45)
        self.contact_us_button.setObjectName('contact_us_button')
        self.contact_us_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.contact_us_button.clicked.connect(self.toggle_contact_us_details)

        self.contact_us_button_layout = QHBoxLayout()
        self.contact_us_button_layout.addSpacerItem(QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.contact_us_button_layout.addWidget(self.contact_us_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.contact_us_widget_layout.addLayout(self.contact_us_button_layout)

        self.contact_us_details = QWidget(self.sidebar)
        self.contact_us_details.setObjectName('contact_us_details')
        self.contact_us_details_layout = QVBoxLayout(self.contact_us_details)
        self.contact_us_details.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.contact_us_details.setMinimumHeight(0)
        self.contact_us_details.setMaximumHeight(0)

        self.contact_us_details_h_layout = QHBoxLayout()
        self.contact_us_details_layout.addLayout(self.contact_us_details_h_layout)

        self.contact_details_icon_label = QLabel()
        self.contact_details_icon_label.setPixmap(QPixmap(r"C:\pic\mail.png"))
        self.contact_details_icon_label.setFixedSize(30, 30)
        self.contact_details_icon_label.setScaledContents(True)
        self.contact_details_icon_label.setObjectName('contact_details_icon_label')

        self.contact_details_label = QLabel("basketballscoresheet.official@gmail.com")
        self.contact_details_label.setFixedHeight(30)
        self.contact_details_label.setObjectName('contact_details_label')

        self.contact_us_details_h_layout.addSpacerItem(QSpacerItem(8, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.contact_us_details_h_layout.addWidget(self.contact_details_icon_label)
        self.contact_us_details_h_layout.addSpacerItem(QSpacerItem(4, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.contact_us_details_h_layout.addWidget(self.contact_details_label)


        # About Us Details
        self.about_us_widget = QWidget(self.sidebar)
        self.about_us_widget.setObjectName('about_us_widget')
        self.about_us_widget_layout = QVBoxLayout(self.about_us_widget)

        self.about_us_button = QPushButton('About Us')
        self.about_us_button.setFixedSize(110, 45)
        self.about_us_button.setObjectName('about_us_button')
        self.about_us_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.about_us_button.clicked.connect(self.toggle_about_us_details)

        self.about_us_button_layout = QHBoxLayout()
        self.about_us_button_layout.addSpacerItem(QSpacerItem(13, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.about_us_button_layout.addWidget(self.about_us_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.about_us_widget_layout.addLayout(self.about_us_button_layout)

        self.about_us_details = QWidget(self.sidebar)
        self.about_us_details_layout = QVBoxLayout(self.about_us_details)
        self.about_us_details.setObjectName('about_us_details')

        self.about_us_details_h_layout_1 = QHBoxLayout()
        self.about_us_details_h_layout_1.setObjectName('about_us_details_h_layout_1')
        self.about_us_details_h_layout_1.setSpacing(0)

        self.navy_photo_label = QLabel()
        self.navy_photo_label.setPixmap(QPixmap(r'C:\pic\navy.png'))
        self.navy_photo_label.setFixedSize(150, 180)
        self.navy_photo_label.setScaledContents(True)
        self.navy_photo_label.setObjectName('navy_photo_label')
        self.about_us_details_h_layout_1.addWidget(self.navy_photo_label)

        self.navy_label = QLabel()
        self.navy_label.setText('<p>Kantaphit Somnueknaitham<br>663050375-9')
        self.navy_label.setObjectName('navy_label')
        self.navy_label.setFixedSize(160, 180)
        self.about_us_details_h_layout_1.addWidget(self.navy_label)

        self.about_us_details_h_layout_2 = QHBoxLayout()
        self.about_us_details_h_layout_2.setObjectName('about_us_details_h_layout_2')
        self.about_us_details_h_layout_2.setSpacing(0)

        self.pun_photo_label = QLabel()
        self.pun_photo_label.setPixmap(QPixmap(r'C:\pic\pun.png'))
        self.pun_photo_label.setFixedSize(160, 200)
        self.pun_photo_label.setScaledContents(True)
        self.pun_photo_label.setObjectName('pun_photo_label')

        self.pun_label = QLabel()
        self.pun_label.setText('<p>Piyawat Yongdee<br>663050387-2')
        self.pun_label.setObjectName('pun_label')
        self.pun_label.setFixedSize(150, 200)
        self.about_us_details_h_layout_2.addWidget(self.pun_photo_label)
        self.about_us_details_h_layout_2.addWidget(self.pun_label)

        self.about_us_details_layout.addLayout(self.about_us_details_h_layout_1)
        self.about_us_details_layout.addSpacerItem(QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.about_us_details_layout.addLayout(self.about_us_details_h_layout_2)

        self.about_us_details.setMinimumHeight(0)
        self.about_us_details.setMaximumHeight(0)

        self.sidebar_layout.addWidget(self.contact_us_widget)
        self.sidebar_layout.addWidget(self.contact_us_details)
        self.sidebar_layout.addWidget(self.about_us_widget)
        self.sidebar_layout.addWidget(self.about_us_details)
        self.sidebar_layout.addStretch()


    def addWidgetsToLayout(self, ui):
        self.user_image_label = QLabel(self)

        self.user_icon = QPushButton()
        self.user_icon.setObjectName('user_icon')
        self.user_icon.setCursor(Qt.CursorShape.PointingHandCursor)
        self.user_icon.setFixedSize(40, 40)
        self.user_icon.setIcon(QIcon(r"C:\pic\user_iconnn.png"))
        self.user_icon.setIconSize(QSize(40, 40))
        self.user_icon.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.user_icon.clicked.connect(self.show_user_menu)

        self.user_menu = QMenu()
        self.user_menu.setObjectName('user_menu')
        self.user_menu.setStyleSheet("""
            QMenu {
                font-family: Tex Gyre Adventor;
                font-weight: 900;
                background-color: #484742;
                color: #f3f3f3;
                border: 3px solid #484742;
                border-radius: 5px !important;
            }
            QMenu::item {
                font-family: Tex Gyre Adventor;
                font-weight: 900;
                padding: 5px 20px;
                background-color: #484742;
                border:none;
                letter-spacing: 1px;
            }
            QMenu::item:selected {
                font-family: Tex Gyre Adventor;
                font-weight: 900;
                background-color: #f3f3f3;
                color: #484742;
                border:none;
                letter-spacing: 1px;

            }
        """)

        # self.profile_action = QAction('Profile', self)
        # self.profile_action.setObjectName('profile_action')
        self.history_action = QAction('History', self)
        self.history_action.setObjectName('history_action')
        self.logout_action = QAction('Logout', self)
        self.logout_action.setObjectName('logout_action')

        # self.user_menu.addAction(self.profile_action)
        self.user_menu.addAction(self.history_action)
        self.user_menu.addAction(self.logout_action)

        # self.profile_action.triggered.connect(self.show_profile)
        self.history_action.triggered.connect(self.show_history)
        self.logout_action.triggered.connect(self.logout)

        self.user_icon.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.user_icon.customContextMenuRequested.connect(self.show_user_menu)

        self.username_label = QLabel('usernameusernameusernamewsdefr')
        self.username_label.setObjectName('username_label')

        self.sidebar_button = QPushButton()
        self.sidebar_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.sidebar_button.setFixedSize(28, 28)
        self.sidebar_button.setObjectName('sidebar_button')
        self.sidebar_button.setIcon(QIcon(r"C:\pic\about_iconn.png"))
        self.sidebar_button.setIconSize(QSize(28, 28))
        self.sidebar_button.clicked.connect(self.toggle_sidebar)

        self.user_image_label_layout = QHBoxLayout()
        self.user_image_label_layout.addSpacerItem(QSpacerItem(15, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.user_image_label_layout.addWidget(self.user_icon)
        self.user_image_label_layout.addSpacerItem(QSpacerItem(0, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.user_image_label_layout.addWidget(self.username_label)
        self.user_image_label_layout.addWidget(self.sidebar_button)
        self.user_image_label_layout.addSpacerItem(QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))

        self.set_up_match_button = QPushButton('Tournament')
        self.set_up_match_button.setObjectName('set_up_match_button')
        self.set_up_match_button.setFixedSize(359, 173)
        self.set_up_match_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.set_up_match_button.clicked.connect(self.switch_to_tournament_32.emit)

        self.set_up_match_button_layout = QHBoxLayout()
        self.set_up_match_button_layout.addWidget(self.set_up_match_button)

        ui.addSpacerItem(QSpacerItem(0, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        ui.addLayout(self.user_image_label_layout)
        ui.addStretch(1)
        ui.addLayout(self.set_up_match_button_layout)
        ui.addStretch(2)

    def show_user_menu(self, pos):
        cursor_pos = self.user_icon.mapToGlobal(QPoint(self.user_icon.width()-37, self.user_icon.height()+12))
        self.user_menu.exec(cursor_pos)

    def show_profile(self):
        print('Profile')

    def show_history(self):
        print('history')
        self.switch_to_history.emit()

    def logout(self):
        self.switch_to_sign_in.emit()

    def fetch_username(self, username_or_email):
        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT * FROM user_account WHERE username = ? or email = ?", (username_or_email,username_or_email))
        self.existing_user = self.cursor.fetchone()

        if self.existing_user:
            self.username_label.setText(str(self.existing_user[1]))
            self.username = str(self.existing_user[1])

    def fetched_username(self):
        return self.username

    def toggle_sidebar(self):
        self.animation = QPropertyAnimation(self.sidebar, b"pos")
        self.animation.setDuration(360)
        self.animation.setEasingCurve(QEasingCurve.Type.InOutCirc)

        self.button_animation = QPropertyAnimation(self.set_up_match_button, b"pos")
        self.button_animation.setDuration(360)
        self.button_animation.setEasingCurve(QEasingCurve.Type.InOutCirc)

        y = self.width() - 360
        yLR = (y - self.set_up_match_button.width()) // 2

        if self.sidebar_visible:
            self.animation.setStartValue(self.sidebar.pos())
            self.animation.setEndValue(QPoint(self.width(), 0))

            self.button_animation.setStartValue(self.set_up_match_button.pos())
            self.button_animation.setEndValue(QPoint((self.width() - self.set_up_match_button.width()) // 2, self.set_up_match_button.y()))
        else:
            self.sidebar.setGeometry(self.width(), 0, 360, self.height())
            self.animation.setStartValue(QPoint(self.width(), 0))
            self.animation.setEndValue(QPoint(self.width() - 360, 0))

            self.button_animation.setStartValue(self.set_up_match_button.pos())
            self.button_animation.setEndValue(QPoint(yLR, self.set_up_match_button.y()))

            self.contact_us_details.setMinimumHeight(0)
            self.contact_us_details.setMaximumHeight(0)

            self.about_us_details.setMinimumHeight(0)
            self.about_us_details.setMaximumHeight(0)

        self.animation.start()
        self.button_animation.start()
        self.sidebar_visible = not self.sidebar_visible

    def toggle_contact_us_details(self):
        if self.about_us_details.height() != 0:
            self.animation3 = QPropertyAnimation(self.about_us_details, b"maximumHeight")
            self.animation3.setDuration(360)
            self.animation3.setStartValue(self.about_us_details.height())
            self.animation3.setEndValue(0)
            self.animation3.start()

        if self.contact_us_details.height() == 0:
            self.animation2 = QPropertyAnimation(self.contact_us_details, b"maximumHeight")
            self.animation2.setEasingCurve(QEasingCurve.Type.InOutCirc)
            self.animation2.setDuration(360)
            self.animation2.setStartValue(0)
            self.animation2.setEndValue(200)
            self.animation2.start()
        else:
            self.animation2 = QPropertyAnimation(self.contact_us_details, b"maximumHeight")
            self.animation2.setDuration(360)
            self.animation2.setStartValue(self.contact_us_details.height())
            self.animation2.setEndValue(0)
            self.animation2.start()

    def toggle_about_us_details(self):
        if self.contact_us_details.height() != 0:
            self.animation2 = QPropertyAnimation(self.contact_us_details, b"maximumHeight")
            self.animation2.setDuration(360)
            self.animation2.setStartValue(self.contact_us_details.height())
            self.animation2.setEndValue(0)
            self.animation2.start()

        if self.about_us_details.height() == 0:
            self.animation3 = QPropertyAnimation(self.about_us_details, b"maximumHeight")
            self.animation3.setEasingCurve(QEasingCurve.Type.InOutCirc)
            self.animation3.setDuration(360)
            self.animation3.setStartValue(0)
            self.animation3.setEndValue(500)
            self.animation3.start()
        else:
            self.animation3 = QPropertyAnimation(self.about_us_details, b"maximumHeight")
            self.animation3.setDuration(360)
            self.animation3.setStartValue(self.about_us_details.height())
            self.animation3.setEndValue(0)
            self.animation3.start()

    def resizeEvent(self, event):
        if not self.sidebar_visible:
            self.sidebar.setGeometry(self.width(), 0, 360, self.height())
        else:
            self.sidebar.setGeometry(self.width() - 360, 0, 360, self.height())
        if self.sidebar_visible:
            y = self.width() - 360
            yLR = (y - self.set_up_match_button.width()) // 2
            self.set_up_match_button.move(QPoint(yLR, self.set_up_match_button.y()))
        super().resizeEvent(event)

    def mousePressEvent(self, event):
        if self.sidebar_visible:
            if not self.sidebar.geometry().contains(event.pos()):
                self.toggle_sidebar()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.pos().x() < self.previous_mouse_position.x():
            if not self.sidebar_visible:
                self.toggle_sidebar()
        self.previous_mouse_position = event.pos()
        super().mouseMoveEvent(event)

    def wheelEvent(self, event):
        if event.angleDelta().x() < 0:
            if not self.sidebar_visible:
                self.toggle_sidebar()
        elif event.angleDelta().x() > 0:
            if self.sidebar_visible:
                self.toggle_sidebar()
        super().wheelEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec())
