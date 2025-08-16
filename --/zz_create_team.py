from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from zz_create_team_pop_up import *
import sys, sqlite3
from z_tournament_32 import *

class player_image_button(QPushButton):
    def __init__(self, file_name=None, information=None, button_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button_id = button_id
        print('\nbutton_id test in player image class : ',self.button_id)
        self.information = information
        self.setObjectName('player_add_image')

        if file_name == 'c:\pic\plus_icon.png':
            self.file_name = file_name
            self.file_name_hover = r'C:\pic\edit_label.png'
            self.setIcon(QIcon(self.file_name))
            self.setIconSize(QSize(127,127))
        else:
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\view_label.png'

            self.setContentsMargins(0, 0, 0, 0)
            self.setFixedSize(120,140)
            self.setIcon(QIcon())
            self.setStyleSheet(f"""
                    QPushButton#player_image_button {{
                        border: none;
                        border-radius: 20%;
                        background: transparent;
                        border-image: url({self.file_name});
                        margin: 0;
                        padding: 0;
                    }}
                    """)

        self.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Button clicked!")
        print(self.information)

        # ✅ ตรวจสอบให้ `self.information` มีข้อมูลครบ
        if self.information is None:
            self.information = {}

        for key in ["player_image_path", "player_name", "player_number", "player_height",
                    "player_weight", "player_birthday", "player_status", "student_id",
                    "thai_id", "phone_number"]:
            if key not in self.information:
                self.information[key] = ""  # ค่าเริ่มต้น

        self.edit_player_pop_up = AddPlayerOnlyOK(self.information)

        parent_window = self.window()
        parent_geometry = parent_window.geometry()
        parent_center = parent_geometry.center()

        popup_x = parent_center.x() - (self.edit_player_pop_up.width() // 2)
        popup_y = parent_center.y() - (self.edit_player_pop_up.height() // 2) - (self.edit_player_pop_up.height() // 25)
        self.edit_player_pop_up.move(popup_x, popup_y)

        #! run
        result = self.edit_player_pop_up.exec()

        if result:
            updated_info = self.edit_player_pop_up.get_information()
            self.information = updated_info
            self.edit_player_pop_up.set_information(self.information)
            print('ok')
            if self.information['player_image_path']:
                self.file_name = self.information['player_image_path']
                self.setStyleSheet(f"""
                        QPushButton#player_image_button {{
                            border: none;
                            border-radius: 20%;
                            background: transparent;
                            border-image: url({self.file_name});
                            margin: 0;
                            padding: 0;
                        }}
                        """)
                print("อัพเดทรูปภาพสำเร็จ")


    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            print("Left mouse button pressed!")
        super().mousePressEvent(event)

    def enterEvent(self, event):
        self.setStyleSheet('''
                            background-color: #1e1e1e;
                            border-radius: 20%;
                            border: 3px solid #1e1e1e;
                           ''')
        self.setIconSize(QSize(145,145))

        self.setIcon(QIcon(self.file_name_hover))
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.file_name == 'c:\pic\plus_icon.png':
            self.setIcon(QIcon(self.file_name))
            self.setIconSize(QSize(127,127))
            self.setStyleSheet("")
        else:
            self.setContentsMargins(0, 0, 0, 0)
            self.setFixedSize(120,140)
            self.setIcon(QIcon())
            self.setStyleSheet(f"""
                    QPushButton#player_image_button {{
                        border: none;
                        border-radius: 20%;
                        background: transparent;
                        border-image: url({self.file_name});
                        margin: 0;
                        padding: 0;
                    }}
                    """)
        super().leaveEvent(event)


class HoverButton(QPushButton):
    def __init__(self, file_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if file_name == 'c:\pic\plus_icon.png':
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\plus_icon_hover_white.png'
        else:
            self.file_name = file_name
            self.file_name_hover = r'c:\pic\change_image_label.png'

        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(127,127))

    def enterEvent(self, event):
        self.setStyleSheet("background-color: #d3d3d3;")
        self.setIcon(QIcon(self.file_name_hover))
        self.setIconSize(QSize(127,127))
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(QIcon(self.file_name))
        self.setIconSize(QSize(127,127))
        self.setStyleSheet("")
        super().leaveEvent(event)


class Create_team(QMainWindow):
    switch_to_match_setup = pyqtSignal()
    switch_to_tournament32 = pyqtSignal(int, str)
    switch_to_tournament32_normal = pyqtSignal()

    def __init__(self,team_id=None):
        super().__init__()
        self.setWindowTitle("Match Setup")
        self.setGeometry(100, 60, 1000, 750)
        self.setMinimumSize(850, 750)
        self.import_style('C:/Users/ASUS/OneDrive/Desktop/code/python/ED251007/project/style_z_create_team.qss')

        self.current_team_id = team_id
        print(f"🔍 กำลังสร้าง Create_team: team_id = {team_id}")


        self.team1_player_layout = QHBoxLayout()
        self.team1_player_layout2 = QHBoxLayout()  # 🛠️ เพิ่มการกำหนดค่า
        self.team1_player_layout3 = QHBoxLayout()

        self.layouts_created = {
            "team1_player_layout": False,
            "team1_player_layout2": False,
            "team1_player_layout3": False
        }
        self.player_buttons = []
        self.button_counter = 0

        self.current_layout = 0
        self.n = 0
        self.n_change = 0
        self.n2 = 0
        self.n_change2 = 0

        self.ui()

        self.installEventFilter(self)
        self.clear_focus_from_all()
        self.connection = sqlite3.connect(r'C:/Users/ASUS/OneDrive/Desktop/Dabest/basketball_score_sheet.db')
        self.cursor = self.connection.cursor()

    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [ self.team1_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.team1_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def ui(self):
        self.layout = QHBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def addWidgetsToLayout(self, ui):

        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_in')
        # self.back_button.clicked.connect(self.switch_to_tournament32_window)
        self.back_button.clicked.connect(self.switch_to_tournament32_normal.emit)
        ui.addWidget(self.back_button,alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)


        self.team1_layout = QVBoxLayout()

        self.team1_label = QLabel('Team name')
        self.team1_label.setObjectName('team1_label')
        self.team1_label.setFixedSize(245, 30)

        self.team1_label_layout = QHBoxLayout()
        self.team1_label_layout.addWidget(self.team1_label)

        self.team1_input_box = QLineEdit()
        self.team1_input_box.setPlaceholderText('Team name')
        self.team1_input_box.setObjectName('team1_input_box')
        self.team1_input_box.setFixedSize(200, 40)
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

                padding-left: 25px;
                color: #767676;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

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

            QLineEdit#team1_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
                color: #dedede;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')

        self.team1_input_box.textChanged.connect(self.team1_name_check_none)

        self.team1_input_box_layout = QHBoxLayout()
        self.team1_input_box_layout.addWidget(self.team1_input_box)

        self.team1_error_label = QLabel('')
        self.team1_error_label.setObjectName('team1_error_label')
        self.team1_error_label.setFixedSize(126, 30)
        self.team1_error_label.setStyleSheet('''
            QLabel#team1_error_label{

                color: #ff4343;

            }''')

        self.team1_error_label_layout = QHBoxLayout()
        self.team1_error_label_layout.addWidget(self.team1_error_label)

        self.team1_add_player_button = HoverButton('c:\pic\plus_icon.png')
        self.team1_add_player_button.setIcon(QIcon(r'c:\pic\plus_icon.png'))
        self.team1_add_player_button.setIconSize(QSize(127,127))
        self.team1_add_player_button.setObjectName('team1_add_player_button')
        self.team1_add_player_button.setFixedSize(120,140)
        self.team1_add_player_button.clicked.connect(self.team1_add_player)

        self.team1_add_player_button_layout = QVBoxLayout()
        self.team1_add_player_button_layout.addWidget(self.team1_add_player_button)

        self.team1_player_layout = QHBoxLayout()
        self.team1_player_layout.addStretch()
        self.team1_player_layout.addLayout(self.team1_add_player_button_layout)
        self.team1_player_layout.addStretch()
        self.layouts_created["team1_player_layout"] = True


        self.save_button = QPushButton('Save')
        self.save_button.setObjectName('save_button')
        self.save_button.setFixedSize(200, 40)
        self.save_button.clicked.connect(self.save)

        self.save_button_layout = QHBoxLayout()
        self.save_button_layout.addItem(QSpacerItem(self.width(), 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.save_button_layout.addWidget(self.save_button)
        self.save_button_layout.addItem(QSpacerItem(35, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))


        self.team1_layout.addLayout(self.team1_label_layout)
        self.team1_layout.addLayout(self.team1_input_box_layout)
        self.team1_layout.addLayout(self.team1_error_label_layout)
        self.team1_layout.addStretch(5)
        self.team1_layout.addLayout(self.team1_player_layout)
        self.team1_layout.addStretch(10)
        self.team1_layout.addLayout(self.save_button_layout)
        self.team1_layout.addStretch(1)

        ui.addStretch()
        ui.addLayout(self.team1_layout)
        ui.addStretch()

    def switch_to_tournament32_window(self):
        print(f"🔄 กำลังเปลี่ยนกลับไป tournament32: current_team_id = {self.current_team_id}")
        self.back_to_tournament_view_only()
        # self.switch_to_tournament32_normal.emit()
        # QTimer.singleShot(0, self.reset_create_team_page)

    def team1_name_check_none(self):
        self.team1_check_none = self.team1_input_box.text()
        if self.team1_check_none != '':
            self.team_name1_input_box_normal_border()
            self.team1_error_label.setText('')

    def team1_add_player(self):
        print('team1_add_player')
        print(f"\n🛠 ก่อนเพิ่มผู้เล่น current_team_id = {self.current_team_id}\n")


        self.team_name1 = self.team1_input_box.text()
        if self.team_name1 == '':
            self.team_name1_input_box_red_border()
            self.team1_error_label.setText('Please enter team name')
            return
        else: pass

        self.team_name1_input_box_normal_border()
        self.team1_error_label.setText('')

        self.add_player_pop_up = AddPlayer()

        parent_window = self.window()
        parent_geometry = parent_window.geometry()
        parent_center = parent_geometry.center()

        popup_x = parent_center.x() - (self.add_player_pop_up.width() // 2)
        popup_y = parent_center.y() - (self.add_player_pop_up.height() // 2) - (self.add_player_pop_up.height() // 25)
        self.add_player_pop_up.move(popup_x, popup_y)

        result = self.add_player_pop_up.exec()
        print(result)
        if result:
            print('ok')
            if self.n_change == 0:
                self.n += 1
                self.n_change += 1
            else:
                self.n += 2
                self.n_change += 1

            self.player_image_path = self.add_player_pop_up.get_player_image_path()
            self.information = self.add_player_pop_up.get_information()

            self.button_counter += 1
            print('button_counter : ',self.button_counter)
            button_name = f"player_image_button_{self.button_counter}"

            self.__dict__[button_name] = player_image_button(self.player_image_path,self.information,self.button_counter)
            self.__dict__[button_name].setObjectName('player_image_button')
            # button_id = self.__dict__[button_name].on_button_clicked()
            # self.__dict__[button_name].clicked.connect(self.on_button_clickedd(button_id))

            layout_name = f"player_image_button_layout_{self.button_counter}"
            self.__dict__[layout_name] = QVBoxLayout()

            self.player_buttons.append({
                'button_id': self.button_counter,
                'button': self.__dict__[button_name],
                'sub_layout': self.__dict__[layout_name]
            })

            self.__dict__[layout_name].addWidget(self.__dict__[button_name])

            print('current n : ', self.n)
            print('current_layout : ', self.current_layout)

            if self.current_layout == 0:
                self.team1_player_layout.insertLayout(self.n,self.__dict__[layout_name])
                self.team1_player_layout.insertSpacing(self.n + 1, 30)
                print('\ninsert spacing at layout 0\n')

                total_items = self.team1_player_layout.count()
                print(f"Total items in layout: {total_items}")
                for i in range(total_items):
                    item = self.team1_player_layout.itemAt(i)
                    print(f"Index {i}: {type(item).__name__}")

            if self.current_layout == 1:
                self.team1_player_layout2.insertLayout(self.n,self.__dict__[layout_name])
                self.team1_player_layout2.insertSpacing(self.n+1 , 30)
                print('\ninsert spacing at layout 1\n')

                total_items = self.team1_player_layout2.count()
                print(f"Total items in layout: {total_items}")
                for i in range(total_items):
                    item = self.team1_player_layout2.itemAt(i)
                    print(f"Index {i}: {type(item).__name__}")

            if self.current_layout == 2:
                self.team1_player_layout3.insertLayout(self.n,self.__dict__[layout_name])
                self.team1_player_layout3.insertSpacing(self.n+1 , 30)
                print('\ninsert spacing at layout 2\n')

                total_items = self.team1_player_layout3.count()
                print(f"Total items in layout: {total_items}")
                for i in range(total_items):
                    item = self.team1_player_layout3.itemAt(i)
                    print(f"Index {i}: {type(item).__name__}")


            #! remove button and create new layout
            if self.current_layout == 0:
                if self.n_change >= 4:
                    self.remove_team1_add_player_button('team1_add_player_button', 'team1_player_layout')

                    self.team1_player_layout2 = QHBoxLayout()
                    self.layouts_created["team1_player_layout2"] = True


                    self.team1_add_player_button2 = HoverButton('c:\pic\plus_icon.png')
                    self.team1_add_player_button2.setIcon(QIcon(r'c:\pic\plus_icon.png'))
                    self.team1_add_player_button2.setIconSize(QSize(127,127))
                    self.team1_add_player_button2.setObjectName('team1_add_player_button2')
                    self.team1_add_player_button2.setFixedSize(120,140)
                    self.team1_add_player_button2.clicked.connect(self.team1_add_player)

                    self.team1_add_player_button_layout2 = QVBoxLayout()
                    self.team1_add_player_button_layout2.addWidget(self.team1_add_player_button2)

                    self.team1_player_layout2 = QHBoxLayout()
                    self.team1_player_layout2.addStretch()
                    self.team1_player_layout2.addLayout(self.team1_add_player_button_layout2)
                    self.team1_player_layout2.addStretch()

                    self.team1_layout.insertStretch(5,1)
                    self.team1_layout.insertLayout(6,self.team1_player_layout2)
                    self.remove_spacing2(self.team1_player_layout, self.n+1, 30)
                    print(self.n)

                    self.n = 0
                    self.n_change = 0
                    self.current_layout = 1

            elif self.current_layout == 1:
                if self.n_change >= 4:
                    self.remove_team1_add_player_button('team1_add_player_button2', 'team1_player_layout2')

                    self.team1_player_layout3 = QHBoxLayout()
                    self.layouts_created["team1_player_layout3"] = True

                    self.team1_add_player_button3 = HoverButton('c:\pic\plus_icon.png')
                    self.team1_add_player_button3.setIcon(QIcon(r'c:\pic\plus_icon.png'))
                    self.team1_add_player_button3.setIconSize(QSize(127,127))
                    self.team1_add_player_button3.setObjectName('team1_add_player_button3')
                    self.team1_add_player_button3.setFixedSize(120,140)
                    self.team1_add_player_button3.clicked.connect(self.team1_add_player)

                    self.team1_add_player_button_layout3 = QVBoxLayout()
                    self.team1_add_player_button_layout3.addWidget(self.team1_add_player_button3)

                    self.team1_player_layout3 = QHBoxLayout()
                    self.team1_player_layout3.addStretch()
                    self.team1_player_layout3.addLayout(self.team1_add_player_button_layout3)
                    self.team1_player_layout3.addStretch()

                    self.team1_layout.insertStretch(7,1)
                    self.team1_layout.insertLayout(8,self.team1_player_layout3)
                    self.remove_spacing2(self.team1_player_layout2, self.n+1, 30)
                    print(self.n)

                    self.n = 0
                    self.n_change = 0
                    self.current_layout = 2

            elif self.current_layout == 2:
                if self.n_change >= 4:
                    self.remove_team1_add_player_button('team1_add_player_button3', 'team1_player_layout3')
                    self.remove_spacing2(self.team1_player_layout3, self.n+1, 30)
                    self.n = 0
                    self.n_change = 0
            print(f"✅ หลังเพิ่มผู้เล่น current_team_id = {self.current_team_id}")

        else:
            print('cancel')

    def remove_team1_add_player_button(self, button_name: str, layout_name: str):
        if hasattr(self, button_name) and getattr(self, button_name):
            target_layout = getattr(self, layout_name)
            target_button = getattr(self, button_name)
            index = target_layout.indexOf(target_button)
            target_layout.removeWidget(target_button)
            target_button.deleteLater()

            button_layout_name = f'{button_name}_layout'
            if hasattr(self, button_layout_name):
                target_layout.removeItem(getattr(self, button_layout_name))
                getattr(self, button_layout_name).deleteLater()
                print(f'{button_layout_name} deleted')

            print(f'index ของ {button_name} คือ {index}')
            self.remove_spacing(target_layout, index)
            print(f'{button_name} deleted')

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

    def remove_spacing2(self, layout, index, size):
        item = layout.takeAt(index)
        if item is not None:
            if isinstance(item, QSpacerItem):
                if item.sizeHint().width() == size or item.sizeHint().height() == size:
                    layout.removeItem(item)
                else:
                    layout.insertItem(index, item)
            else:
                layout.insertItem(index, item)
        print('remove_spacing2')

    def team_name1_input_box_red_border(self):
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

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
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

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

            QLineEdit#team1_input_box:focus{

                border-color: #ff7777;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
                color: #dedede;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')

    def team_name1_input_box_normal_border(self):
        self.team1_input_box.setStyleSheet('''
            QLineEdit#team1_input_box{

                padding-left: 25px;
                color: #767676;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;

            }
            QLineEdit#team1_input_box:hover,QLineEdit#team1_input_box:focus:hover{

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

            QLineEdit#team1_input_box:focus{

                border-color: #2a2a2a;

            }

            QLineEdit#team1_input_box::placeholder{

                padding-left: 25px;
                color: #dedede;
                background-color: transparent;
                border-top: transparent;
                border-bottom: 2px solid;
                border-left: transparent;
                border-right: transparent;
                border-color: #dcdcdc;
                font-family: TeX Gyre Adventor;
                font-weight: 620;
            }''')

    def save(self):
        self.team_name_insave = self.team1_input_box.text()

        if not hasattr(self, 'current_team_id'):
            print("❌ Error: current_team_id is not set!")
            return


        team_data = self.get_all_player_button_info_with_spacers()

        self.cursor.execute("UPDATE teams SET team_name = ? WHERE team_id = ?", (self.team_name_insave, self.current_team_id))
        self.cursor.execute("DELETE FROM players WHERE team_id = ?", (self.current_team_id,))

        for player in team_data["player_buttons"]:
            info = player["information"]

            for key in ["player_number", "player_height", "player_weight", "player_birthday",
                        "player_status", "student_id", "thai_id", "phone_number"]:
                if key not in info:
                    info[key] = ""

            self.cursor.execute('''
                INSERT INTO players (team_id, player_name, player_image_path, button_id, button_object_name,
                                    player_number, player_height, player_weight, player_birthday,
                                    player_status, student_id, thai_id, phone_number)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.current_team_id, info["player_name"], info["player_image_path"], player["button_id"],
                player["button_object_name"], info["player_number"], info["player_height"],
                info["player_weight"], info["player_birthday"], info["player_status"],
                info["student_id"], info["thai_id"], info["phone_number"]))

        self.connection.commit()

        self.switch_to_tournament32.emit(self.current_team_id, self.team_name_insave)
        # QTimer.singleShot(0, self.reset_create_team_page)

    def get_all_player_button_info_with_spacers(self):
        player_button_info = []
        for player in self.player_buttons:
            button = player['button']
            sub_layout = player['sub_layout']

            # ✅ ตรวจสอบว่า button_object_name มีค่าหรือไม่
            button_object_name = button.objectName()
            if not button_object_name:
                button_object_name = f"player_image_button_{button.button_id}"  # กำหนดค่าเริ่มต้น

            info = {
                'button_id': player['button_id'],
                'button_object_name': button_object_name,
                'information': button.information,
                'sub_layout': sub_layout,
            }
            player_button_info.append(info)

        return {
            'player_buttons': player_button_info
        }

    def clear_data(self):
        # เคลียร์ Widget เก่าทั้งหมดก่อนโหลดใหม่
        for player in self.player_buttons:
            player['button'].deleteLater()
        self.player_buttons.clear()

        # ลบ Layouts และรีเซ็ตค่า
        for layout_name, created in self.layouts_created.items():
            if created:
                layout = getattr(self, layout_name)
                while layout.count():
                    item = layout.takeAt(0)
                    if item.widget():
                        item.widget().deleteLater()
                    elif item.layout():
                        self.clear_layout(item.layout())
                setattr(self, layout_name, QHBoxLayout())  # สร้างใหม่
                self.layouts_created[layout_name] = False

        # รีเซ็ตตัวแปรตัวนับ
        self.button_counter = 0
        self.n = self.n_change = 0
        self.n2 = self.n_change2 = 0
        self.current_layout = 0

    def load_team_data(self, team_name, team_id):
        self.save_button.hide()

        # ปรับการทำงานของปุ่ม Back
        self.back_button.clicked.disconnect()
        self.back_button.clicked.connect(self.back_to_tournament_view_only)


        self.team1_input_box.setText(team_name)
        self.team1_input_box.setReadOnly(True)

        if team_id is None:
            print("❌ Error: team_id is None!")
        else:
            self.current_team_id = team_id  # ✅ ตั้งค่า current_team_id
            print('team_id ใน load_team_data : ',team_id)
            print(f"✅ current_team_id ถูกตั้งค่าเป็น {self.current_team_id}")

        self.team1_input_box.setText(team_name)

        self.cursor.execute("SELECT player_name, player_image_path, button_id, player_number, player_height, player_weight, player_birthday, player_status, student_id, thai_id, phone_number FROM players WHERE team_id = ?", (team_id,))
        players = self.cursor.fetchall()

        for player in players:
            player_info = {
                'player_name': player[0],
                'player_image_path': player[1],
                'player_number': player[3],
                'player_height': player[4],
                'player_weight': player[5],
                'player_birthday': player[6],
                'player_status': player[7],
                'student_id': player[8],
                'thai_id': player[9],
                'phone_number': player[10],
            }
            self.add_player_button(player_info, player[1])
            print(f"\nเพิ่มผู้เล่น {player_info['player_name']} สำเร็จ (Button ID: {player[2]})\n")

        print(f"โหลดข้อมูลทีม {team_name} สำเร็จ (Team ID: {team_id})")

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                elif item.layout():
                    self.clear_layout(item.layout())  # เรียกใช้ตัวเองเพื่อลบ nested layouts

    def reset_create_team_page(self):
        print("Resetting create_team page...")

        # ✅ ลบปุ่ม team1_add_player_button ถ้ามีอยู่
        if hasattr(self, "team1_add_player_button") and self.team1_add_player_button is not None:
            try:
                self.team1_player_layout.removeWidget(self.team1_add_player_button)
                self.team1_add_player_button.deleteLater()
                self.team1_add_player_button = None
                print("Deleted team1_add_player_button")
            except RuntimeError:
                print("team1_add_player_button already deleted")

        # ✅ ลบปุ่ม save_button ถ้ามีอยู่
        if hasattr(self, "save_button") and self.save_button is not None:
            try:
                self.save_button_layout.removeWidget(self.save_button)
                self.save_button.deleteLater()
                self.save_button = None
                print("Deleted save_button")
            except RuntimeError:
                print("save_button already deleted")

        # ✅ ลบ Spacer ทั้งหมดใน layout
        for i in reversed(range(self.team1_player_layout.count())):
            item = self.team1_player_layout.itemAt(i)
            if isinstance(item, QSpacerItem):
                self.team1_player_layout.removeItem(item)
                print("Removed a spacer")

        print("Reset completed successfully.")


        self.layouts_created = {
            "team1_player_layout": False,
            "team1_player_layout2": False,
            "team1_player_layout3": False
        }

        self.button_counter = 0

        print("Create Team Page Reset Complete!")

    def add_player_button(self, player_info, player_image_path):
        print('add_player_button')

        self.button_counter += 1
        print('button_counter:', self.button_counter)

        # สร้างปุ่ม player
        button_name = f"player_image_button_{self.button_counter}"
        self.__dict__[button_name] = player_image_button(player_image_path, player_info, self.button_counter)
        self.__dict__[button_name].setObjectName('player_image_button')
        # self.__dict__[button_name].setEnabled(False)

        # สร้าง layout สำหรับปุ่ม
        layout_name = f"player_image_button_layout_{self.button_counter}"
        self.__dict__[layout_name] = QVBoxLayout()
        self.__dict__[layout_name].addWidget(self.__dict__[button_name])

        self.player_buttons.append({
            'button_id': self.button_counter,
            'button': self.__dict__[button_name],
            'sub_layout': self.__dict__[layout_name]
        })

        # คำนวณตำแหน่งที่ต้องเพิ่ม
        if self.n_change == 0:
            self.n += 1
        else:
            self.n += 2
        self.n_change += 1

        print('current n:', self.n)
        print('current_layout:', self.current_layout)

        # เพิ่มปุ่มไปยัง layout ปัจจุบัน
        target_layout = None
        if self.current_layout == 0:
            target_layout = self.team1_player_layout
        elif self.current_layout == 1:
            target_layout = self.team1_player_layout2
        elif self.current_layout == 2:
            target_layout = self.team1_player_layout3

        if target_layout:
            target_layout.insertLayout(self.n, self.__dict__[layout_name])
            target_layout.insertSpacing(self.n + 1, 30)

        # ถ้าปุ่มครบ 4 อัน ต้องเปลี่ยน layout
        if self.n_change >= 4:
            if self.current_layout == 0:
                self.remove_team1_add_player_button('team1_add_player_button', 'team1_player_layout')

                self.team1_player_layout2 = QHBoxLayout()
                self.team1_add_player_button2 = HoverButton('c:\pic\plus_icon.png')
                self.team1_add_player_button2.setIcon(QIcon(r'c:\pic\plus_icon.png'))
                self.team1_add_player_button2.setIconSize(QSize(127,127))
                self.team1_add_player_button2.setObjectName('team1_add_player_button2')
                self.team1_add_player_button2.setFixedSize(120,140)
                self.team1_add_player_button2.clicked.connect(self.team1_add_player)

                self.team1_add_player_button_layout2 = QVBoxLayout()
                self.team1_add_player_button_layout2.addWidget(self.team1_add_player_button2)

                self.team1_player_layout2.addStretch()
                self.team1_player_layout2.addLayout(self.team1_add_player_button_layout2)
                self.team1_player_layout2.addStretch()

                self.team1_layout.insertStretch(5, 1)
                self.team1_layout.insertLayout(6, self.team1_player_layout2)
                self.remove_spacing2(self.team1_player_layout, self.n + 1, 30)

                self.n = 0
                self.n_change = 0
                self.current_layout = 1

            elif self.current_layout == 1:
                self.remove_team1_add_player_button('team1_add_player_button2', 'team1_player_layout2')

                self.team1_player_layout3 = QHBoxLayout()
                self.team1_add_player_button3 = HoverButton('c:\pic\plus_icon.png')
                self.team1_add_player_button3.setIcon(QIcon(r'c:\pic\plus_icon.png'))
                self.team1_add_player_button3.setIconSize(QSize(127,127))
                self.team1_add_player_button3.setObjectName('team1_add_player_button3')
                self.team1_add_player_button3.setFixedSize(120,140)
                self.team1_add_player_button3.clicked.connect(self.team1_add_player)

                self.team1_add_player_button_layout3 = QVBoxLayout()
                self.team1_add_player_button_layout3.addWidget(self.team1_add_player_button3)

                self.team1_player_layout3.addStretch()
                self.team1_player_layout3.addLayout(self.team1_add_player_button_layout3)
                self.team1_player_layout3.addStretch()

                self.team1_layout.insertStretch(7, 1)
                self.team1_layout.insertLayout(8, self.team1_player_layout3)
                self.remove_spacing2(self.team1_player_layout2, self.n + 1, 30)

                self.n = 0
                self.n_change = 0
                self.current_layout = 2

            elif self.current_layout == 2:
                # ✅ ตรวจสอบว่าปุ่มยังอยู่ก่อนลบ
                # if hasattr(self, 'team1_add_player_button3') and isinstance(self.team1_add_player_button3, HoverButton):
                #     try:
                #         if self.team1_add_player_button3.parent() is not None:
                #             if self.team1_player_layout3.indexOf(self.team1_add_player_button3) >= 0:
                self.remove_team1_add_player_button('team1_add_player_button3', 'team1_player_layout3')
                #             else:
                #                 print("⚠️ Warning: team1_add_player_button3 ไม่อยู่ใน layout แล้ว")
                #         else:
                #             print("⚠️ Warning: team1_add_player_button3 ถูกลบจาก parent แล้ว")
                #     except RuntimeError:
                #         print("⚠️ Warning: team1_add_player_button3 ถูกลบไปแล้ว (RuntimeError)")
                #         self.team1_add_player_button3 = None
                # else:
                #     print("⚠️ Warning: team1_add_player_button3 ไม่มีอยู่แล้ว")


                self.remove_spacing2(self.team1_player_layout3, self.n + 1, 30)
                self.n = 0
                self.n_change = 0

    def back_to_tournament_view_only(self):
        self.switch_to_tournament32_normal.emit()

    def prepare_for_team_creation(self):
        self.save_button.show()
        # self.back_button.clicked.disconnect()
        # self.back_button.clicked.connect(self.switch_to_tournament32_window)

    def prepare_for_team_view(self):
        self.save_button.hide()
        # self.back_button.clicked.disconnect()
        # self.back_button.clicked.connect(self.back_to_tournament_view_only)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Create_team()
    window.show()
    sys.exit(app.exec())
