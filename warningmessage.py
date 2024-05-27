import sys # import system related variable such as closing
from PyQt6.QtWidgets import * #importing qtwidget related variable
class App(QWidget): # inheret qwidget
    def __init__(self):   # initilizing the constructor
        super().__init__()      # calling the parent constructor
        self.resize(500,300)  # setting the size
        self.setWindowTitle('PyGam') #setting the title
        button = QPushButton('Click me!',self) # adding the Push button
        button.setGeometry(180,120,100,50) # where the button should be placed
        button.clicked.connect(lambda :self.message()) # creating the event when the user press the button
        QMessageBox.information(self, 'Information', "This is a message")
        self.show() #
    def message(self):
        # message = QMessageBox(self)
        # mess = "You won't be able to see this message"
        # message.warning(self,"Warning",mess)
        QMessageBox.information(self,'Information',"This is a message")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = App()
    sys.exit(app.exec())