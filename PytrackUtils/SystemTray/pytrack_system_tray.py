from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon

class PytrackSystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon: QIcon, parent: QObject = None):
        super(PytrackSystemTrayIcon, self).__init__(icon, parent)

        menu = QMenu()


        self.showMessage("PyTrack", "This is a system tray for pytrack")
        self.setContextMenu(menu)
        self.show()


if __name__ == "__main__":
    system_tray_icon = QIcon("Icons\icon.ico")

    if QSystemTrayIcon.isSystemTrayAvailable():
        tray = PytrackSystemTrayIcon(system_tray_icon) 