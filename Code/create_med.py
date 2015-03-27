from PyQt4.QtCore import *
from PyQt4.QtGui import *

from insert_record import *

import sys

class MedWindow(QDialog):
    """Med layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Med")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Med")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.label_med = QLabel("Med:")

        self.add_med = QLineEdit()

        self.med_grid = QGridLayout()

        self.med_grid.addWidget(self.enter_button,2,0)
        self.med_grid.addWidget(self.cancel_button,2,1)
        self.med_grid.addWidget(self.label_med,0,0)
        self.med_grid.addWidget(self.add_med,0,1)

        self.setLayout(self.med_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()

    def add_data(self):
        data = self.add_med.text()
        sql = "insert into Med (MedName) values (?)"
        adding_doctor_type = insert_data(data, sql)
        self.close()
