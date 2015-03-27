import sqlite3

def search_record(data, table_name, attribute, sort, option):
    with sqlite3.connect("main_database.db") as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        sql = "select {0} from {1} where {2}{3}?".format(attribute, table_name, sort, option)
        cursor.execute(sql, data)
        db.commit()

def search_patient(patient_name):
    with sqlite3.connect("main_database.db") as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        sql = "select {0} from Patient".format(patient_name)
        cursor.execute(sql)
        db.commit()

#Allow them to search without knowing all details
#(Search patient name, without knowing exactly what it is
#(Or search an attribute without knowing the table
#THEN (possibly) add a search overhaul that can include every attribute

def new_search_record(attribute):
    Patient_attribute_list = ["HospitalNo","DoctorID","FirstName","LastName","Age","Gender","DOB","TelWork","TelHome","Email","AddressLine1","AddressLine2","AddressLine3"]
    Admission_attribute_list = ["AdmissionID","HospitalNo","DoctorID","AdmissionDate","AdmissionTime","Call","CallTime","DischargeDate","DischargeTime"]

    table_name = None
    if attribute in Patient_attribute_list:
        table_name = "Patient"
    elif attribute in Admission_attribute_list:
        table_name = "Admission"
    search_record(data, table_name, attribute, sort, option)
        
                

if __name__ == "__main__":
    new_search_record()

