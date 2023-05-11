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

from PySide6 import QtWidgets, QtCore
import requests


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()
        self.initThread()
        self.initSignals()

    def initUI(self):
        """

        :return:
        """
        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Enter URL: ")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(1)
        labelSpinBox = QtWidgets.QLabel("Delay: ")
        self.pushBtnThradHandle = QtWidgets.QPushButton("Start")
        self.pushBtnThradHandle.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEditUrl)
        layout.addWidget(self.plainTextEdit)
        layout.addWidget(labelSpinBox)
        layout.addWidget(self.spinBoxDelay)
        layout.addWidget(self.pushBtnThradHandle)
        self.setLayout(layout)

    def initThread(self):
        self.thread = RequestsThread()

    def initSignals(self):
        self.thread.responsed.connect(self.updateSiteStatus)
        self.thread.finished.connect(self.threadFinished)
        self.pushBtnThradHandle.clicked.connect(self.handleThread())
        self.spinBoxDelay.valueChanged.connect(self.setUrlDelay)

    def updateSiteStatus(self, status_code: int):
        self.plainTextEdit.appendPlainText(f"{time.ctime()} >>> status code:{status_code}")

    def handleThread(self):
        btn_status = self.pushBtnThradHandle.isChecked()
        if self.thread.isRunning() or self.thread.status or not btn_status:
            self.thread.status = False
            self.pushBtnThradHandle.setText("Start")
        else:
            self.thread.url = self.lineEditUrl.text()
            self.thread.delay = self.spinBoxDelay.value()
            self.thread.start()
            self.pushBtnThradHandle.setText("Stop")

    def threadFinished(self):
        self.pushBtnThradHandle.setChecked(False)

    def setUrlDelay(self):
        self.thread.delay = self.spinBoxDelay.text()
        self.pushBtnThradHandle.setText("Start")


class RequestsThread(QtCore.QThread):
    responsed = QtCore.Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__status = None
        self.__url = ""
        self.__delay = 2

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError
        self.__status = value

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError
        self.__delay = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError
        self.__url = value

    def run(self) -> None:
        if not self.url:
            return

        self.status = True
        while self.status:
            try:
                response = requests.get(self.url)
                status_code = response.status_code
            except requests.exceptions:
                status_code = -1

            self.responsed.emit(status_code)
            time.sleep(self.delay)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    # rt = RequestsThread()
    # rt.url = "https://google.ru"
    # rt.responsed.connect(lambda data_from_thread: print(data_from_thread))
    # rt.start()
    window = Window()
    window.show()

    app.exec()
