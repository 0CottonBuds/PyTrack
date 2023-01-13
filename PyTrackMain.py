from PySide6.QtCharts import QLineSeries
import pygetwindow as gw
import time
import datetime as dt
from PytrackUtils import entry, point_tracker, window_type

from PySide6.QtCore import QObject, Signal


class PyTrackWorker(QObject):
    time_started: tuple
    time_finished: tuple

    def __init__(self, main_window):
        super().__init__()
        print("helloWorld")

        self.main_window = main_window

        self.last_active_window = None
        self.dt_now = dt.datetime.now()
        self.time_started = (self.dt_now.hour, self.dt_now.minute, self.dt_now.second)
        self.time_finished = (0, 0, 0)
        self.point_tracker = point_tracker.PointTracker()

        # self.main_loop()

    def main_loop(self):
        while self.main_window.main_loop_active:
            time.sleep(5)
            # get the active windows
            self.new_active_window = gw.getActiveWindow()

            self.dt_now = dt.datetime.now()
            self.time_finished = (
                self.dt_now.hour,
                self.dt_now.minute,
                self.dt_now.second,
            )

            # check app type and change points
            window = window_type.WindowType()
            window.window_name = self.new_active_window.title  # type: ignore
            window.check_app_type()
            self.point_tracker.change_points(window)
            self.point_tracker.check_point_threshold()

            print(f"Active Window: {window}")
            print(self.point_tracker)
            self.main_window.label_points_home.setText(str(self.point_tracker))

            if self.new_active_window != self.last_active_window:
                """checks if window changed if it changes it records the data to the
                database if all prerequisite parameters exists
                time_finished and time_started
                last_active_window and new_active_window"""

                is_parameters_complete = (
                    self.time_finished is not None
                    and self.time_started is not None
                    and self.last_active_window is not None
                    and self.new_active_window is not None
                )
                if is_parameters_complete:

                    window_entry = entry.WindowEntryIn(
                        self.last_active_window.title,  # type: ignore
                        self.get_elapsed_time(),
                    )
                    window_entry.record_in_database()

                # set the last active window to the current window
                self.last_active_window = self.new_active_window

                self.time_started = (
                    self.dt_now.hour,
                    self.dt_now.minute,
                    self.dt_now.second,
                )

            self.check_if_last_window_exists()

            self.printer()

    def check_if_last_window_exists(self):
        """checks if last window is none if yes then set it to the new active window"""
        if self.last_active_window is None:
            self.last_active_window = self.new_active_window

    def get_elapsed_time(self) -> tuple:
        """function to subtract two time(hours, minutes, seconds)\n
        returns tuple(Hours, Minutes, Seconds)\n
        check TODO to see bugs"""

        """ TODO: fix bug that make this function act weird when we are subtracting from another 12 hour cycle i.e.: 11pm - 12am(00:00) which results this function to make large numbers i.e.: -23,-58,-30"""

        hours: float = self.time_finished[0] - self.time_started[0]
        minutes: float = self.time_finished[1] - self.time_started[1]
        seconds: float = self.time_finished[2] - self.time_started[2]

        # check if the time became negative and compensate
        if seconds < 0:
            minutes -= 1
            seconds += 60
        if minutes < 0:
            hours -= 1
            minutes += 60

        time_elapsed = (hours, minutes, seconds)
        return time_elapsed

    def printer(self):
        """placeholder function to print some data in the terminal"""
        if self.time_finished is not None and self.time_started is not None:
            # app_type = check_app_type(self.last_active_window)
            elapsed_time = self.get_elapsed_time()
            print(elapsed_time)


class PointChecker(QObject):
    looped = Signal()

    def __init__(self, main_window) -> None:
        super().__init__()
        self.line_series = QLineSeries()
        self.main_window = main_window

    def point_checking_loop(self):
        points: list[int] = []
        print("starting")
        while self.main_window.main_loop_active:
            print("looped")
            time.sleep(300)
            print("checking the points")
            new_point = self.main_window.pytrack_worker.point_tracker.points
            points.append(new_point)
            self.line_series.append(len(points), int(new_point / 10))
            self.looped.emit()


# if __name__ == "__main__":
#     app1 = PyTrack()
