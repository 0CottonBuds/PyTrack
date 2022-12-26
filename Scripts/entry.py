import sqlite3
import datetime as dt

# from .Scripts import notification


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

        c.execute(
            """INSERT INTO windowTimeEntries VALUES(?,?,?)""",
            (self.window_title, str(self.time_elapsed), str(dt.date.today())),
        )

        conn.commit()

        conn.close()

        print("successfully added to database")


# all the code need for querying processing and showing the data in this block


class WindowRecord:
    """class to handle and store data that is retrieved from the database"""

    def __init__(self, entry):
        window_name: str = entry[0]
        time_elapsed: str = entry[1]
        date_entered: str = entry[2]

        split_window_name = window_name.split("- ")

        self.window_short_name: str = split_window_name[-1]
        self.window_full_name: str = window_name
        self.window_time_elapsed = WindowTime(time_elapsed)
        self.window_date_entered = date_entered


class WindowTime:
    """class window time for keeping data(time)"""

    name: str
    full_name: str

    def __init__(self, time_elapsed: str) -> None:
        split_time_elapsed = time_elapsed.split(", ")

        self.hours: float = float(split_time_elapsed[0])
        self.minutes: float = float(split_time_elapsed[1])
        self.seconds: float = float(split_time_elapsed[2])

        self.format_time()

    def get_time(self) -> tuple:
        """returns tuple of time"""
        self.format_time()
        time = (self.hours, self.minutes, self.seconds)
        return time

    def format_time(self):
        """formats the time to avoid the negatives and time going above 60 \n use this when changing the time value"""
        if self.minutes > 60:
            self.minutes -= 60
            self.hours += 1
        if self.seconds > 60:
            self.seconds -= 60
            self.minutes += 1
        if self.seconds < 0:
            self.seconds += 60
        if self.minutes < 0:
            self.minutes += 60

    def __add__(self, other: "WindowTime") -> "WindowTime":
        self.hours = self.hours + other.hours
        self.minutes = self.minutes + other.minutes
        self.seconds = self.seconds + other.seconds

        self.format_time()

        return WindowTime(f"{self.hours}, {self.minutes}, {self.seconds}")


class WindowRecordFetcher:
    """Class that fetches the data and formats it\n
    -> list[WindowRecords]"""

    formatted_records = []

    def __init__(self) -> None:
        self.fetch_all_records()

    def fetch_all_records(self):
        """combination of format_raw_entries and retrieve_raw_entries as one function"""
        self.formatted_records = self.format_records(self.retrieve_all_raw_records())

    def fetch_records_by_date(self, date: str):
        """combination of format_raw_entries and retrieve_raw_entries as one function but with dates"""
        self.formatted_records = self.format_records(
            self.retrieve_all_raw_records_by_date(date)
        )

    def format_records(self, raw_records: list) -> list[WindowRecord]:
        """Method for formatting records as `WindowRecord` objects"""
        formatted_records = []
        for entry in raw_records:
            record = WindowRecord(entry)
            formatted_records.append(record)
        return formatted_records

    def retrieve_all_raw_records(self) -> list:
        """Method for retrieving all raw records from the database"""
        conn = sqlite3.connect("pyTrack.db")
        c = conn.cursor()
        c.execute("SELECT * FROM windowTimeEntries")
        raw_records = c.fetchall()
        conn.commit()
        conn.close
        return raw_records

    def retrieve_all_raw_records_by_date(self, date: str) -> list:
        """Method for retrieving raw records from the database by date"""
        conn = sqlite3.connect("pyTrack.db")
        c = conn.cursor()
        c.execute("SELECT * FROM windowTimeEntries WHERE date = ?", (date,))
        raw_records = c.fetchall()
        conn.commit()
        conn.close
        return raw_records

    def __str__(self) -> str:
        message = ""

        for records in self.formatted_records:
            message += f"{records.window_full_name}, {records.window_time_elapsed.get_time()} \n"
        return message


def get_total_time_elapsed(formatted_records: list[WindowRecord]) -> WindowTime:
    """Calculate the total time elapsed.

    Args:
        formatted_records: A list of window records.

    Returns:
        The total time elapsed as a WindowTime object.
    """
    total_time = WindowTime(f"0, 0, 0")

    # Iterate over the records and add the elapsed time for each record to the total time.
    for entry in formatted_records:
        total_time += entry.window_time_elapsed
    return total_time


def get_time_of_each_window(formatted_records: list[WindowRecord]) -> list[WindowTime]:
    """get time elapsed on each window"""
    unique_windows: list[WindowTime] = []

    # loop through the entries
    for entry in formatted_records:

        # loop through the unique window list find if there is a match or not
        is_unique: bool = True
        for window in unique_windows:
            # if unique add time elapsed to the object that it matched
            if window.name == entry.window_short_name:
                is_unique = False
                window += entry.window_time_elapsed
            else:
                pass

        # if unique then add a new item in the list
        if is_unique:
            unique_window = entry.window_time_elapsed
            unique_window.full_name = entry.window_full_name
            unique_window.name = entry.window_short_name
            unique_windows.append(unique_window)

    return unique_windows


def get_percentage_of_time_of_each_window(formatted_records: list[WindowRecord]):
    """returns list of window and percentage"""
    total_time = get_total_time_elapsed(formatted_records)
    time_of_each_window = get_time_of_each_window(formatted_records)

    total_time_in_seconds = total_time.hours * 3600
    total_time_in_seconds += total_time.minutes * 60
    total_time_in_seconds += total_time.seconds

    percentages: list[list] = []

    for window in time_of_each_window:
        percentage = 0

        window_time_in_seconds = window.hours * 3600
        window_time_in_seconds += window.minutes * 60
        window_time_in_seconds += window.seconds

        percentage = window_time_in_seconds / total_time_in_seconds
        percentage = percentage * 100

        percentages.append([window, round(percentage, 2)])

    return percentages


if __name__ == "__main__":
    records = WindowRecordFetcher().formatted_records
    # print(records)

    total_time_elapsed = get_total_time_elapsed(records)
    print(total_time_elapsed.get_time())
    print()

    time_of_each_window = get_time_of_each_window(records)

    for window in time_of_each_window:
        print(window.full_name)
        print(window.get_time())

    percentage_time_of_each_window = get_percentage_of_time_of_each_window(records)

    full_percentage = 0
    for window in percentage_time_of_each_window:
        print(f"name: {window[0].full_name}")
        print(f"percentage: {window[1]}")
        full_percentage += window[1]
    # print(full_percentage)
