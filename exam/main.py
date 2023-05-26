"""
Разработать приложение для мониторинга нагрузки системы и системных процессов (аналог диспетчера задач).

Обязательные функции в приложении:

1) Показ общих сведений о системе (в текстовом виде!):
 - Название процессора, количество ядер, текущая загрузка
 - Общий объём оперативной памяти, текущая загрузка оперативаной памяти
 - Количество, жестких дисков + информация по каждому (общий/занятый объём)
2) Обеспечить динамический выбор обновления информации (1, 5, 10, 30 сек.)
3) Показ работающих процессов
4) Показ работающих служб
5) Показ задач, которые запускаются с помощью планировщика задач
"""
from PySide6 import QtWidgets

from exam.widgets.system_monitor import SystemMonitorWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = SystemMonitorWindow()
    win.show()

    app.exec()