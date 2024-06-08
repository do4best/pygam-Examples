import sys
from PyQt6.QtWidgets import QApplication,QWidget,QTableWidget,QTableWidgetItem,QHeaderView,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt6.QtCore import Qt
import pandas as pd
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700,500)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.button = QPushButton("&Load Data")
        layout.addWidget(self.button)

    def loadExcelData(self,excel_file_dir,work_sheet_name):
        df = pd.read_excel(excel_file_dir,work_sheet_name)
        if df.size == 0:
            return


if __name__ == "__main__":

    excel_file_path = ''
    worksheet_name = ''
    app = QApplication(sys.argv)
    app.setStyleSheet('''
    QWidget{
    font-size:17px;
    }''')
    myapp = MyApp()
    myapp.show()
    sys.exit(app.exec())
