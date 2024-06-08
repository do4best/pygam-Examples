import sys
from collections import  Counter
from PyQt6.QtWidgets import QWidget,QApplication,QLabel,QGridLayout,QMainWindow,QVBoxLayout

class myClass(QMainWindow):
    def __init__(self,name):
        super().__init__()
        layout = QVBoxLayout()
        self.widget = QWidget()

        self.label = QLabel(self)
        self.label.setText(name)
        layout.addWidget(self.label)
        self.widget.setLayout(layout)

        self.setCentralWidget(self.widget)
        self.show()

if __name__ == "__main__":
    names = [5,2,1,3,4]
    result = list(Counter(names).elements())

    app = QApplication(sys.argv)
    myapp = myClass(str(result))
    app.exec()
