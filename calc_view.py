from PyQt6.QtWidgets import *
import os
import sys
from calc_main_window import *
from calc_model import *


if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "venv/Lib/site-packages/PyQt6/Qt6/plugins/platforms"


class SimpleCalcView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 300)
        self.calculator_buttons()

    def calculator_buttons(self):
        layout = QVBoxLayout()
        self.label = QLabel("0")
        layout.addWidget(self.label)

        grid_of_buttons = QGridLayout()
        calc_buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            "0", ",", "=", "/"
        ]

        row, column = 1, 0

        for nums in calc_buttons:
            button = QPushButton(nums)
            grid_of_buttons.addWidget(button, row, column)

            column = (column + 1) % 4
            if column == 0:
                row += 1

        layout.addLayout(grid_of_buttons)
        self.setLayout(layout)

def calculator_activate():
    app = QApplication([])
    calculator = SimpleCalcView()
    calculator.show()
    app.exec()

calculator_activate()

class AccountCalcView(SimpleCalcView):
    def __init__(self):
        super().__init__()
        keys_layout = QGridLayout()
        self.layout().addLayout(keys_layout)

        keys = ('(', ')', '%', '')

        for r in range(len(keys)):
            key = keys[r]
            if key:
                btn = QPushButton(text = key)
                btn.clicked.connect(self.on_button_pressed)
                if key != '%':
                    keys_layout.addWidget(btn, 0, r)
                else:
                    keys_layout.addWidget(btn, 0, r, 1, 2)
