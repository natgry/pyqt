"""
Модуль, в котором содержатся потоки задач планировщика
"""
import time
import win32com.client

from typing import Optional
from PySide6 import QtCore


class TaskSchedulerInfo(QtCore.QThread):
    taskInfoReceived = QtCore.Signal(list)

    TASK_STATE = {0: 'Unknown',
                  1: 'Disabled',
                  2: 'Queued',
                  3: 'Ready',
                  4: 'Running'}

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None

    def get_task_info(self) -> Optional[list]:
        """
        Получение списка задач планировщика
        :return: список задач планировщика
        """
        task_info = []
        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        folders = [scheduler.GetFolder('\\')]
        while folders:
            folder = folders.pop(0)
            folders += list(folder.GetFolders(0))
            for task in folder.GetTasks(0):
                task_path = task.Path
                task_state = TaskSchedulerInfo.TASK_STATE[task.State]
                task_schedule = str(task.NextRunTime)
                task_info.append([task_path, task_state, task_schedule])
        return task_info

    def run(self) -> None:
        """
        Метод для запуска потока
        :return: None
        """
        if self.delay is None:
            self.delay = 1

        # запускаем бесконечный цикл получения информации о системе
        while True:
            task_info = self.get_task_info()
            self.systemSignal = task_info
            self.taskInfoReceived.emit(self.systemSignal)
            time.sleep(self.delay)
