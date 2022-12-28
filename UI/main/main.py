from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QThread
from ui_main import Ui_MainWindow

import PySide6.QtGui

import threading

import sys

import time


class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTrack")
        self.worker = Worker(self)
        self.worker_thread = QThread()

        self.run = False

        self.button_minimize.clicked.connect(self.worker.infinite_loop)  # type: ignore
        self.button_minimize.clicked.connect(self.infinite_loop_runner)  # type: ignore

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.start()

    def infinite_loop_runner(self):
        if not self.run:
            self.run = True
            print("turning On")
        elif self.run:
            self.run = False
            print("turning Off")


class Worker(QObject):
    def __init__(self, main_window: main) -> None:
        super().__init__()
        self.main_window = main_window

    def infinite_loop(self):
        print("button is clicked")

        while self.main_window.run:
            time.sleep(2)
            print("hello world")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_Window = main()
    main_Window.show()
    # main_Window.worker.infinite_loop()
    app.exec()
