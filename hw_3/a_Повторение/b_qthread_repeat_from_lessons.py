"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import time

import requests
from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initThread()
        self.initSignals()

    def initUi(self) -> None:
        """

        :return:
        """

        self.lineEditURL = QtWidgets.QLineEdit()
        self.lineEditURL.setPlaceholderText("Введите URL")

        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)

        labelSpinBox = QtWidgets.QLabel("Задержка обновления: ")
        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(1)

        self.pushButtonThreadHandle = QtWidgets.QPushButton("Запуск")
        self.pushButtonThreadHandle.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditURL)
        layout.addWidget(self.plainTextEdit)
        layout.addWidget(labelSpinBox)
        layout.addWidget(self.spinBoxDelay)
        layout.addWidget(self.pushButtonThreadHandle)

        self.setLayout(layout)

    def initThread(self) -> None:
        """

        :return:
        """

        self.thread = RequestsThread()

    def initSignals(self) -> None:
        """

        :return:
        """

        self.thread.responsed.connect(self.updateSiteStatus)
        self.thread.finished.connect(self.threadFinished)
        self.spinBoxDelay.valueChanged.connect(self.setURLDelay)
        self.pushButtonThreadHandle.clicked.connect(self.handleThread)

    def updateSiteStatus(self, status_code: int):
        """

        :param status_code:
        :return:
        """

        self.plainTextEdit.appendPlainText(f'{time.ctime()} >>> status code: {status_code}')

    def handleThread(self):
        """

        :return:
        """

        button_status = self.pushButtonThreadHandle.isChecked()

        if self.thread.isRunning() or self.thread.status or not button_status:
            self.thread.status = False
            self.pushButtonThreadHandle.setText("Запуск")
        else:
            self.thread.url = self.lineEditURL.text()
            self.thread.delay = self.spinBoxDelay.value()
            self.thread.start()
            self.pushButtonThreadHandle.setText("Остановка")

    def threadFinished(self):
        self.pushButtonThreadHandle.setChecked(False)
        self.pushButtonThreadHandle.setText("Запуск")

    def setURLDelay(self):
        """

        :return:
        """

        self.thread.delay = self.spinBoxDelay.value()


class RequestsThread(QtCore.QThread):
    responsed = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__status = None
        self.__url = ""
        self.__delay = 2

    @property
    def status(self) -> bool:
        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError

        self.__status = value

    @property
    def delay(self) -> int:
        return self.__delay

    @delay.setter
    def delay(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError

        self.__delay = value

    # @property
    # def url(self) -> str:
    #     return self.__url
    #
    # @url.setter
    # def url(self, value: str) -> None:
    #     if not isinstance(value, str):
    #         raise ValueError
    #
    #     self.__url = value

    def run(self) -> None:
        if not self.url:
            return

        self.status = True

        while self.status:
            try:
                response = requests.get(self.url)
                status_code = response.status_code
            except requests.exceptions.SSLError:
                status_code = -1

            self.responsed.emit(status_code)
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    # rt = RequestsThread()
    # rt.url = "https://googles.ru"
    # rt.responsed.connect(lambda data_from_thread: print(data_from_thread))
    #
    # rt.start()

    window = Window()
    window.show()

    app.exec()
