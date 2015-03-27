import sqlite3

def delete_record(table_name, attribute, data):
    with sqlite3.connect("main_database.db") as db:
        cursor = db.cursor()
        cursor.execute("Pragma foreign_keys = ON")
        sql = "delete from {0} where {1}=?".format(table_name, attribute)
        cursor.execute(sql, data)
        db.commit()

def get_delete_record():
    table_name = input("Table Name: ")
    attribute = input("Attribute: ")
    data = input("Attribute Value: ")
    delete_record(table_name, attribute, data)

if __name__ == "__main__":
    get_delete_record()
    
