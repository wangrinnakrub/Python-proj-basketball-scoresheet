from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page 1"))
        self.setLayout(layout)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is Page 2"))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")  # Initial window titleqwdasdasdasd
        self.setGeometry(100, 100, 600, 400)

        # Create stacked widget to switch between pages
        self.stacked_widget = QStackedWidget()

        # Add pages to the stacked widget
        self.page1 = Page1()
        self.page2 = Page2()

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        self.setCentralWidget(self.stacked_widget)

        # Connect signal to slot to change window title when page changes
        self.stacked_widget.currentChanged.connect(self.change_window_title)

        # Initial window title
        self.change_window_title(0)  # Set the title based on the first page

    def change_window_title(self, index):
        # Change the window title based on the current page index
        if index == 0:
            self.setWindowTitle("Page 1 - Main Window")
        elif index == 1:
            self.setWindowTitle("Page 2 - Main Window")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_1:  # Press 1 to switch to Page 1
            self.stacked_widget.setCurrentIndex(0)
        elif event.key() == Qt.Key.Key_2:  # Press 2 to switch to Page 2
            self.stacked_widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
