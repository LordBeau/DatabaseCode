from PyQt4.QtCore import *
from PyQt4.QtGui import *

from insert_record import *

import sys

class DoctorTypeWindow(QDialog):
    """Doctor Type layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doctor Type")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Doc-Type")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.label_doc_type = QLabel("Doctor Type:")

        self.add_doc_type = QLineEdit()
        self.add_doc_type.setPlaceholderText("Paramedic")

        self.doctor_type_grid = QGridLayout()

        self.doctor_type_grid.addWidget(self.enter_button,2,0)
        self.doctor_type_grid.addWidget(self.cancel_button,2,1)
        self.doctor_type_grid.addWidget(self.label_doc_type,0,0)
        self.doctor_type_grid.addWidget(self.add_doc_type,0,1)

        self.setLayout(self.doctor_type_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()

    def add_data(self):
        data = self.add_doc_type.text()
        sql = "insert into DoctorType (DoctorType) values (?)"
        adding_doctor_type = insert_data(data, sql)
        self.close()
