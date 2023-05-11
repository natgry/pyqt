"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        settings = QtCore.QSettings("MyApp")
        self.plainTextEdit = QtWidgets.QPlainTextEdit()
        self.plainTextEdit.setPlainText(settings.value("text", ""))

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.plainTextEdit)

        self.setLayout(layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        print("close event method when window is closed")

        settings = QtCore.QSettings("MyApp")
        settings.setValue("text", self.plainTextEdit.toPlainText())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()

