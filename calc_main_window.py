from PyQt6.QtWidgets import QMainWindow
from calc_view import SimpleCalcView

class CalcMainWindow(QMainWindow): # Унаследование от QMainWindow
    calc_view = None
    calc_layout = None

    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        self.calc_layout = QGridLayout()
        self.setLayout(self.calc_layout)

    def set_view(self, view):
        self.calc_view = view
        self.calc_layout.addWidget(self.calc_view, 1, 0)

    def set_model(self, model):
        self.calc_model = model
        if self.calc_view:
            self.calc_view.set_model(model)

    def set_switcher(self, widget):
        self.calc_layout.addWidget(widget, 0, 0)
