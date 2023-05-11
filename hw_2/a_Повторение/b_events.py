"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""
from time import ctime

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def event(self, event: QtCore.QEvent) -> bool:
        print(ctime(), event.type())

        # or to react on specific event
        # if QtCore.QEvent.Type.Move == event.type():
        #     print(ctime(), event.type())
        #     event: QtCore.QEvent.Type.Move
        #     print(event.pos())

        return super(Window, self).event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
