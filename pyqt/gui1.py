import sys
from PyQt6.QtWidgets import QWidget,QApplication,QMessageBox,QLineEdit,QLabel,QGridLayout,QHBoxLayout,QVBoxLayout

from PyQt6.QtCore import Qt
class App1(QWidget):
    def __init__(self,name):
        super().__init__()
        self.message = QMessageBox(self)
        self.message.information(self,"Your Result",name)
        self.resize(500,300)
        grid1 = QVBoxLayout()
        self.setLayout(grid1)
        label = QLabel("Name: ",self)
        grid1.addWidget(label)


        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Enter Your Name")
        grid1.addWidget(self.input)

        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input.textChanged.connect(self.textChanged1)

        self.label2 = QLabel("",self)
        grid1.addWidget(self.label2)

        self.show()

    def textChanged(self,e):
        print(e)
    def textChanged1(self):
        value = self.input.text()
        self.label2.setText(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = App1("Meer")
    sys.exit(app.exec())
