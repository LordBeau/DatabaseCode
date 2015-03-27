from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, sqlite3

class DBTable(QTableWidget):
    def __init__(self):
        super().__init__()

    def create_table(self):
        self.clear()
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.setSortingEnabled(False)
        with sqlite3.connect("main_database.db") as db:
            cursor = db.cursor()
            cursor.execute(self.sql)
        columns = [tuple[0] for tuple in cursor.description]
        self.setRowCount(0)
        self.setColumnCount(len(columns))
        self.setHorizontalHeaderLabels(columns)
        for row, form in enumerate(cursor):
            self.insertRow(row)
            for column, item in enumerate(form):
                self.setItem(row, column, QTableWidgetItem(str(item)))
        self.setSortingEnabled(True)
