import sqlite3

def insert_data(data, sql):
    with sqlite3.connect("main_database.db") as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        cursor.execute(sql, data)
        db.commit()

def add_patient_record():
    data = (input("First Name: "), input("Last Name: "), input("Age: "), input("Gender: "), input("Date of birth: "), input("Work phone: "), input("Home phone: "), input("Email: "), input("Address line 1: "), input("Address line 2: "), input("Address line 3: "))
    return data

def add_admission_record():
    data = (input("AdmissionDate: "), input("AdmissionTime: "), input("Call: "), input("CallTime: "), input("DischargeDate: "), input("DischargeTime: "))
    return data

def add_admissiontrans_record():
    data = input("AdmissionTrans: ")
    return data

def add_doctor_record():
    data = (input("First Name: "), input("Last Name: "), input("WorkTel: "), input("Mobile: "), input("Email: "))
    return data

def add_doctortype_record():
    data = input("DoctorType: ")
    return data

def add_diagnosis_record():
    data = (input("DiagnosisNoteDate: "), input("DiagnosisNoteTime: "))
    return data

def add_treatments_record():
    data = (input("MedDosage: "), input("MedTimeGiven: "), input("MedDateGiven: "))
    return data

def add_med_record():
    data = input("MedName: ")
    return data

def something():
    this = False
    while not this:
        value = None
        true = False
        while not true:
            try:
                if value not in [0,1,2,3,4,5,6,7,8,9]:
                    menu_choice()
                    print()
                    print("Please select a valid option")
                    print()
                    value = int(input("Which option would you like to pick: "))
                else:
                    true = True
            except ValueError:
                print()
                print("Don't be a pap")
                true = False
                
        if value == 1:
            data = add_patient_record()
            sql = "insert into Patient (FirstName, LastName, Age, Gender, DOB, TelWork, TelHome, Email, AddressLine1, AddressLine2, AddressLine3) values (?,?,?,?,?,?,?,?,?,?,?)"
            insert_data(data, sql)
        elif value == 2:
            data = add_admission_record()
            sql = "insert into Admission (AdmissionDate, AdmissionTime, Call, CallTime, DischargeDate, DischargeTime) values (?,?,?,?,?,?)"
            insert_data(data, sql)
        elif value == 3:
            data = add_admissiontrans_record()
            sql = "insert into AdmissionTrans (AdmissionTrans) values (?)"
            insert_data(data, sql)
        elif value == 4:
            data = add_doctor_record()
            sql = "insert into Doctor (DoctorForename, DoctorSurname, DoctorWorkTel, DoctorMobile, DoctorEmail) values (?,?,?,?,?)"
            insert_data(data, sql)
        elif value == 5:
            data = add_doctortype_record()
            sql = "insert into DoctorType (DoctorType) values (?)"
            insert_data(data, sql)
        elif value == 6:
            data = add_diagnosis_record()
            sql = "insert into Diagnosis (DiagnosisNoteDate, DiagnosisNoteTime) values (?,?)"
            insert_data(data, sql)
        elif value == 7:
            data = add_treatments_record()
            sql = "insert into Treatments (MedDosage, MedTimeGiven, MedDateGiven) values (?,?,?)"
            insert_data(data, sql)
        elif value == 8:
            data = add_med_record()
            sql = "insert into Med (MedName) values (?)"
            insert_data(data, sql)
        elif value == 0:
                this = True
   
        
    

def menu_choice():
    print()
    print("1. Patient")
    print("2. Admission")
    print("3. AdmissionTrans")
    print("4. Doctor")
    print("5. DoctorType")
    print("6. Diagnosis")
    print("7. Treatments")
    print("8. Meds")
    print("0. Quit")



if __name__ == "__main__":
    something()
