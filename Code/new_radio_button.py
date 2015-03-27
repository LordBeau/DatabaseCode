from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    def __init__(self, label, instruction, button_list):
        super().__init__()
        self.title_label = QLabel(label)
        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        self.radio_button_list[0].setChecked(True)
        self.radio_button_layout = QHBoxLayout()
        counter = 1
                        
