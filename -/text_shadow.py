# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# from PyQt6.QtGui import QColor
# from PyQt6.QtWidgets import QGraphicsDropShadowEffect

# class ShadowWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Text Shadow Example')
#         self.setGeometry(100, 100, 800, 600)

#         self.label = QLabel('Hello, World!')
#         self.label.setStyleSheet('font-size: 24px;')

#         # สร้าง QGraphicsDropShadowEffect
#         shadow_effect = QGraphicsDropShadowEffect()
#         shadow_effect.setBlurRadius(20)
#         shadow_effect.setXOffset(0)
#         shadow_effect.setYOffset(0)
#         shadow_effect.setColor(QColor(0, 0, 0, 240))

#         # เพิ่มเงาให้กับ QLabel
#         self.label.setGraphicsEffect(shadow_effect)

#         self.setup_ui()

#     def setup_ui(self):
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.label)

#         main_widget = QWidget()
#         main_widget.setLayout(self.layout)
#         self.setCentralWidget(main_widget)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = ShadowWindow()
#     window.show()
#     app.exec()


from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

class ShadowWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Text Shadow Example')
        self.setGeometry(100, 100, 800, 600)

        self.sign_in_label = QLabel('Sign In')
        self.sign_in_label.setObjectName('sign_in_label')
        self.sign_in_label.setFixedHeight(100)

        # สร้าง QGraphicsDropShadowEffect
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(20)
        shadow_effect.setXOffset(0)
        shadow_effect.setYOffset(0)
        shadow_effect.setColor(QColor(0, 0, 0, 240))

        # เพิ่มเงาให้กับ QLabel
        self.sign_in_label.setGraphicsEffect(shadow_effect)

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()
        main_layout.addStretch()
        main_layout.addWidget(self.sign_in_label)
        main_layout.addStretch()

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = ShadowWindow()
    window.show()
    app.exec()
