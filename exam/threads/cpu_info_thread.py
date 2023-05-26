"""
Модуль в котором содержатся потоки общих сведений о системе:
 - Название процессора, количество ядер, текущая загрузка
 - Общий объём оперативной памяти, текущая загрузка оперативаной памяти
 - Количество, жестких дисков + информация по каждому (общий/занятый объём)
"""
import platform
import time
from collections import namedtuple
import psutil
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def get_cpu_info(self) -> namedtuple:
        """
        Получить информацию о названии процессора, количестве ядер, текущей загрузки
        :return: namedtuple c информацией о названии процессора, количестве ядер, текущей загрузки
        """
        cpu = namedtuple('cpu', 'cpu_name cpu_count cpu_percent')

        cpu_name = platform.processor()
        cpu_count = psutil.cpu_count()
        cpu_percent = psutil.cpu_percent()
        return cpu(cpu_name, cpu_count, cpu_percent)

    def get_ram_info(self) -> namedtuple:
        """
        Получить информацию об общем объёме оперативной памяти, текущей загрузки оперативаной памяти
        :return: namedtuple c информацией об общем объёме оперативной памяти,
                текущей загрузки оперативаной памяти
        """
        ram = namedtuple('ram', 'ram_total ram_used')

        ram_total = psutil.virtual_memory().total
        ram_used = psutil.virtual_memory().used
        return ram(ram_total, ram_used)

    def get_disks_info(self) -> namedtuple:
        """
        Получить информацию о количестве, жестких дисков +
        информация по каждому (общий/занятый объём)
        :return: namedtuple c информацией о количестве, жестких дисков +
                информация по каждому (общий/занятый объём)
        """
        disks = namedtuple('disks', 'count info')
        disk_info = namedtuple('disk_info', 'total used mountpoint')

        physical_disks = psutil.disk_partitions()
        disks_count = len(physical_disks)
        list_ = []
        for diskpart in physical_disks:
            total = psutil.disk_usage(diskpart.device).total
            used = psutil.disk_usage(diskpart.device).used
            mountpoint = diskpart.device
            list_.append(disk_info(total, used, mountpoint))
        return disks(disks_count, list_)

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        if self.delay is None:
            self.delay = 1

        # запускаем бесконечный цикл получения информации о системе
        while True:
            cpu_info = self.get_cpu_info()
            ram_info = self.get_ram_info()
            disks_info = self.get_disks_info()
            self.systemSignal = [cpu_info, ram_info, disks_info]
            self.systemInfoReceived.emit(self.systemSignal)
            time.sleep(self.delay)
