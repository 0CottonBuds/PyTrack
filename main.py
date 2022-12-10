import pygetwindow as gw
import time
import datetime as dt
import entry
import window_type
import notification


class app:
    time_started: tuple
    time_finished: tuple

    def __init__(self):
        print("helloWorld")
        self.main()

    def main(self):
        self.last_active_window = None

        self.dt_now = dt.datetime.now()
        self.time_started = (self.dt_now.hour, self.dt_now.minute, self.dt_now.second)
        self.time_finished = (0, 0, 0)
        self.point_tracker = window_type.PointTracker()
        self.notification_handler = notification.NotificationHandler()

        while True:
            # get the active window
            self.new_active_window = gw.getActiveWindow()
            time.sleep(5)

            self.dt_now = dt.datetime.now()
            self.time_finished = (
                self.dt_now.hour,
                self.dt_now.minute,
                self.dt_now.second,
            )

            app_type = window_type.check_app_type(self.new_active_window)
            self.change_points(app_type)

            if self.point_tracker.points >= 15:
                self.notification_handler.take_a_break()
            if self.point_tracker.points <= -15:
                self.notification_handler.get_back_to_work()

            if self.new_active_window != self.last_active_window:
                """checks if window changed if it changes it records the data to the database if all prerequisite parameters exists \n \n
                time_finished and time_started\n
                last_active_window and new_active_window"""

                is_parameters_complete = (
                    self.time_finished is not None
                    and self.time_started is not None
                    and self.last_active_window is not None
                    and self.new_active_window is not None
                )
                if is_parameters_complete:

                    window_entry = entry.WindowEntryIn(
                        self.last_active_window.title,
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

    def change_points(self, app_type: str):
        """add and subtracts points based on app type"""

        if app_type == "good":
            self.point_tracker.add_points(5)
            print(f"added 5 points\ntotal points: {self.point_tracker.points}")
        elif app_type == "bad":
            self.point_tracker.subtract_points(5)
            print(f"subtract 5 points\ntotal points: {self.point_tracker.points}")
        else:
            print(self.new_active_window.title)
            print("this window does not have a label")

    def printer(self):
        """placeholder function to print some data in the terminal"""
        if self.time_finished is not None and self.time_started is not None:
            # app_type = check_app_type(self.last_active_window)
            elapsed_time = self.get_elapsed_time()
            print(elapsed_time)

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


if __name__ == "__main__":
    app1 = app()
