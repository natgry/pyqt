from PySide6 import QtWidgets, QtCore


class LoginWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self) -> None:
        """
        Complete UI initialization
        :return: None
        """
        self.setWindowTitle("Login to application")
        size = QtCore.QSize(300, 200)
        self.setFixedSize(size)

        labelLogin = QtWidgets.QLabel()
        labelLogin.setMinimumWidth(50)
        labelLogin.setText("Login")

        labelPsw = QtWidgets.QLabel()
        labelPsw.setMinimumWidth(50)
        labelPsw.setText("Password")

        self.lineEditLogin = QtWidgets.QLineEdit()
        self.lineEditpsw = QtWidgets.QLineEdit()
        self.lineEditpsw.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.pushButtonRegister = QtWidgets.QPushButton()
        self.pushButtonRegister.setText("Register")

        self.pushButtonOk = QtWidgets.QPushButton()
        self.pushButtonOk.setText("OK")

        self.pushButtonCancel = QtWidgets.QPushButton()
        self.pushButtonCancel.setText("Cancel")

        # layouts
        layoutLogin = QtWidgets.QHBoxLayout()
        layoutLogin.addWidget(labelLogin)
        layoutLogin.addWidget(self.lineEditLogin)

        layoutPsw = QtWidgets.QHBoxLayout()
        layoutPsw.addWidget(labelPsw)
        layoutPsw.addWidget(self.lineEditpsw)

        layoutRegister = QtWidgets.QHBoxLayout()
        layoutRegister.addSpacerItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutRegister.addWidget(self.pushButtonRegister)

        layoutHandle = QtWidgets.QHBoxLayout()
        layoutHandle.addSpacerItem(
            QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Expanding)
        )
        layoutHandle.addWidget(self.pushButtonOk)
        layoutHandle.addWidget(self.pushButtonCancel)

        layoutMain = QtWidgets.QVBoxLayout()
        layoutMain.addLayout(layoutLogin)
        layoutMain.addLayout(layoutPsw)
        layoutMain.addLayout(layoutRegister)
        layoutMain.addLayout(layoutHandle)

        self.setLayout(layoutMain)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    win = LoginWindow()
    win.show()

    app.exec()
