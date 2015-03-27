#Importing PyQt, sys and other required modules/functions
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from database_layout import *
from Create_Hospital_DB import *

#Creating the main class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Addenbrooke's PICU Database")
        self.setFixedSize(669,268)
        self.setWindowIcon(QIcon("Images\()23 Tile - RedCross2.png"))
        self.setStyleSheet("QMainWindow {background-image: url(./Images/best_layout.png) }");


                                
        #Create actions for which potential actions can be added
        self.find_product = QAction("Find Patients",self)
        self.show_product = QAction("Show Patients",self)

        #Create menu bar
        self.menu_bar = QMenuBar()

        self.file_menu = self.menu_bar.addMenu("File")
        self.patient_menu = self.menu_bar.addMenu("Patient")
        
        #Add action to MenuBar 
        self.patient_menu.addAction(self.find_product)
        self.patient_menu.addAction(self.show_product)

        self.setMenuBar(self.menu_bar)

        #self.create_main_widget()
        self.MainLayout = FirstLayout()
        self.MainLayout.vertical.addLayout(self.MainLayout.record_edit)
        self.MainLayout.vertical.addLayout(self.MainLayout.data_display)
        self.MainLayout.vertical.addLayout(self.MainLayout.data_switch)
        self.MainLayout.setLayout(self.MainLayout.vertical)
        
        self.stacked_layout = QStackedLayout()
        
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.central_widget)
        self.stacked_layout.addWidget(self.MainLayout)
        
if __name__ == "__main__":
##    made_database = False
##    while not made_database:
##        made_database = True
##        try:
            application = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            window.raise_()
            application.exec_()
##        except sqlite3.OperationalError:
##            made_database = False
##            create_my_database()


