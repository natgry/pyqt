"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtCore

from b_systeminfo_widget import SystemInfoWindow


class UnitedWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.systemWindow = SystemInfoWindow()

        self.initUI()

        #self.weatherWindow =

    def initUI(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.systemWindow)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = UnitedWindow()
    win.show()

    app.exec()
