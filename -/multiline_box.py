from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiline Input Box")

        # Create a QTextEdit for multiline input
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Type your text here...")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        # Create a main widget
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the windowasdqwdasd
        self.setCentralWidget(container)


# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
