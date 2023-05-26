"""
Модуль, в котором содержится поток получени текущего времени и даты
"""
import time

from PySide6 import QtCore


class TimeInfo(QtCore.QThread):
    timeInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__delay = 1

    def get_time(self) -> str:
        """
        Получение текущего времени
        :return: список работающих процессов
        """
        return str(time.ctime())

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        # запускаем бесконечный цикл получения информации о системе
        while True:
            time_info = self.get_time()
            self.systemSignal = time_info
            self.timeInfoReceived.emit(self.systemSignal)
            time.sleep(self.__delay)
