# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_login_form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(280, 160)
        Form.setMinimumSize(QSize(280, 160))
        Form.setMaximumSize(QSize(280, 160))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 241, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLogin = QLabel(self.layoutWidget)
        self.labelLogin.setObjectName(u"labelLogin")
        self.labelLogin.setMinimumSize(QSize(50, 0))

        self.horizontalLayout.addWidget(self.labelLogin)

        self.lineEditLogin = QLineEdit(self.layoutWidget)
        self.lineEditLogin.setObjectName(u"lineEditLogin")

        self.horizontalLayout.addWidget(self.lineEditLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelPsw = QLabel(self.layoutWidget)
        self.labelPsw.setObjectName(u"labelPsw")
        self.labelPsw.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_2.addWidget(self.labelPsw)

        self.lineEditPsw = QLineEdit(self.layoutWidget)
        self.lineEditPsw.setObjectName(u"lineEditPsw")
        self.lineEditPsw.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout_2.addWidget(self.lineEditPsw)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButtonRegister = QPushButton(self.layoutWidget)
        self.pushButtonRegister.setObjectName(u"pushButtonRegister")

        self.horizontalLayout_3.addWidget(self.pushButtonRegister)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pushButtonOk = QPushButton(self.layoutWidget)
        self.pushButtonOk.setObjectName(u"pushButtonOk")

        self.horizontalLayout_4.addWidget(self.pushButtonOk)

        self.pushButtonCancel = QPushButton(self.layoutWidget)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_4.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelLogin.setText(QCoreApplication.translate("Form", u"Login", None))
        self.labelPsw.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButtonRegister.setText(QCoreApplication.translate("Form", u"Register", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Form", u"OK", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

