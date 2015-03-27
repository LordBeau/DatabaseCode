from PyQt4.QtGui import *
from datetime import *

class BirthDate(QWidget):
    """Date of birth widget"""
    def __init__(self, unit):
        super().__init__()
        if unit != 2:
            self.day_combo = QComboBox(self)
            self.month_combo = QComboBox(self)
            self.year_combo = QComboBox(self)
            self.split_label = QLabel("/")
            self.split_label2 = QLabel("/")

            day_list = []
            for count in range(31):
                day_list.append(str(count+1))
            self.day_combo.addItems(day_list)

            month_list = []
            for count in range(12):
                month_list.append(str(count+1))
            self.month_combo.addItems(month_list)


            year_list = []
            year = date.today()
            year = int(year.strftime("%Y"))
            if unit == 1:
                for count in range(19,0,-1):
                    year_list.append(str(count + year - 19))
            elif unit == 2:
                for count in range(100, 0, -1):
                    year_list.append(str(count + year - 100))
            self.year_combo.addItems(year_list)

            self.date_box = QHBoxLayout()
            self.date_box.addWidget(self.day_combo)
            self.date_box.addWidget(self.split_label)
            self.date_box.addWidget(self.month_combo)
            self.date_box.addWidget(self.split_label2)
            self.date_box.addWidget(self.year_combo)
            self.setLayout(self.date_box)
        else:
            self.trans_combo = QComboBox(self)

            trans_list = ["Ambulance", "Car", "Helicopter", "Foot", "Other"]

            self.trans_combo.addItems(trans_list)

            self.box = QVBoxLayout()
            self.box.addWidget(self.trans_combo)
            self.setLayout(self.box)
