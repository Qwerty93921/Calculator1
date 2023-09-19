import sys
from PyQt6.QtWidgets import QApplication
from calc_main_window import CalcMainWindow
from calc_view import *
from calc_main_window import *
from calc_control import CalcControlWidget
from calc_model import *


options = {
    "Simple": {"model": SimpleCalcModel, "view": SimpleCalcView},
    "Account": {"model": AccountCalcModel, "view": AccountCalcView}
}

def switch_mode(name):
    if name in options:
        model = options[name]["model"]()
        view = options[name]["view"]()
        view.set_model(model)
        window.set_view(view)

if __name__ == "__main__":
    app = QApplication(sys.argv) # Создание приложения
    window = CalcMainWindow("Qalculus v. 1.0") # Название приложения

    fd = open("style.css", "r", encoding="UTF-8") # fd - файловый дескриптор
    style = fd.read() # соединение с CSS файлом
    fd.close()

    switch = CalcControlWidget(tuple(options.keys))
    switch.swithed.connect(switch_mode)
    window.set_switcher(switch)

    switch_mode("Simple")
    window.show() # Показать

    app.setStyleSheet(style)
    app.exec() # Запуск приложения


    # app.setStyleSheet("QMainWindow {background-color: green;}") # Как в CSS стили

    # model = AccountCalcModel()
    # view = SimpleCalcView()
    # window.set_view(view) # Внутри окна то что в скобках
