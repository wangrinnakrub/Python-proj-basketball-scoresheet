import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QTabWidget, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu and Tabs Example")

        # สร้างเมนูบาร์
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        help_menu = menubar.addMenu("Help")

        # สร้าง QTabWidget สำหรับแท็บ
        tab_widget = QTabWidget()

        # สร้างแท็บต่าง ๆ
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("This is tab 1"))
        tab1.setLayout(tab1_layout)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("This is tab 2"))
        tab2.setLayout(tab2_layout)

        # เพิ่มแท็บใน QTabWidget
        tab_widget.addTab(tab1, "Tab 1")
        tab_widget.addTab(tab2, "Tab 2")

        # ตั้งค่าตัววิดเจ็ตหลักของหน้าต่าง
        self.setCentralWidget(tab_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
