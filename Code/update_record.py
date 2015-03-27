import sqlite3

def update_record(data, table_name, attribute):
    with sqlite3.connect("main_database.db") as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        if table_name == "Patient":
            sql = "update {0} set {1}=? where HospitalNo=?".format(table_name, attribute)
        elif table_name == "Treatments":
            sql = "update {0} set {1}=? where TreatmentID=?".format(table_name, attribute)
        else:
            sql = "update {0} set {1}=? where {0}ID=?".format(table_name, attribute)
        cursor.execute(sql, data)
        db.commit()

def get_update_record():
    table_name = input("Table Name: ")
    attribute = input("Attribute: ")
    data = (input("New attribute: "), input("Unique ID: "))
    update_record(data, table_name, attribute)

if __name__ == "__main__":
    get_update_record()

