from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal

class CalcControlWidget(QWidget):
    swithed : pyqtSignal = None

    def calc_mode_switch(self):
        radiobtn = self.sender()
        if radiobtn.isChecked():
            text = radiobtn.text()
            self.swithed.emit(text) # Выпустить - emit

    def __init__(self):
        super().__init__()
        self.swithed = pyqtSignal(str)

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        radiobutton = QRadioButton(text = "Simple")
        radiobutton.setChecked(True)
        radiobutton.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton)

        radiobutton2 = QRadioButton(text = "account")
        radiobutton2.toggled.connect(self.calc_mode_switch)
        main_layout.addWidget(radiobutton2)
