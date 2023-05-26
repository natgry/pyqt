"""
Модуль, в котором содержатся потоки работающих служб
"""
import time
from typing import Optional

import psutil
from PySide6 import QtCore


class ServiceInfo(QtCore.QThread):
    serviceInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def get_service_info(self) -> Optional[list]:
        """
        Получение списка работающих служб
        :return: список работающих служб
        """
        services = [p.as_dict() for p in psutil.win_service_iter()]
        return services

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        if self.delay is None:
            self.delay = 1

        # запускаем бесконечный цикл получения информации о системе
        while True:
            serv_info = self.get_service_info()
            self.systemSignal = serv_info
            self.serviceInfoReceived.emit(self.systemSignal)
            time.sleep(self.delay)
