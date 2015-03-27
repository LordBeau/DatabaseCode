from PyQt4.QtCore import *
from PyQt4.QtGui import *

from database_table import *

from create_patient import *
from create_admission import *
from create_admission_trans import *
from create_doctor import *

import sys

class RecordUpdateWindow(QDialog):
    """Updating"""

    def __init__(self, ct):
        super().__init__()
        if ct == "Patient":
           Update = PatientWindow(1)
