from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Radio_Button_Widget_Class import *
from birthdate_combo_box import *
from insert_record import *
import sys

class AdmissionTransWindow(QDialog):
    """Admission transport"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admission Transport")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Transport")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.label_trans = QLabel("Transport type:")

        self.add_trans = BirthDate(2)

        self.admission_grid = QGridLayout()
        self.admission_grid.addWidget(self.enter_button,2,0)
        self.admission_grid.addWidget(self.cancel_button,2,1)
        self.admission_grid.addWidget(self.label_trans,1,0)
        self.admission_grid.addWidget(self.add_trans,1,1)

        self.setLayout(self.admission_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()
        
    def add_data(self):
        data = str(self.add_trans.trans_combo.currentText())
        sql = "insert into AdmissionTrans (AdmissionTrans) values (?)"
        adding_trans = insert_data(data, sql)
        self.close()
