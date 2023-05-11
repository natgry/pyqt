"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
import time

from PySide6 import QtWidgets, QtCore

from a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.initThread()

        self.initSignals()

    def initUI(self) -> None:
        """
        Complete UI initialization
        :return: None
        """
        self.setWindowTitle("SystemInfoWindow")

        self.lineEditDelay = QtWidgets.QLineEdit()
        self.lineEditDelay.setPlaceholderText("Enter delay")

        labelCpu = QtWidgets.QLabel("CPU >>>:")
        self.plainTextEditCpu = QtWidgets.QPlainTextEdit()

        labelRam = QtWidgets.QLabel("RAM >>>: ")
        self.plainTextEditRam = QtWidgets.QPlainTextEdit()

        layout_cpu = QtWidgets.QHBoxLayout()
        layout_cpu.addWidget(labelCpu)
        layout_cpu.addWidget(self.plainTextEditCpu)

        layout_ram = QtWidgets.QHBoxLayout()
        layout_ram.addWidget(labelRam)
        layout_ram.addWidget(self.plainTextEditRam)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditDelay)
        layout.addLayout(layout_cpu)
        layout.addLayout(layout_ram)
        self.setLayout(layout)

    def initSignals(self):
        """
        Инициализация сигналов
        :return: None
        """
        self.lineEditDelay.textChanged.connect(self.lineEditDelayTextChanged)
        self.thread.systemInfoReceived.connect(self.updateCpuRamInfo)

    def initThread(self):
        """
        Инициализация потоков

        :return: None
        """
        self.thread = SystemInfo()
        self.thread.start()

    def lineEditDelayTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для поля lineEditDelay

        :return: None
        """
        delay = self.lineEditDelay.text()
        if delay:
            delay = int(delay)
        else:
            delay = 1
        self.thread.delay = delay

    def updateCpuRamInfo(self) -> None:
        """
        Обработка данных из потока

        :return: None
        """
        self.plainTextEditCpu.appendPlainText(f"{time.ctime()} >>> CPU:{self.thread.systemSignal[0]}")
        self.plainTextEditRam.appendPlainText(f"{time.ctime()} >>> CPU:{self.thread.systemSignal[1]}")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = SystemInfoWindow()
    win.show()

    app.exec()
