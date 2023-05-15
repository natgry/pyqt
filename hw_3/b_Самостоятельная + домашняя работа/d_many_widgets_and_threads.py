"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QGroupBox, QWidget, QHBoxLayout, QVBoxLayout

from b_systeminfo_widget import SystemInfoWindow
from c_weatherapi_widget import WeatherHandlerWindow


# The method 1 based on QtWidgets.QMainWindow
class UnitedWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.systemWindow = SystemInfoWindow()
        self.weatherWindow = WeatherHandlerWindow()

        self.initUI()

    def initUI(self) -> None:
        """
        Complete UI initialization
        :return: None
        """
        self.setWindowTitle("United Window")
        self.resize(700, 600)
        self.centralwidget = QWidget()
        self.mainLayout = QHBoxLayout()

        self.groupBoxCpu = QGroupBox("System Info")
        self.verticalLayoutCpu = QVBoxLayout()
        self.verticalLayoutCpu.addWidget(self.systemWindow)
        self.groupBoxCpu.setLayout(self.verticalLayoutCpu)

        self.groupBoxWeather = QGroupBox("Weather Info")
        self.verticalLayoutWeather = QVBoxLayout()
        self.verticalLayoutWeather.addWidget(self.weatherWindow)
        self.groupBoxWeather.setLayout(self.verticalLayoutWeather)

        self.mainLayout.addWidget(self.groupBoxCpu)
        self.mainLayout.addWidget(self.groupBoxWeather)

        self.centralwidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralwidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = UnitedWindow()
    win.show()

    app.exec()


# The method 2 based on QtWidgets.QWidget
# class UnitedWindow(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.systemWindow = SystemInfoWindow()
#         self.weatherWindow = WeatherHandlerWindow()
#
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("UnitedWindow")
#         layout = QtWidgets.QHBoxLayout()
#         layout.addWidget(self.systemWindow)
#         layout.addWidget(self.weatherWindow)
#
#         self.setLayout(layout)
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication()
#
#     win = UnitedWindow()
#     win.show()
#
#     app.exec()
