from PyQt6.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])

stacked_widget = QStackedWidget()
stacked_widget.setWindowTitle("QStackedWidget Example")

page1 = QWidget()
layout1 = QVBoxLayout()
layout1.addWidget(QLabel("Page 1"))
button1 = QPushButton("Go to Page 2")
layout1.addWidget(button1)
page1.setLayout(layout1)
# qwdqwdqwdadasd
page2 = QWidget()
layout2 = QVBoxLayout()
layout2.addWidget(QLabel("Page 2"))
button2 = QPushButton("Go to Page 1")
layout2.addWidget(button2)
page2.setLayout(layout2)

stacked_widget.addWidget(page1)
stacked_widget.addWidget(page2)

button1.clicked.connect(lambda: stacked_widget.setCurrentWidget(page2))
button2.clicked.connect(lambda: stacked_widget.setCurrentWidget(page1))

stacked_widget.show()
app.exec()
