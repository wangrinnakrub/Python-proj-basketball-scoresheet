import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel

class DropdownExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dropdown Box Example")
        self.setGeometry(100, 100, 300, 150)

        # สร้างเลย์เอาท์
        layout = QVBoxLayout()

        # สร้าง QLabel สำหรับแสดงค่าที่เลือก
        self.label = QLabel("กรุณาเลือกตัวเลือก", self)

        # สร้าง QComboBox (Dropdown Box)
        self.comboBox = QComboBox()
        self.comboBox.addItems(["ตัวเลือกที่ 1", "ตัวเลือกที่ 2", "ตัวเลือกที่ 3"])

        # เชื่อมสัญญาณการเลือกไปยังฟังก์ชัน
        self.comboBox.currentTextChanged.connect(self.update_label)

        # เพิ่มวิดเจ็ตลงในเลย์เอาท์
        layout.addWidget(self.comboBox)
        layout.addWidget(self.label)

        # ตั้งค่าเลย์เอาท์ให้หน้าต่างหลัก
        self.setLayout(layout)

    # ฟังก์ชันสำหรับอัปเดตข้อความเมื่อมีการเลือกค่า
    def update_label(self, text):
        self.label.setText(f"คุณเลือก: {text}")

# เรียกใช้งานแอปพลิเคชัน
app = QApplication(sys.argv)
window = DropdownExample()
window.show()
sys.exit(app.exec())
