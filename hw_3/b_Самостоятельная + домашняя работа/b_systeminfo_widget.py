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

from PySide6 import QtWidgets

from a_threads import SystemInfo


class SystemInfoWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.initThread()

        self.initSignals()

    def initUI(self) -> None:
        """
        Инициализация фронтенда.
        :return: None
        """
        self.setWindowTitle("SystemInfoWindow")

        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(1)
        labelSpinBox = QtWidgets.QLabel("Время задержки потока: ")

        labelCpu = QtWidgets.QLabel("CPU >>>")
        self.plainTextEditCpu = QtWidgets.QPlainTextEdit()

        labelRam = QtWidgets.QLabel("RAM >>>")
        self.plainTextEditRam = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(labelSpinBox)
        layout.addWidget(self.spinBoxDelay)
        layout.addWidget(labelCpu)
        layout.addWidget(self.plainTextEditCpu)
        layout.addWidget(labelRam)
        layout.addWidget(self.plainTextEditRam)
        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.spinBoxDelay.textChanged.connect(self.spinBoxDelayTextChanged)
        self.thread.systemInfoReceived.connect(self.updateCpuRamInfo)

    def initThread(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.thread = SystemInfo()
        self.thread.start()

    def spinBoxDelayTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для поля spinBoxDelay

        :return: None
        """
        self.thread.delay = self.spinBoxDelay.value()

    def updateCpuRamInfo(self) -> None:
        """
        Обработка данных из потока

        :return: None
        """
        self.plainTextEditCpu.appendPlainText(f"{time.ctime()} >>> CPU:{self.thread.systemSignal[0]}")
        self.plainTextEditRam.appendPlainText(f"{time.ctime()} >>> RAM:{self.thread.systemSignal[1]}")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = SystemInfoWindow()
    win.show()

    app.exec()
