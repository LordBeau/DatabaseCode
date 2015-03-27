from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Radio_Button_Widget_Class import *
from birthdate_combo_box import *
from insert_record import *
import sys, datetime

class TreatmentsWindow(QDialog):
    """Treatment layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Treatments")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Treatment")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)

        self.label_med_dosage = QLabel("Med Dosage:")
        self.label_med_date = QLabel("Med Time Given:")
        self.label_med_time = QLabel("Med Date Given:")

        self.add_med_dosage = QLineEdit()
        self.date = date.today()
        self.date = self.date.strftime("{} {} {}".format("%d", "%m", "%Y"))
        self.add_med_date = QLineEdit(str(self.date))
        self.time = datetime.datetime.now()
        self.time = self.time.strftime("{}:{}".format("%H", "%M"))
        self.add_med_time = QLineEdit(str(self.time))

        self.treatments_grid = QGridLayout()

        self.treatments_grid.addWidget(self.enter_button,2,0)
        self.treatments_grid.addWidget(self.cancel_button,2,1)
        self.treatments_grid.addWidget(self.label_med_dosage,0,0)
        self.treatments_grid.addWidget(self.label_med_date,1,0)
        self.treatments_grid.addWidget(self.label_med_time,0,2)

        self.treatments_grid.addWidget(self.add_med_dosage,0,1)
        self.treatments_grid.addWidget(self.add_med_date,1,1)
        self.treatments_grid.addWidget(self.add_med_time,0,3)

        self.setLayout(self.treatments_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()

    def add_data(self):
        data = (self.add_med_dosage.text(), self.add_med_date.text(), self.add_med_time.text())
        sql = "insert into Treatments (MedDosage, MedDateGiven, MedTimeGiven) values (?,?,?)"
        adding_treatment = insert_data(data, sql)
        self.close()
