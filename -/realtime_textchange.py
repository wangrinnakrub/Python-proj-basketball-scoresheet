# from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QCompleter
# from PyQt6.QtCore import QStringListModel

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QLineEdit with Suggestions")
#         self.resize(300, 100)

#         # สร้าง QCompleter และเติมค่าให้
#         completer = QCompleter()
#         completer.setModel(QStringListModel(["apple", "banana", "cherry", "date", "fig"]))

#         # สร้าง QLineEdit และเชื่อมต่อกับ QCompleter
#         self.line_edit = QLineEdit()
#         self.line_edit.setCompleter(completer)

#         layout = QVBoxLayout()
#         layout.addWidget(self.line_edit)
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = Window()
#     window.show()
#     app.exec()



from PyQt6.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit Real-time Check")
        self.resize(300, 100)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type here...")

        self.label = QLabel("Text will appear here...")

        # เชื่อมต่อ signal textChanged กับฟังก์ชัน update_label
        self.line_edit.textChanged.connect(self.update_label)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def update_label(self, text):
        self.label.setText(text)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

