"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""
import time

from PySide6 import QtWidgets, QtCore, QtGui

from hw_2.b_hw.ui.c_signals_events import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None, primary_screen: QtWidgets.QApplication = None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.primary = primary_screen
        self.screenGeom = self.screen().availableGeometry()
        self.initUI()
        self.initSignals()

    def initUI(self):
        """
        Доинициализация Ui

        :return: None
        """
        pass

    def initSignals(self):
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)
        self.ui.pushButtonCenter.clicked.connect(self.onPushButtonCenterClicked)
        self.ui.pushButtonLB.clicked.connect(self.onPushButtonLBClicked)
        self.ui.pushButtonLT.clicked.connect(self.onPushButtonLTClicked)
        self.ui.pushButtonRT.clicked.connect(self.onPushButtonRTClicked)
        self.ui.pushButtonRB.clicked.connect(self.onPushButtonRBClicked)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onPushButtonMoveCoordsClicked)

    def onPushButtonGetDataClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonGetData

        :return: None
        """
        self.print_data()

    def print_data(self) -> None:
        """
        Получение параметров экрана и вывод параметров в plainTextEdit

        :return: None
        """
        data = []
        data_in_time = f"Текущее время: {time.ctime()}"
        data.append(data_in_time)

        screens = f"Кол-во экранов: {len(self.primary.screens())}"
        data.append(screens)

        currentWindow = f"Текущее основное окно: {self.objectName()}"
        data.append(currentWindow)

        screenRect = f"Разрешение экрана: {self.screenGeom.width()}, {self.screenGeom.height()}"
        data.append(screenRect)

        screenAt = f"На каком экране окно находится: {self.screen().name()}"
        data.append(screenAt)

        size = f"Размеры окна: {self.size().toTuple()}"
        data.append(size)

        min_size = f"Минимальные размеры окна: {self.minimumSize().toTuple()}"
        data.append(min_size)

        cur_pos = f"Текущее положение (координаты) окна: {self.pos().toTuple()}"
        data.append(cur_pos)

        centerPos = f"Координаты центра приложения: {self.screen().availableGeometry().center().toTuple()}"
        data.append(centerPos)

        state = f"Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено): " \
                f"{self.isHidden()}/{self.isMaximized()}/{self.isActiveWindow()}/{self.isVisible()}"
        data.append(state)

        text = "\n".join(data)
        self.ui.plainTextEdit.setPlainText(text)

    def onPushButtonMoveCoordsClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonMoveCoords

        :return: None
        """
        x = self.ui.spinBoxX.value()
        y = self.ui.spinBoxY.value()
        self.move(x, y)

    def onPushButtonCenterClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonCenter

        :return: None
        """
        frameGeom = self.frameGeometry()
        center = self.screen().availableGeometry().center()

        frameGeom.moveCenter(center)
        self.move(frameGeom.topLeft())

    def onPushButtonLTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLT

        :return: None
        """

        self.move(self.screenGeom.topLeft())

    def onPushButtonLBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonLB

        :return: None
        """

        self.move(0, self.screenGeom.bottom() - self.height())

    def onPushButtonRTClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRT

        :return: None
        """

        self.move(self.screenGeom.right() - self.width(), 0)

    def onPushButtonRBClicked(self) -> None:
        """
        Обработка сигнала clicked для кнопки pushButtonRB

        :return: None
        """
        self.move(self.screenGeom.right() - self.width(), self.screenGeom.bottom() - self.height())

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Обработка событий движения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """
        print(f"{time.ctime()} >> Moved: old pos: {event.oldPos().toTuple()}, "
              f"new pos: {event.pos().toTuple()}")

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Обработка событий изменения размера окна

        :param event: QtGui.QResizeEvent
        :return: None
        """
        print(f"{time.ctime()} >> Resized: old size: {event.oldSize().toTuple()}, "
              f"new size: {event.size().toTuple()}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window(primary_screen=app)
    window.show()

    app.exec()
