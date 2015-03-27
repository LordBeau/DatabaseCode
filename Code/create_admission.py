from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Radio_Button_Widget_Class import *
from birthdate_combo_box import *
from insert_record import *
import sys, datetime

class AdmissionWindow(QDialog):
    """Admission layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Admission")
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Add Admission")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        self.label_forename = QLabel("Admission Date:")
        self.label_surname = QLabel("Admission Time:")
        self.label_gender = QLabel("Call:")
        self.label_dob = QLabel("Call Time:")
        self.label_telwork = QLabel("Discharge Date:")
        self.label_telhome = QLabel("Discharge Time:")

        self.date = date.today()
        self.date = self.date.strftime("{} {} {}".format("%d", "%m", "%Y"))
        self.add_forename = QLineEdit(str(self.date))
        self.time = datetime.datetime.now()
        self.time = self.time.strftime("{}:{}".format("%H", "%M"))
        self.add_surname = QLineEdit(str(self.time))
        self.add_gender = RadioButtonWidget("","",("Yes","No"))
        self.add_dob = QLineEdit()
        self.add_dob.setPlaceholderText(str(self.time))
        self.add_telwork = QLineEdit()
        self.add_telwork.setPlaceholderText("Example: 01 01 2015")
        self.add_telhome = QLineEdit()
        self.add_telhome.setPlaceholderText("Example: 12:00")

        self.patient_grid = QGridLayout()

        self.patient_grid.addWidget(self.enter_button,2,0)
        self.patient_grid.addWidget(self.cancel_button,2,1)
        self.patient_grid.addWidget(self.label_forename,0,0)
        self.patient_grid.addWidget(self.label_surname,1,0)
        self.patient_grid.addWidget(self.label_gender,0,2)
        self.patient_grid.addWidget(self.label_dob,1,2)
        self.patient_grid.addWidget(self.label_telwork,0,4)
        self.patient_grid.addWidget(self.label_telhome,1,4)
                
        self.patient_grid.addWidget(self.add_forename,0,1)
        self.patient_grid.addWidget(self.add_surname,1,1)
        self.patient_grid.addWidget(self.add_gender,0,3)
        self.patient_grid.addWidget(self.add_dob,1,3)
        self.patient_grid.addWidget(self.add_telwork,0,5)
        self.patient_grid.addWidget(self.add_telhome,1,5)

        self.setLayout(self.patient_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()
        
    def add_data(self):
        Gender = "Yes"
        if self.add_gender.selected_button == 2:
            Gender = "No"
        
        data = (self.add_forename.text(), self.add_surname.text(), Gender, self.add_dob.text(), self.add_telwork.text(), self.add_telhome.text())
        sql = "insert into Admission (AdmissionDate,AdmissionTime,Call,CallTime,DischargeDate,DischargeTime) values (?,?,?,?,?,?)"
        adding_admission = insert_data(data, sql)
        self.close()

    
def main():
    patient_view = QApplication(sys.argv)
    patient_window = PatientWindow()
    patient_window.show()
    patient_window.raise_()
    patient_view.exec_()




if __name__ == "__main__":
    main()
