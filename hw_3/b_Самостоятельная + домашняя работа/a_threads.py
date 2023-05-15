"""
Модуль в котором содержаться потоки Qt
"""

import time
from typing import Optional

import psutil
import requests
from PySide6 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        """
        Метод для запуска потока
        :return: None
        """
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemSignal = [cpu_value, ram_value]  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            self.systemInfoReceived.emit(self.systemSignal)
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    weatherInfoReceived = QtCore.Signal(str)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """
        if not isinstance(delay, int):
            raise ValueError
        self.__delay = delay

    @property
    def delay(self) -> int:
        """
        Метод для получения информации о времени задержки потока

        :return: текущее время задержки потока
        """
        return self.__delay

    @property
    def status(self) -> Optional[bool]:
        """
        Метод для получения информации о статусе потока

        :return: текущий статус потока
        """
        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        """
        Метод для установки статуса потока

        :param value: статус потока
        :return: None
        """
        if not isinstance(value, bool):
            raise ValueError

        self.__status = value

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        # TODO настройте метод для корректной работы

        self.__status = True
        while self.__status:
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """
            response = requests.get(self.__api_url)
            self.data = response.json()
            self.weatherInfoReceived.emit(self.data)
            time.sleep(self.__delay)
