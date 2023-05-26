"""
Модуль, в котором содержатся потоки работающих процессов
"""
import psutil
import time
from typing import Optional
from PySide6 import QtCore


class ProcInfo(QtCore.QThread):
    procInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def get_proc_info(self) -> Optional[dict]:
        """
        Получение списка работающих процессов
        :return: список работающих процессов
        """
        procs = {p.pid: (p.name(), p.status(), p.cpu_percent()) for p in psutil.process_iter(['name', 'username'])}
        return procs

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        if self.delay is None:
            self.delay = 1

        # запускаем бесконечный цикл получения информации о системе
        while True:
            proc_info = self.get_proc_info()
            self.systemSignal = proc_info
            self.procInfoReceived.emit(self.systemSignal)
            time.sleep(self.delay)
