"""
Разработать приложение для мониторинга нагрузки системы и системных процессов (аналог диспетчера задач).

Обязательные функции в приложении:

1) Показ общих сведений о системе (в текстовом виде!):
 - Название процессора, количество ядер, текущая загрузка
 - Общий объём оперативной памяти, текущая загрузка оперативаной памяти
 - Количество, жестких дисков + информация по каждому (общий/занятый объём)
2) Обеспечить динамический выбор обновления информации (1, 5, 10, 30 сек.)
3) Показ работающих процессов
4) Показ работающих служб
5) Показ задач, которые запускаются с помощью планировщика задач
"""
from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem

from exam.threads.cpu_info_thread import SystemInfo
from exam.threads.proc_thread import ProcInfo
from exam.threads.time_thread import TimeInfo
from exam.threads.service_thread import ServiceInfo
from exam.threads.task_thread import TaskSchedulerInfo
from exam.ui.system_monitor import Ui_MainWindow


class SystemMonitorWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

        self.initThread()

        self.initSignals()

    def initUI(self) -> None:
        """
        Инициализация фронтенда.
        :return: None
        """
        self.ui.comboBox.insertItem(0, '1')
        self.ui.comboBox.insertItem(1, '5')
        self.ui.comboBox.insertItem(2, '15')
        self.ui.comboBox.insertItem(3, '30')

    def initThread(self) -> None:
        """
        Инициализация потоков

        :return: None
        """
        self.threadSystemInfo = SystemInfo()
        self.threadSystemInfo.start()

        self.threadProcInfo = ProcInfo()
        self.threadProcInfo.start()

        self.threadTimeInfo = TimeInfo()
        self.threadTimeInfo.start()

        self.threadServiceInfo = ServiceInfo()
        self.threadServiceInfo.start()

        self.threadTaskInfo = TaskSchedulerInfo()
        self.threadTaskInfo.start()

    def initSignals(self) -> None:
        """
        Инициализация сигналов
        :return: None
        """
        self.ui.comboBox.currentIndexChanged.connect(self.onComboBoxCurrentIndexChanged)
        self.threadSystemInfo.systemInfoReceived.connect(self.updateCpuRamInfo)
        self.threadProcInfo.procInfoReceived.connect(self.updateProcInfo)
        self.threadTimeInfo.timeInfoReceived.connect(self.updateTimeInfo)
        self.threadServiceInfo.serviceInfoReceived.connect(self.updateServiceInfo)
        self.threadTaskInfo.taskInfoReceived.connect(self.updateTaskInfo)

    def onComboBoxCurrentIndexChanged(self) -> None:
        """
        Обработка сигнала currentIndexChanged для поля comboBox

        :return: None
        """
        self.threadSystemInfo.delay = int(self.ui.comboBox.currentText())
        self.threadProcInfo.delay = int(self.ui.comboBox.currentText())
        self.threadServiceInfo.delay = int(self.ui.comboBox.currentText())
        self.threadTaskInfo.delay = int(self.ui.comboBox.currentText())

    def updateTaskInfo(self) -> None:
        """
        Обработка данных из потока threadTaskInfo

        :return: None
        """
        task_info = self.threadTaskInfo.systemSignal

        table = self.ui.tableWidget_3
        # Set the number of rows and columns in the table
        if task_info:
            table.setRowCount(len(task_info))
            table.setColumnCount(3)

            # Set the headers for the table
            table.setHorizontalHeaderLabels(['Task Name', 'State', 'Next Runtime'])

            # Populate the table with data
            i = 0
            for task in task_info:
                table.setItem(i, 0, QTableWidgetItem(str(task[0])))
                table.setItem(i, 1, QTableWidgetItem(task[1]))
                table.setItem(i, 2, QTableWidgetItem(task[2]))

                i += 1

            table.setStyleSheet('background-color: #F5F5F5;')

            table.show()

    def updateServiceInfo(self) -> None:
        """
        Обработка данных из потока threadServiceInfo

        :return: None
        """
        service_info = self.threadServiceInfo.systemSignal

        table = self.ui.tableWidget_2
        # Set the number of rows and columns in the table
        table.setRowCount(len(service_info))
        if service_info:
            headers = service_info[0].keys()
            table.setColumnCount(len(headers))
            # Set the headers for the table
            table.setHorizontalHeaderLabels(headers)

            # Populate the table with data
            i = 0
            for service in service_info:
                j = 0
                for item in service.values():
                    table.setItem(i, j, QTableWidgetItem(str(item)))
                    j += 1
                i += 1

            table.setStyleSheet('background-color: #F5F5F5;')

            table.show()

    def updateCpuRamInfo(self) -> None:
        """
        Обработка данных из потока threadSystemInfo

        :return: None
        """
        info = []

        cpu_info = self.threadSystemInfo.systemSignal[0]
        info.append(f"CPU:\n"
                    f"название процессора: {cpu_info.cpu_name}\n"
                    f"количество ядер: {cpu_info.cpu_count}\n"
                    f"текущая загрузка (%): {cpu_info.cpu_percent}")
        info.append("-------------------------------")
        ram_info = self.threadSystemInfo.systemSignal[1]
        info.append(f"RAM:\n"
                    f"общий объём оперативной памяти (bytes): {ram_info.ram_total}\n"
                    f"текущая загрузка оперативаной памяти (bytes): {ram_info.ram_used}")
        info.append("-------------------------------")
        disks_info = self.threadSystemInfo.systemSignal[2]
        info.append(f"DISKS:\n"
                    f"Количество жестких дисков: {disks_info.count}\n")
        for disk in disks_info.info:
            info.append(f"Диск: {disk.mountpoint}\n"
                        f"общий объём (bytes): {disk.total}\n"
                        f"занятый объём (bytes): {disk.used}\n")
        self.ui.plainTextEdit_3.setPlainText('\n'.join(info))

    def updateTimeInfo(self) -> None:
        """
        Обработка данных из потока threadTimeInfo

        :return: None
        """
        time_info = self.threadTimeInfo.systemSignal
        self.ui.lineEdit_5.setText(time_info)

    def updateProcInfo(self) -> None:
        """
        Обработка данных из потока threadSystemInfo

        :return: None
        """
        proc_info = self.threadProcInfo.systemSignal

        table = self.ui.tableWidget
        # Set the number of rows and columns in the table
        table.setRowCount(len(proc_info))
        table.setColumnCount(4)

        # Set the headers for the table
        table.setHorizontalHeaderLabels(['PID', 'Name', 'Status', 'Usage'])

        # Populate the table with data
        i = 0
        for p, info in proc_info.items():
            table.setItem(i, 0, QTableWidgetItem(str(p)))
            table.setItem(i, 1, QTableWidgetItem(info[0]))
            table.setItem(i, 2, QTableWidgetItem(info[1]))
            table.setItem(i, 3, QTableWidgetItem(str(info[2])))
            i += 1

        table.setStyleSheet('background-color: #F5F5F5;')

        table.show()

    def closeEvent(self, event) -> None:
        """
        Обработка события закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """
        self.threadSystemInfo.terminate()
        self.threadProcInfo.terminate()
        self.threadTimeInfo.terminate()
        self.threadServiceInfo.terminate()
        self.threadTaskInfo.terminate()
