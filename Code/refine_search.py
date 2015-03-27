from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Radio_Button_Widget_Class import *
from birthdate_combo_box import *
from insert_record import *

import sys

class RefineSearchWindow(QDialog):
    """Search layout"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Specific Search)
        self.create_layout()

    def create_layout(self):
        self.setModal(True)
        self.enter_button = QPushButton("Search")
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        self.label_forename = QLabel("Select:")
                            #Premade Box - has all tables
                            #For instance: Patient
        self.label_surname = QLabel("Where:")
                            #Line edit - Pick an attribute
                            #For instance: Admission Date
        self.label_age = QLabel("Is:")
                            #Premade Box
                            #For instance: >
        self.label_gender = QLabel("The following:")
                            #Line Edit
                            #Whatever you want
        self.label_dob = QLabel("Search Type")
                            #Radio
        self.label_telwork = QLabel("Order by:")
                            #premade - Ascending, etc
        

        self.add_forename = QLineEdit()
        self.add_surname = QLineEdit()
        self.add_gender = RadioButtonWidget("","",("Male","Female"))
        self.add_dob = RadioButtonWidget("","",("Exact", "Non-Exact"))
        self.add_telwork = QLineEdit()
        self.add_telhome = QLineEdit()
        self.add_email = QLineEdit()
        self.add_address1 = QLineEdit()
        self.add_address2 = QLineEdit()
        self.add_address3 = QLineEdit()

        self.patient_grid = QGridLayout()

        self.patient_grid.addWidget(self.enter_button,2,0)
        self.patient_grid.addWidget(self.cancel_button,2,1)
        self.patient_grid.addWidget(self.label_forename,0,0)
        self.patient_grid.addWidget(self.label_surname,1,0)
        self.patient_grid.addWidget(self.label_gender,0,2)
        self.patient_grid.addWidget(self.label_dob,1,2)
        self.patient_grid.addWidget(self.label_telwork,0,4)
        self.patient_grid.addWidget(self.label_telhome,1,4)
        self.patient_grid.addWidget(self.label_email,2,4)
        self.patient_grid.addWidget(self.label_address1,0,6)
        self.patient_grid.addWidget(self.label_address2,1,6)
        self.patient_grid.addWidget(self.label_address3,2,6)
                
        self.patient_grid.addWidget(self.add_forename,0,1)
        self.patient_grid.addWidget(self.add_surname,1,1)
        self.patient_grid.addWidget(self.add_gender,0,3)
        self.patient_grid.addWidget(self.add_dob,1,3)
        self.patient_grid.addWidget(self.add_telwork,0,5)
        self.patient_grid.addWidget(self.add_telhome,1,5)
        self.patient_grid.addWidget(self.add_email,2,5)
        self.patient_grid.addWidget(self.add_address1,0,7)
        self.patient_grid.addWidget(self.add_address2,1,7)
        self.patient_grid.addWidget(self.add_address3,2,7)

        self.setLayout(self.patient_grid)

        self.enter_button.clicked.connect(self.add_data)
        self.exec_()
        
    def add_data(self):
        self.get_age()
        Gender = "Male"
        if self.add_gender.selected_button == 2:
            Gender = "Female"
        data = (self.add_forename.text(), self.add_surname.text(), self.Age, Gender,"00009983", self.add_telwork.text(), self.add_telhome.text(), self.add_email.text(), self.add_address1.text(), self.add_address2.text(), self.add_address3.text())
        sql = "insert into Patient (FirstName, LastName, Age, Gender, DOB, TelWork, TelHome, Email, AddressLine1, AddressLine2, AddressLine3) values (?,?,?,?,?,?,?,?,?,?,?)"
        adding_patient = insert_data(data, sql)
        self.close()

    def get_age(self):
        older = False
        current_month = str(date.today())
        current_month = int(current_month[5:7])
        birth_month = int(self.add_dob.month_combo.currentText())
        month = current_month - birth_month
        if month >= 0:
            current_day = str(date.today())
            current_day = int(current_day[8:])
            birth_day = int(self.add_dob.day_combo.currentText())
            day = current_day - birth_day
            if day >= 0:
                older = True
        current_year = int(str(date.today())[0:4])
        birth_year = int(self.add_dob.year_combo.currentText())
        self.Age = current_year - birth_year
        if older == False:
            self.Age -= 1
    
def main():
    patient_view = QApplication(sys.argv)
    patient_window = PatientWindow()
    patient_window.show()
    patient_window.raise_()
    patient_view.exec_()




if __name__ == "__main__":
    main()
