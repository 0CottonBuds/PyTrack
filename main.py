import pygetwindow as gw
import time
import datetime as dt
import entry


class app:
    time_started: tuple
    time_finished: tuple

    def __init__(self):
        print("helloWorld")
        self.run()

    # this is the main loop
    def run(self):
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
                        last_active_window.title, self.time_started, self.time_finished
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

        # get time elapsed from time started and time finished

    def get_elapsed_time(self) -> tuple:
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
        if seconds > 60:
            seconds -= 60
            minutes += 1
        if minutes > 60:
            minutes -= 60
            hours += 1

        time_spent = (hours, minutes, seconds)
        return time_spent


def check_app_type(last_active_window) -> str:
    productive_apps = ["Visual Studio Code"]
    bad_apps = ["Opera"]
    app_type = ""

    separated_title: list[str] = last_active_window.title.split("- ")
    for app in productive_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is an productive app {str(separated_title)}")
            app_type = "good"
    for app in bad_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is a bad app {str(separated_title)}")
            app_type = "bad"

    return app_type


if __name__ == "__main__":
    app1 = app()
