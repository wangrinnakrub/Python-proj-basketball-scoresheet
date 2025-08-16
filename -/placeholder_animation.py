# ในคลาส Signin_page

# *---------- ในฟังก์ชัน __init__ ---------- #
def __init__(self):
    super().__init__()
    self.setWindowTitle('Basketball Score Sheet - Sign In')
    self.setGeometry(360, 110, 700, 650)
    self.import_style('style_sign_in.qss')
    self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
    self.ui()

    # การตั้งค่าเพิ่มเติม
    self.username_input_box.setGraphicsEffect(QGraphicsOpacityEffect())
    self.password_input_box.setGraphicsEffect(QGraphicsOpacityEffect())

# *---------- สร้างฟังก์ชันโฟกัส ---------- #
def focusInEvent(self, event):
    if event.source() == self.username_input_box:
        self.username_input_box.setPlaceholderText('Username')
    elif event.source() == self.password_input_box:
        self.password_input_box.setPlaceholderText('Password')
    super().focusInEvent(event)

def focusOutEvent(self, event):
    if event.source() == self.username_input_box:
        self.username_input_box.setPlaceholderText('Type your username')
    elif event.source() == self.password_input_box:
        self.password_input_box.setPlaceholderText('Type your password')
    super().focusOutEvent(event)

# *---------- ปรับ QSS ---------- #
def import_style(self, file_name):
    try:
        with open(file_name, 'r') as file:
            style = file.read()
            # ตัวอย่างการปรับแต่ง QSS สำหรับ placeholder
            style += """
                QLineEdit {
                    padding-left: 10px;  /* ขยับข้อความไปทางซ้าย */
                    transition: padding 0.2s ease;  /* เพิ่มอนิเมชัน */
                }
                QLineEdit:focus {
                    padding-left: 30px;  /* ขยับ placeholder ไปทางขวาเมื่อโฟกัส */
                }
                QLineEdit::placeholder {
                    color: #999;  /* สี placeholder */
                }
            """
            self.setStyleSheet(style)
    except FileNotFoundError:
        print(f"Error: Cannot find the file '{file_name}'")
