import sys
from PyQt6.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLineEdit
from PyQt6.QtCore import Qt

class App2(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width,self.window_height=700,500
        self.resize(self.window_width,self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)
        lineEdits ={}
        lineEdits['NoEcho']= QLineEdit(self)
        lineEdits['NoEcho'].setPlaceholderText("No echo")
        lineEdits['NoEcho'].setEchoMode(QLineEdit.EchoMode.NoEcho)
        lineEdits['NoEcho'].textChanged.connect(self.printValue)
        lineEdits['Normal'] = QLineEdit(self)
        lineEdits['Password'] = QLineEdit(self)
        lineEdits['PasswordEchoOnEdit'] = QLineEdit(self)
        for _, item in lineEdits.items():
            layout.addWidget(item)

    def printValue(self,v):
        print(v)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    QWidget{
    font-size: 17px;}''')

    myApp = App2()
    myApp.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window")
