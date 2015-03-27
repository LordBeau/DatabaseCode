import sqlite3

def create_table(db_name, table_name, sql):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
            if response == "y":
                keep_table = False
                print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                cursor.execute("drop table if exists {0}".format(table_name))
                db.commit()
            else:
                print("The existing table was kept.")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()


def create_my_database():

    db_name = "main_database.db"
    sql = """create table Patient(
             HospitalNo integer,
             DoctorID integer,
             FirstName text,
             LastName text,
             Age integer,
             Gender text,
             DOB text,
             TelWork text,
             TelHome text,
             Email text,
             AddressLine1 text,
             AddressLine2 text,
             AddressLine3 text,
             primary key(HospitalNo)
             foreign key(DoctorID) references Doctor(DoctorID))"""
    create_table(db_name, "Patient", sql)

    sql = """create table Admission(
             AdmissionID integer,
             HospitalNo integer,
             DoctorID integer,
             AdmissionDate text,
             AdmissionTime text,
             Call text,
             CallTime text,
             DischargeDate text,
             DischargeTime text,
             primary key(AdmissionID)
             foreign key(HospitalNo) references Patient(HospitalNo)
             foreign key(DoctorID) references Doctor(DoctorID))"""
    create_table(db_name, "Admission", sql)

    sql = """create table AdmissionTrans(
             AdmissionTransID integer,
             AdmissionTrans text,
             primary key(AdmissionTransID))"""
    create_table(db_name, "AdmissionTrans", sql)

    sql = """create table Doctor(
             DoctorID integer,
             DoctorTypeID integer,
             DoctorForename text,
             DoctorSurname text,
             DoctorWorkTel text,
             DoctorMobile text,
             DoctorEmail text,
             primary key(DoctorID)
             foreign key(DoctorTypeID) references DoctorType(DoctorTypeID))"""
    create_table(db_name, "Doctor", sql)

    sql = """create table DoctorType(
             DoctorTypeID integer,
             DoctorType text,
             primary key(DoctorTypeID))"""
    create_table(db_name, "DoctorType", sql)


    sql = """create table Diagnosis(
             DiagnosisID integer,
             DoctorID integer,
             HospitalNo integer,
             DiagnosisNoteDate text,
             DiagnosisNoteTime text,
             primary key(DiagnosisID),
             foreign key(DoctorID) references Doctor(DoctorID),
             foreign key(HospitalNo) references Patient(HospitalNo))"""
    create_table(db_name, "Diagnosis", sql)

    sql = """create table Treatments(
             TreatmentID integer,
             DiagnosisID integer,
             MedID integer,
             MedDosage text,
             MedTimeGiven text,
             MedDateGiven text,
             primary key(TreatmentID),
             foreign key(DiagnosisID) references Diagnosis(DiagnosisID)
             foreign key(MedID) references Med(MedID))"""
    create_table(db_name, "Treatments", sql)

    sql = """create table Med(
             MedID integer,
             MedName text,
             primary key(MedID))"""
    create_table(db_name, "Med", sql)

if __name__ == "__main__":
    create_my_database()
