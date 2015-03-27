from PyQt4.QtCore import *
from PyQt4.QtGui import *

from insert_record import *

import sys

class DoctorWindow(QDialog):
    """Doctor layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doctor")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Doctor")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.label_forename = QLabel("Forename:")
        self.label_surname = QLabel("Surname:")
        self.label_telwork = QLabel("Work Tel:")
        self.label_telhome = QLabel("Home tel:")
        self.label_email = QLabel("Email:")

        self.add_forename = QLineEdit()
        self.add_surname = QLineEdit()
        self.add_telwork = QLineEdit()
        self.add_telhome = QLineEdit()
        self.add_email = QLineEdit()

        self.doctor_grid = QGridLayout()

        self.doctor_grid.addWidget(self.enter_button,2,0)
        self.doctor_grid.addWidget(self.cancel_button,2,1)
        self.doctor_grid.addWidget(self.label_forename,0,0)
        self.doctor_grid.addWidget(self.label_surname,1,0)
        self.doctor_grid.addWidget(self.label_telwork,0,2)
        self.doctor_grid.addWidget(self.label_telhome,1,2)
        self.doctor_grid.addWidget(self.label_email,0,4)

        self.doctor_grid.addWidget(self.add_forename,0,1)
        self.doctor_grid.addWidget(self.add_surname,1,1)
        self.doctor_grid.addWidget(self.add_telwork,0,3)
        self.doctor_grid.addWidget(self.add_telhome,1,3)
        self.doctor_grid.addWidget(self.add_email,0,5)

        self.setLayout(self.doctor_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()

    def add_data(self):
        data = (self.add_forename.text(), self.add_surname.text(), self.add_telwork.text(), self.add_telhome.text(), self.add_email.text())
        sql = "insert into Doctor (DoctorForename, DoctorSurname, DoctorWorkTel, DoctorMobile, DoctorEmail) values (?,?,?,?,?)"
        adding_doctor = insert_data(data, sql)
        self.close()
