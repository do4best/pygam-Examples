import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget,QVBoxLayout,QLabel
from PyQt6.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color,name):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.name = QLabel(name,self)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.resize(500,500)
        layout = QVBoxLayout()
        layout.addWidget(Color('red',"Red"))
        layout.addWidget(Color('blue',"BLUE"))
        layout.addWidget(Color('green',"GREEN"))
        layout.addWidget(Color('yellow',"YELLOW"))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()