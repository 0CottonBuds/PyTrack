import sqlite3
import datetime as dt


class WindowEntryIn:
    """Takes Window Title, Time Started, Time Finished \n
    class for window entry that wil handle the data structure and entry of the data to the database
    """

    def __init__(self, window_title, time_elapsed):
        self.window_title = window_title
        self.time_elapsed = f"{time_elapsed[0]}, {time_elapsed[1]}, {time_elapsed[2]}"

    def record_in_database(self):
        """enter the data to data base"""
        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS windowTimeEntries(windowName text, timeElapsed text, date text)""")

        today = dt.date.today()
        today = [today.year, today.month, today.day]
        date_string = f"{today[0]}-{today[1]}-{today[2]}"

        c.execute(
            """INSERT INTO windowTimeEntries VALUES(?,?,?)""",
            (self.window_title, str(self.time_elapsed), date_string),
        )

        conn.commit()

        conn.close()

        print("successfully added to database")
