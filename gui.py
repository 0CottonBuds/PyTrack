from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread

from UI.main import icons_rc
from UI.main.ui_main import Ui_MainWindow

from PyTrackMain import PyTrackWorker


class PytrackMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytrack")
        self.main_loop_active = False

        self.pytrack_worker = PyTrackWorker(self)
        self.pytrack_worker_thread = QThread()

        self.button_activate_deactivate_main_loop.setText("Activate")

        # setting the button signals to slots
        self.button_go_to_home.clicked.connect(self.go_to_home_page)  # type: ignore
        self.button_go_to_analytics.clicked.connect(self.go_to_analytics_page)  # type: ignore
        self.button_go_to_settings.clicked.connect(self.go_to_settings_page)  # type: ignore
        self.button_activate_deactivate_main_loop.clicked.connect(self.activate_deactivate_main_loop)  # type: ignore
        self.button_activate_deactivate_main_loop.clicked.connect(self.pytrack_worker.main_loop)  # type: ignore

        # move workers to their threads and start the threads
        self.pytrack_worker.moveToThread(self.pytrack_worker_thread)
        self.pytrack_worker_thread.start()

        # show the window
        self.show()

    def go_to_home_page(self):
        print("to home page")
        self.stackedWidget.setCurrentWidget(self.page_home)

    def go_to_analytics_page(self):
        print("to analytics page")
        self.stackedWidget.setCurrentWidget(self.page_analytics)

    def go_to_settings_page(self):
        print("go to settings page")
        self.stackedWidget.setCurrentWidget(self.page_settings)

    def activate_deactivate_main_loop(self):
        if not self.main_loop_active:
            print("Activated")
            self.main_loop_active = True
            self.button_activate_deactivate_main_loop.setText("Deactivate")
        elif self.main_loop_active:
            print("Deactivated")
            self.main_loop_active = False
            self.button_activate_deactivate_main_loop.setText("Activate")


if __name__ == "__main__":
    app = QApplication()
    window = PytrackMainWindow()
    app.exec()
