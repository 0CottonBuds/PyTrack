import sqlite3
import datetime as dt

from typing import Protocol

# all the code needs for entering data is in this block
class WindowEntryIn:
    """Takes Window Title, Time Started, Time Finished \n
    class for window entry that wil handle the data structure and entry of the data to the database
    """

    def __init__(self, window_title, time_started, time_finished):
        self.window_title = window_title
        self.time_started = time_started
        self.time_finished = time_finished
        self.time_elapsed = self.convertTimeFormat()

    def record_in_database(self):
        """enter the data to data base"""
        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute(
            """
                    INSERT INTO windowTimeEntries VALUES(?,?,?)

        """,
            (self.window_title, self.time_elapsed, str(dt.date.today())),
        )

        conn.commit()

        conn.close()

        print("successfully added to database")

    def convertTimeFormat(self):
        """subtracts the time started and time finished to get time elapsed"""
        hours = self.time_finished[0] - self.time_started[0]
        minutes = self.time_finished[1] - self.time_started[1]
        seconds = self.time_finished[2] - self.time_started[2]
        timeElapsed = f"{hours}, {minutes}, {seconds}"
        return timeElapsed


"""
all the code need for querying processing and showing the data in this block
"""
# class window record to handle and store data that is retrieved from the database
class WindowRecord:
    def __init__(self, entry):
        windowName: str = entry[0]
        timeElapsed: str = entry[1]
        dateEntered: str = entry[2]

        splitWindowName = windowName.split("- ")

        self.windowShortName: str = splitWindowName[-1]
        self.windowFullName: str = windowName
        self.windowTimeElapsed = WindowTime(timeElapsed)
        self.windowDateEntered = dateEntered


# class window time for keeping data(time)
class WindowTime:
    name: str
    fullName: str

    def __init__(self, timeElapsed: str) -> None:
        splitTimeElapsed = timeElapsed.split(", ")

        self.hours: float = float(splitTimeElapsed[0])
        self.minutes: float = float(splitTimeElapsed[1])
        self.seconds: float = float(splitTimeElapsed[2])

        self.formatTime()

    def getTime(self) -> tuple:
        self.formatTime()
        time = (self.hours, self.minutes, self.seconds)
        return time

    def add_time(self, hours=0, minutes=0, seconds=0):
        self.formatTime()

        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds

        self.formatTime()

    def formatTime(self):
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


# all in one class for window record needs
class WindowRecordUtils:
    formattedRecords = []

    def __init__(self) -> None:
        self.fetchEntries()

    def fetchEntries(self):
        self.formattedRecords = self.formatRawEntries(self.retrieveRawEntries())

    # format raw entry list output is a list of Class WindowRecord
    def formatRawEntries(self, rawEntries: list) -> list[WindowRecord]:
        formattedEntries = []
        for entry in rawEntries:
            record = WindowRecord(entry)
            formattedEntries.append(record)
        return formattedEntries

    # get all entries as raw list
    def retrieveRawEntries(self, q=None) -> list:
        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute("SELECT * FROM windowTimeEntries")

        rawEntries = c.fetchall()

        conn.commit()
        conn.close

        return rawEntries

    # get total time elapsed
    def getTotalTimeElapsed(self) -> WindowTime:
        time = WindowTime(f"0, 0, 0")

        # cycle through the formatted entries and format the time
        for entry in self.formattedRecords:
            time.hours += entry.windowTimeElapsed.hours
            time.minutes += entry.windowTimeElapsed.minutes
            time.seconds += entry.windowTimeElapsed.seconds

            time.formatTime()

        # format and return time
        return time

    # get time elapsed on each window
    def getTimeOfEachWindow(self):
        uniqueWindows: list[WindowTime] = []

        # loop through the entries
        for entry in self.formattedRecords:

            # loop through the unique window list find if there is a match or not
            isUnique: bool = True
            for window in uniqueWindows:
                # if unique add time elapsed to the object that it matched
                if window.name == entry.windowShortName:
                    isUnique = False
                    timeToAdd = entry.windowTimeElapsed.getTime()
                    window.add_time(timeToAdd[0], timeToAdd[1], timeToAdd[2])
                else:
                    pass

            # if unique then add a new item in the list
            if isUnique:
                uniqueWindow = entry.windowTimeElapsed
                uniqueWindow.fullName = entry.windowFullName
                uniqueWindow.name = entry.windowShortName
                uniqueWindows.append(uniqueWindow)

        return uniqueWindows

    def getPercentageOfTimeOfEachWindow(self):
        totalTime = self.getTotalTimeElapsed()
        timeOfEachWindow = self.getTimeOfEachWindow()

        percentages: list[list] = []

        for window in timeOfEachWindow:
            percentage = window.seconds / totalTime.seconds
            percentage = percentage + window.minutes
            percentage = percentage / totalTime.minutes
            percentage = percentage + window.hours
            percentage = percentage / totalTime.hours
            percentage = percentage * 100

            percentages.append([window, round(percentage, 2)])

        return percentages


if __name__ == "__main__":
    windowUtil = WindowRecordUtils()

    totalTimeElapsed = windowUtil.getTotalTimeElapsed()
    print(totalTimeElapsed.getTime())
    print()

    totalTimeOfEachWindow = windowUtil.getTimeOfEachWindow()

    percentageTimeOfEachWindow = windowUtil.getPercentageOfTimeOfEachWindow()

    for window in percentageTimeOfEachWindow:
        print(f"name: {window[0].fullName}")
        print(f"percentage: {window[1]}")
