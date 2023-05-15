"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time

from PySide6 import QtWidgets

from a_threads import WeatherHandler


class WeatherHandlerWindow(QtWidgets.QWidget):
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
        self.setWindowTitle("WeatherHandlerWindow")

        labelLatitude = QtWidgets.QLabel("Широта:")
        self.spinBoxLatitude = QtWidgets.QSpinBox()
        self.spinBoxLatitude.setMinimum(-90)
        self.spinBoxLatitude.setMaximum(90)

        labelLongitude = QtWidgets.QLabel("Долгота:")
        self.spinBoxLongitude = QtWidgets.QSpinBox()
        self.spinBoxLongitude.setMinimum(-180)
        self.spinBoxLongitude.setMaximum(180)

        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(10)
        labelSpinBox = QtWidgets.QLabel("Время задержки потока: ")

        labelWeather = QtWidgets.QLabel("Информация о погоде >>>")
        self.plainTextEditWeather = QtWidgets.QPlainTextEdit()
        self.plainTextEditWeather.setReadOnly(True)

        self.pushBtnThreadHandle = QtWidgets.QPushButton("Запустить поток")
        self.pushBtnThreadHandle.setCheckable(True)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(labelLatitude)
        layout.addWidget(self.spinBoxLatitude)
        layout.addWidget(labelLongitude)
        layout.addWidget(self.spinBoxLongitude)
        layout.addWidget(labelSpinBox)
        layout.addWidget(self.spinBoxDelay)
        layout.addWidget(labelWeather)
        layout.addWidget(self.plainTextEditWeather)
        layout.addWidget(self.pushBtnThreadHandle)
        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.pushBtnThreadHandle.clicked.connect(self.handleThread)
        self.spinBoxDelay.textChanged.connect(self.spinBoxDelayTextChanged)
        self.spinBoxLatitude.textChanged.connect(self.spinBoxLatitudeTextChanged)
        self.spinBoxLongitude.textChanged.connect(self.spinBoxLongitudeTextChanged)

    def initThreadSignals(self) -> None:
        self.thread.weatherInfoReceived.connect(self.updateWeatherInfo)
        self.thread.finished.connect(self.threadFinished)

    def initThread(self):
        """
        Инициализация потоков

        :return: None
        """
        lat = self.spinBoxLatitude.value()
        lon = self.spinBoxLongitude.value()
        self.thread = WeatherHandler(lat, lon)

        self.initThreadSignals()

    def handleThread(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushBtnThreadHandle

        :return: None
        """
        btn_status = self.pushBtnThreadHandle.isChecked()
        if self.thread.isRunning() or self.thread.status or not btn_status:
            self.thread.status = False
        else:
            self.thread.start()
            self.pushBtnThreadHandle.setText("Остановить поток")
            self.spinBoxLatitude.setEnabled(False)
            self.spinBoxLongitude.setEnabled(False)
            self.spinBoxDelay.setEnabled(False)

    def threadFinished(self) -> None:
        """
        Обработка остановки потока

        :return:
        """
        self.spinBoxLatitude.setEnabled(True)
        self.spinBoxLongitude.setEnabled(True)
        self.spinBoxDelay.setEnabled(True)
        self.plainTextEditWeather.clear()
        self.pushBtnThreadHandle.setText("Запустить поток")
        self.pushBtnThreadHandle.setChecked(False)

    def updateWeatherInfo(self) -> None:
        """
        Обработка данных из потока

        :return:
        """
        self.plainTextEditWeather.setPlainText(f"{time.ctime()} >>> {self.thread.data}")

    def spinBoxDelayTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для поля spinBoxDelay

        :return: None
        """
        self.thread.setDelay(self.spinBoxDelay.value())

    def spinBoxLatitudeTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для поля spinBoxLatitude

        :return: None
        """
        self.initThread()

    def spinBoxLongitudeTextChanged(self) -> None:
        """
        Обработка сигнала textChanged для поля spinBoxLongitude

        :return: None
        """
        self.initThread()


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = WeatherHandlerWindow()
    win.show()

    app.exec()
