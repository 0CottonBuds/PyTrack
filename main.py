from gui import PytrackMainWindow
from PyTrackMain import PyTrackWorker

from PySide6.QtCore import QThread

class main(PytrackMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.pytrack_worker = PyTrackWorker(self)