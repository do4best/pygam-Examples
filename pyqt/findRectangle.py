import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QGridLayout,QPushButton,QLineEdit
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,500)
        grid = QGridLayout()
        self.label1 = QLabel("Enter first Data",self)
        self.input1 = QLineEdit()
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.input1, 0, 1)
        self.input2 = QLineEdit()
        self.label2 = QLabel("Enter second Data", self)
        grid.addWidget(self.label2, 1, 1)
        grid.addWidget(self.input2, 1, 2)

        
        self.setLayout(grid)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyApp()
    window.show()

    app.exec()