from UI.main.ui_main import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow


class PytrackMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pytrack")

        # setting the button signals to slots
        self.button_go_to_home.clicked.connect(self.go_to_home_page)  # type: ignore
        self.button_go_to_analytics.clicked.connect(self.go_to_analytics_page)  # type: ignore
        self.button_go_to_settings.clicked.connect(self.go_to_settings_page)  # type: ignore

        # show the window
        self.show()

    def go_to_home_page(self):
        print("to home page")

    def go_to_analytics_page(self):
        print("to analytics page")

    def go_to_settings_page(self):
        print("go to settings page")


if __name__ == "__main__":
    app = QApplication()
    window = PytrackMainWindow()
    app.exec()