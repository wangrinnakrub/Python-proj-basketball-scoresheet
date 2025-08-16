# from PyQt6.QtWidgets import QApplication, QToolBox, QLabel, QWidget, QVBoxLayout

# app = QApplication([])

# toolbox = QToolBox()
# toolbox.setWindowTitle("QToolBox Example")

# page1 = QWidget()
# layout1 = QVBoxLayout()
# layout1.addWidget(QLabel("Content in Page 1"))
# page1.setLayout(layout1)

# page2 = QWidget()
# layout2 = QVBoxLayout()
# layout2.addWidget(QLabel("Content in Page 2"))
# page2.setLayout(layout2)

# toolbox.addItem(page1, "Page 1")
# toolbox.addItem(page2, "Page 2")

# toolbox.show()
# app.exec()

from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Expandable Sidebar Example")
        self.setGeometry(300, 150, 800, 600)

        # Create the expandable sidebar
        sidebar = QToolBox()
        sidebar.setFixedWidth(200)

        # Page 1
        page1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QLabel("Content in Section 1"))
        page1.setLayout(layout1)

        # Page 2
        page2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QLabel("Content in Section 2"))
        page2.setLayout(layout2)

        # Add pages to the toolbox
        sidebar.addItem(page1, "Section 1")
        sidebar.addItem(page2, "Section 2")

        # Create a dock widget to hold the sidebar
        dock = QDockWidget("Sidebar", self)
        dock.setWidget(sidebar)
        dock.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)  # Fix it to the left
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        # Add the dock to the main window on the left
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

        # Main content area
        main_content = QLabel("Main Content Area")
        main_content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(main_content)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
