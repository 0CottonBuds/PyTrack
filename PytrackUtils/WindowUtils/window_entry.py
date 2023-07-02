import sqlite3
import datetime as dt

from PytrackUtils.Helpers.database_helper import record_window_time


class WindowTimeEntries:
    """Takes Window Title, Time Started, Time Finished \n
    class for window entry that wil handle the data structure and entry of the data to the database
    """

    def __init__(self, window_name, time_elapsed):
        self.window_name = window_name
        self.time_elapsed = f"{time_elapsed[0]}, {time_elapsed[1]}, {time_elapsed[2]}"

    def record_in_database(self):
        record_window_time(self.window_name, self.time_elapsed)
        
