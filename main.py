import pygetwindow as gw
import time
import datetime as dt
import entry
from window_type import check_app_type


class app:
    time_started: tuple
    time_finished: tuple

    def __init__(self):
        print("helloWorld")
        self.main()

    def main(self):
        last_active_window = None

        dt_now = dt.datetime.now()
        self.time_started = (dt_now.hour, dt_now.minute, dt_now.second)
        self.time_finished = (0, 0, 0)

        while True:
            # get the active window
            new_active_window = gw.getActiveWindow()
            time.sleep(5)

            dt_now = dt.datetime.now()
            self.time_finished = (dt_now.hour, dt_now.minute, dt_now.second)

            # if the window changed
            if new_active_window != last_active_window:
                # if there is both time started and finished this means that we changed from another window
                # to another in this case we will record it on the database
                if (
                    self.time_finished is not None
                    and self.time_started is not None
                    and last_active_window is not None
                ):

                    window_entry = entry.WindowEntryIn(
                        last_active_window.title, self.get_elapsed_time()
                    )
                    window_entry.record_in_database()

                # set the last active window to the current window
                last_active_window = new_active_window

                self.time_started = (dt_now.hour, dt_now.minute, dt_now.second)

            # check if the window app is productive or not
            if last_active_window is not None:
                app_type = check_app_type(last_active_window)
                if self.time_finished is not None and self.time_started is not None:
                    elapsed_time = self.get_elapsed_time()
                    print(elapsed_time)

            else:
                last_active_window = new_active_window

    def get_elapsed_time(self) -> tuple:
        """function to subtract two time(hours, minutes, seconds)\n
        returns tuple(Hours, Minutes, Seconds)\n
        check TODO to see bugs"""

        # TODO: fix bug that make this function act weird when we are subtracting from another 12 hour cycle i.e.: 11pm - 12am(00:00) which results this function to make large numbers i.e.: -23,-58,-30

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

        time_spent = (hours, minutes, seconds)
        return time_spent


if __name__ == "__main__":
    app1 = app()
