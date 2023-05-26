# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_monitor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(554, 600)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(16777215, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolBox = QToolBox(self.centralwidget)
        self.toolBox.setObjectName(u"toolBox")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setGeometry(QRect(0, 0, 536, 388))
        self.verticalLayout_8 = QVBoxLayout(self.page_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.plainTextEdit_3 = QPlainTextEdit(self.page_1)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")

        self.horizontalLayout_13.addWidget(self.plainTextEdit_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.toolBox.addItem(self.page_1, u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 536, 388))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget = QTableWidget(self.page_2)
        self.tableWidget.setObjectName(u"tableWidget")
        font = QFont()
        font.setPointSize(9)
        self.tableWidget.setFont(font)

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.toolBox.addItem(self.page_2, u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 536, 388))
        self.verticalLayout_10 = QVBoxLayout(self.page_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tableWidget_2 = QTableWidget(self.page_3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_10.addWidget(self.tableWidget_2)

        self.toolBox.addItem(self.page_3, u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 536, 388))
        self.verticalLayout_11 = QVBoxLayout(self.page_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.tableWidget_3 = QTableWidget(self.page_4)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_11.addWidget(self.tableWidget_3)

        self.toolBox.addItem(self.page_4, u"\u0417\u0430\u0434\u0430\u0447\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0430")

        self.verticalLayout.addWidget(self.toolBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(15, 0))

        self.horizontalLayout.addWidget(self.comboBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_2.addWidget(self.lineEdit_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 554, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SystemMonitor", None))
        self.plainTextEdit_3.setPlainText("")
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_1), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u0438\u0441\u0442\u0435\u043c\u0435", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0435 \u0441\u043b\u0443\u0436\u0431\u044b", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0438 \u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0449\u0438\u043a\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 (\u0441\u0435\u043a):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0432\u0440\u0435\u043c\u044f:", None))
    # retranslateUi

