from PySide6.QtWidgets import QMainWindow, QApplication
from ui_main import Ui_MainWindow

import threading

import sys


class main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTrack")
        # self.button_go_to_analytics.clicked.connect() #type: ignore


def infinite_loop():
    import time

    while True:
        time.sleep(2)
        print("Hello World")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_Window = main()
    main_Window.show()

    # app.exec()

    t1 = threading.Thread(target=infinite_loop)
    t1.run()
    t2 = threading.Thread(target=app.exec)
    t2.run()
