from PyQt6.QtWidgets import QApplication, QScrollArea, QLabel, QWidget, QVBoxLayout

app = QApplication([])

scroll_area = QScrollArea()
scroll_area.setWindowTitle("QScrollArea Example")

content_widget = QWidget()
layout = QVBoxLayout()

for i in range(20):
    layout.addWidget(QLabel(f"Label {i + 1}"))

content_widget.setLayout(layout)
scroll_area.setWidget(content_widget)

scroll_area.show()
app.exec()
