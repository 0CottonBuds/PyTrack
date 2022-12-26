from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QObject, QThread
from ui_main import Ui_MainWindow

import threading

import sys

import time


class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTrack")
        self.worker = Worker()
        self.worker_thread = QThread()

        self.button_minimize.clicked.connect(self.worker.infinite_loop)  # type: ignore

        self.worker.moveToThread(self.worker_thread)
        self.worker_thread.start()

        # self.worker.infinite_loop()


class Worker(QObject):
    def __init__(self) -> None:
        super().__init__()

    def infinite_loop(self):
        cnt = 0
        print("button is clicked")
        while True:
            time.sleep(1)
            print("hello world")
            cnt += 0


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_Window = main()
    main_Window.show()
    app.exec()
