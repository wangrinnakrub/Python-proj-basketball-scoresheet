from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class OtpInputBox(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaxLength(1)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Backspace:
            current_index = self.parentWidget().layout().itemAt(0).layout().indexOf(self)
            self.clear()  # ลบตัวเลขในช่องปัจจุบันทันที
            if current_index > 0:  # ถ้าไม่ใช่ช่องแรก ให้โฟกัสไปที่ช่องก่อนหน้า
                prev_widget = self.parentWidget().layout().itemAt(0).layout().itemAt(current_index - 1).widget()
                if isinstance(prev_widget, OtpInputBox):
                    prev_widget.setFocus()
                    prev_widget.deselect()  # เอาไฮไลท์ออก
                    prev_widget.setCursorPosition(len(prev_widget.text()))
        else:
            super().keyPressEvent(event)

class otp_check(QMainWindow):
    switch_to_forgot_password = pyqtSignal()
    switch_to_sign_in = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Verify OTP')
        self.setGeometry(360, 200, 700, 400)
        self.import_style('style_otp_check.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

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
        ui.addStretch()

    def on_text_changed(self):
        for i, box in enumerate(self.otp_input_boxes):
            if box.text() and i < len(self.otp_input_boxes) - 1:  # ถ้าช่องนี้ไม่ว่างและไม่ใช่ช่องสุดท้าย
                self.otp_input_boxes[i + 1].setFocus()
                self.otp_input_boxes[i + 1].deselect()

# ! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    Otp_check = otp_check()
    Otp_check.show()
    app.exec()
