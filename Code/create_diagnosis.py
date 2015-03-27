from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Radio_Button_Widget_Class import *
from birthdate_combo_box import *
from insert_record import *
import sys, datetime

class DiagnosisWindow(QDialog):
    """Diagnosis layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diagnosis")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Diagnosis")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        self.label_dia_date = QLabel("Diagnosis Date:")
        self.label_dia_time = QLabel("Diagnosis Time:")

        self.date = date.today()
        self.date = self.date.strftime("{} {} {}".format("%d", "%m", "%Y"))
        self.add_dia_date = QLineEdit(str(self.date))
        self.time = datetime.datetime.now()
        self.time = self.time.strftime("{}:{}".format("%H", "%M"))
        self.add_dia_time = QLineEdit(str(self.time))
 
        self.dia_grid = QGridLayout()

        self.dia_grid.addWidget(self.enter_button,2,0)
        self.dia_grid.addWidget(self.cancel_button,2,1)
        self.dia_grid.addWidget(self.label_dia_date,0,0)
        self.dia_grid.addWidget(self.label_dia_time,1,0)

                
        self.dia_grid.addWidget(self.add_dia_date,0,1)
        self.dia_grid.addWidget(self.add_dia_time,1,1)
        self.setLayout(self.dia_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()
        
    def add_data(self):
        data = (self.add_dia_date.text(), self.add_dia_time.text())
        sql = "insert into Diagnosis (DiagnosisNoteDate, DiagnosisNoteTime) values (?,?)"
        adding_diagnosis = insert_data(data, sql)
        self.close()
