#Importing all that sys stuff
import sys, sqlite3
from database_table import *
from update_all import *

from create_patient import *
from create_admission import *
from create_admission_trans import *
from create_doctor import *
from create_doctor_type import *
from create_diagnosis import *
from create_treatments import *
from create_med import *

from delete_record import *
from search_record import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
#That main window
class FirstLayout(QWidget):
    def __init__(self):
        super().__init__()

        #Record editing tools
        self.record_edit = QGridLayout()

        self.add_record_button = QPushButton("Add Record",self)
        self.update_record_button = QPushButton("Update Record",self)
        self.delete_record_button = QPushButton("Delete Record",self)
        self.refine_search_button = QPushButton("Refine Search",self)
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Patient Name")

        self.record_edit.addWidget(self.add_record_button,0,0)
        self.record_edit.addWidget(self.update_record_button,0,1)
        self.record_edit.addWidget(self.delete_record_button,0,2)
        self.record_edit.setColumnStretch(3,1)
        self.record_edit.addWidget(self.refine_search_button,0,4)
        self.record_edit.addWidget(self.search_box,0,5)

        self.add_record_button.clicked.connect(self.AddButton)
        self.update_record_button.clicked.connect(self.UpdateButton)
        self.delete_record_button.clicked.connect(self.DeleteButton)
        self.refine_search_button.clicked.connect(self.RefineSearch)
        self.search_box.textChanged.connect(self.Searching)

        #Table display widget
        self.data_display = QVBoxLayout()

        self.Table = DBTable()
        self.Table.sql = "select * from Patient"
        self.current_table = "Patient"
        self.Table.create_table()
        self.data_display.addWidget(self.Table)

        #Table switch widget
        self.data_switch = QGridLayout()

        self.patient_button = QPushButton("Patient", self)
        self.admission_button = QPushButton("Admission", self)
        self.admission_trans_button = QPushButton("Admission Trans", self)
        self.doctor_button = QPushButton("Doctor", self)
        self.doctor_type_button = QPushButton("Doctor Type", self)
        self.diagnosis_button = QPushButton("Diagnosis", self)
        self.treatments_button = QPushButton("Treatments", self)
        self.med_button = QPushButton("Meds", self)
        
        self.data_switch.addWidget(self.patient_button,0,0)
        self.data_switch.addWidget(self.admission_button,0,1)
        self.data_switch.addWidget(self.admission_trans_button,0,2)
        self.data_switch.addWidget(self.doctor_button,0,3)
        self.data_switch.addWidget(self.doctor_type_button,0,4)
        self.data_switch.addWidget(self.diagnosis_button,0,5)
        self.data_switch.addWidget(self.treatments_button,0,6)
        self.data_switch.addWidget(self.med_button,0,7)

        self.patient_button.clicked.connect(self.PatientTable)
        self.admission_button.clicked.connect(self.AdmissionTable)
        self.admission_trans_button.clicked.connect(self.AdmissionTransTable)
        self.doctor_button.clicked.connect(self.DoctorTable)
        self.doctor_type_button.clicked.connect(self.DoctorTypeTable)
        self.diagnosis_button.clicked.connect(self.DiagnosisTable)
        self.treatments_button.clicked.connect(self.TreatmentsTable)
        self.med_button.clicked.connect(self.MedTable)

        self.vertical = QVBoxLayout()

    def Searching(self):
        pass
        #search_patient(self.search_box)
        

    def AddButton(self):
        if self.current_table == "Patient":
            self.NewPatient = PatientWindow()
            self.PatientTable()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "HospitalNo"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "Admission":
            self.NewAdmission = AdmissionWindow()
            self.AdmissionTable()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "AdmissionID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "AdmissionTrans":
            self.NewTransport = AdmissionTransWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "AdmissionTransID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "Doctor":
            self.NewDoctor = DoctorWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "DoctorID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "DoctorType":
            self.NewType = DoctorTypeWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "DoctorTypeID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "Diagnosis":
            self.NewDiagnosis = DiagnosisWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "DiagnosisID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "Treatments":
            self.NewTreatment = TreatmentsWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "TreatmentID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()
            
        elif self.current_table == "Med":
            self.NewMedication = MedWindow()
            self.ThisRow = self.Table.currentRow()
            self.RowIDName = "MedID"
            self.RowID = QTableWidgetItem(self.Table.item(self.ThisRow, 0)).text()

    def UpdateButton(self):
        RecordUpdateWindow(self.current_table)

    def DeleteButton(self):
        pass

    def RefineSearch(self):
        pass

    def PatientTable(self):
        self.Table.sql = "select * from Patient"
        self.Table.create_table()
        self.current_table = "Patient"

    def AdmissionTable(self):
        self.Table.sql = "select * from Admission"
        self.Table.create_table()
        self.current_table = "Admission"

    def AdmissionTransTable(self):
        self.Table.sql = "select * from AdmissionTrans"
        self.Table.create_table()
        self.current_table = "AdmissionTrans"

    def DoctorTable(self):
        self.Table.sql = "select * from Doctor"
        self.Table.create_table()
        self.current_table = "Doctor"

    def DoctorTypeTable(self):
        self.Table.sql = "select * from DoctorType"
        self.Table.create_table()
        self.current_table = "DoctorType"

    def DiagnosisTable(self):
        self.Table.sql = "select * from Diagnosis"
        self.Table.create_table()
        self.current_table = "Diagnosis"

    def TreatmentsTable(self):
        self.Table.sql = "select * from Treatments"
        self.Table.create_table()
        self.current_table = "Treatments"

    def MedTable(self):
        self.Table.sql = "select * from Med"
        self.Table.create_table()
        self.current_table = "Med"
