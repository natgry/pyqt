from PySide6 import QtWidgets

from hw_1.ui.a_add_ui_form import Ui_MainWindow


class TrainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

    def initUI(self) -> None:
        """
        Complete UI initialization
        :return: None
        """
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = TrainWindow()
    win.show()

    app.exec()
