"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui

from hw_2.b_hw.ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.qSettings = QtCore.QSettings("MyApp")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
        self.initSignals()

    def initUI(self):
        """
        Доинициализация Ui

        :return: None
        """
        settings = self.qSettings.value("settings_list", [])

        self.ui.comboBox.insertItem(0, 'oct')
        self.ui.comboBox.insertItem(1, 'hex')
        self.ui.comboBox.insertItem(2, 'bin')
        self.ui.comboBox.insertItem(3, 'dec')
        if settings:
            self.ui.comboBox.setCurrentIndex(int(settings[0]))
            #self.lcdNumberSetMode()

            lcdNumber = int(settings[1])
            self.ui.lcdNumber.display(lcdNumber)
            self.ui.horizontalSlider.setValue(lcdNumber)
            self.ui.dial.setValue(lcdNumber)
        self.lcdNumberSetMode()
        self.ui.dial.installEventFilter(self)

    def initSignals(self):
        """
        Инициализация сигналов

        :return: None
        """
        self.ui.horizontalSlider.valueChanged.connect(self.onHorizontalSliderValueChanged)
        self.ui.comboBox.currentIndexChanged.connect(self.onComboBoxCurrentIndexChanged)
        self.ui.dial.valueChanged.connect(self.onDialValueChanged)

    def onDialValueChanged(self) -> None:
        """
        Обработка сигнала valueChanged для QDial dial

        :return: None
        """
        value = self.ui.dial.value()
        self.ui.lcdNumber.display(value)
        self.ui.horizontalSlider.setValue(value)

    def onComboBoxCurrentIndexChanged(self) -> None:
        """
        Обработка сигнала currentIndexChanged для QComboBox comboBox

        :return: None
        """
        self.lcdNumberSetMode()

    def lcdNumberSetMode(self) -> None:
        """
        Установка формата отображаемого значения для QLCDNumber
        в зависимости от выбранного в comboBox параметра

        :return: None
        """
        if self.ui.comboBox.currentText() == 'oct':
            self.ui.lcdNumber.setOctMode()
        elif self.ui.comboBox.currentText() == 'hex':
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText() == 'bin':
            self.ui.lcdNumber.setBinMode()
        elif self.ui.comboBox.currentText() == 'dec':
            self.ui.lcdNumber.setDecMode()

    def onHorizontalSliderValueChanged(self) -> None:
        """
        Обработка сигнала valueChanged для слайдера horizontalSlider

        :return: None
        """
        value = self.ui.horizontalSlider.value()
        self.ui.lcdNumber.display(value)
        self.ui.dial.setValue(value)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Обработка событий закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.qSettings.setValue(
            "settings_list", [self.ui.comboBox.currentIndex(), self.ui.lcdNumber.value()]
        )

    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Настройка дополнительного поведения виджетов

        :param source: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """
        if source == self.ui.dial and event.type() == QtCore.QEvent.Type.KeyPress:
            current_value = self.ui.dial.value()
            new_value = current_value

            if event.key() == QtCore.Qt.Key.Key_Plus:
                new_value = current_value + 1

            if event.key() == QtCore.Qt.Key.Key_Minus:
                new_value = current_value - 1

            if current_value != new_value:
                self.ui.dial.setValue(new_value)
                print(f"Old dial value: {current_value}, New dial value: {self.ui.dial.value()}")

        return super().eventFilter(source, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
