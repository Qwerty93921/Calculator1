import os
from fast_html import *
from PyQt6.QtWidgets import *

def set_qt_plugin_path():
    # qpa_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
    # qpa_path = qpa_path.encode("latin").decode("utf-8")
    os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

set_qt_plugin_path()

print(render(p("text")))

app = QApplication([])
window = QMainWindow()

label = QLabel("Привет из Qt!")

window.setCentralWidget(label)
window.show()
app.exec()

print(render(p("text")))

# В терминале писать python -m venv venv
# Создается папка venv с файлами

# myvenv\scripts\activate - презентация
# .\venv\Scripts\activate - рабочий вариант

# Появляется (venv) - зеленым текстом ---------------------------------------------------------------------------

# https://pypi.org/project/fast-html/
# Скопировать и вставить строку от fast html в терминал
# fast-html 1.0.3
# pip install fast-html - вставить в терминал

# pip list - выдает это:

# Package    Version
# ---------- -------
# fast-html  1.0.3
# pip        21.2.4
# setuptools 58.1.0

# pip freeze - команда
# pip freeze > .\requirements.txt

# fast-html==1.0.3

# .gitignore venv - git игнорирует venv папку
# .gitignore - создать папку

# pip freeze > requirements.txt - создание файла

# pip - менеджер пакетов

# --------------------------------------------------------------------------------------------------------------------------------

# https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-open/ - with open тема(другая)

# https://ru.hexlet.io/courses/python-functions/lessons/map-filter-reduce/theory_unit - map, filter, reduce

# chrome://whats-new/ - chrome new functions

# --------------------------------------------------------------------------------------------------------------------------------

# pip install PyQt5

# $Env:QT_QPA_PLATFORM_PLUGIN_PATH = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

# python '.\Classwork 2\22 August py(Виртуальное окружение и менеджер пакетов)\Virtual environment INFO.py'
