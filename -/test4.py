import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,  QMessageBox
from PyQt6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # สร้าง QAction สำหรับ 'New', 'Open', 'Save', 'Exit'
        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.setStatusTip('Create a new file')
        new_action.triggered.connect(self.newFile)

        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')
        open_action.setStatusTip('Open an existing file')
        open_action.triggered.connect(self.openFile)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save the current file')
        save_action.triggered.connect(self.saveFile)

        exit_action = QAction('Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(self.close)

        # สร้างเมนูบาร์
        menubar = self.menuBar()

        # สร้างเมนู 'File' และเพิ่มการกระทำเข้าไปในเมนู
        file_menu = menubar.addMenu('File')
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # สร้างเมนู 'Edit' (ตัวอย่างเพิ่มเติม)
        edit_menu = menubar.addMenu('Edit')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Paste')

        # ตั้งค่า window properties
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Menubar Example')
        self.show()

    def newFile(self):
        QMessageBox.information(self, 'Info', 'New file created')

    def openFile(self):
        QMessageBox.information(self, 'Info', 'Opened file')

    def saveFile(self):
        QMessageBox.information(self, 'Info', 'Saved file')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
