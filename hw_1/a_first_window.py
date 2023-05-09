from PySide6 import QtWidgets, QtCore


class MyFirstWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        """
        Complete UI initialization
        :return: None
        """
        self.setWindowTitle("My First Window")
        #self.resize(300, 100)
        size = QtCore.QSize(300, 100)
        self.resize(size)

        size = self.size()
        print(size)
        

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = MyFirstWindow()
    win.show()

    app.exec()