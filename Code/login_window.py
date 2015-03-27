#Importing all that sys stuff
import sys, sqlite3

#I assume this is the core and GUI stuff
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#That main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Please log in")
        self.stacked_layout = QStackedLayout()
        self.create_initial_layout()
        self.create_second_layout()
    
        self.widget = QWidget()
        self.widget.setLayout(self.stacked_layout)
        self.setCentralWidget(self.widget)

    def create_initial_layout(self):
        self.text_box = QLineEdit()
        self.text_box1 = QLineEdit()
        self.button = QPushButton("Enter")
        self.label = QLabel()
        self.label1 = QLabel("Log in")
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.text_box1)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.text_box.returnPressed.connect(self.switch_layout)
        self.text_box.textChanged.connect(self.switch_layout)
        self.button.clicked.connect(self.switch_layout)
        self.text_box.setPlaceholderText("Username")
        self.text_box1.setPlaceholderText("Password")

    def validate_login(self):
        self.username = self.text_box()
        self.password = self.text_box1()

        #determine the login
        with sqlite3.connect("Logs.db") as db:
            cursor = db.cursor()
            cursor.execute("select * from accounts where username = ?", (self.username,))
            self.account = cursor.fetchone()

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()
