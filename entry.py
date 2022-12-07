import sqlite3
import datetime as dt

import graphs

"""
all the code needs for entering data is in this block
"""
# class for window entry that wil handle the data structure and entry of the data to the database
class WindowEntryIn:
    def __init__(self, windowTitle, timeStarted, timeFinished):
        self.windowTitle = windowTitle
        self.timeStarted = timeStarted
        self.timeFinished = timeFinished
        self.timeElapsed = self.convertTimeFormat()

    def recordInDatabase(self):

        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute(
            """
                    INSERT INTO windowTimeEntries VALUES(?,?,?)

        """,
            (self.windowTitle, self.timeElapsed, str(dt.date.today())),
        )

        conn.commit()

        conn.close()

        print("successfully added to database")

    def convertTimeFormat(self):
        # minus the time started to time finished and convert it to a more readable format
        hours = self.timeFinished[0] - self.timeStarted[0]
        minutes = self.timeFinished[1] - self.timeStarted[1]
        seconds = self.timeFinished[2] - self.timeStarted[2]
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
        self.minutes += seconds
        self.seconds += minutes

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


# all in one class for window record needs
class WindowRecordUtils:
    def fetchEntries(self):
        return self.formatRawEntries(self.retrieveRawEntries())

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
    def getTotalTimeElapsed(self, formattedEntries: list[WindowRecord]) -> WindowTime:
        time = WindowTime(f"0, 0, 0")

        # cycle through the formatted entries and format the time
        for entry in formattedEntries:
            time.hours += entry.windowTimeElapsed.hours
            time.minutes += entry.windowTimeElapsed.minutes
            time.seconds += entry.windowTimeElapsed.seconds

            time.formatTime()

        # format and return time
        return time

    # get time elapsed on each window
    def getTimeOfEachWindow(
        self, formattedEntries: list[WindowRecord]
    ) -> list[WindowTime]:
        uniqueWindows: list[WindowTime] = []

        # loop through the entries
        for entry in formattedEntries:

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
                uniqueWindow.name = entry.windowShortName
                uniqueWindows.append(uniqueWindow)

        return uniqueWindows


if __name__ == "__main__":
    windowUtil = WindowRecordUtils()

    formattedRecords = windowUtil.fetchEntries()

    # for records in formattedRecords:
    #     print(records.windowTimeElapsed.get_time())

    totalTimeElapsed = windowUtil.getTotalTimeElapsed(formattedRecords)
    totalTimeOfEachWindow = windowUtil.getTimeOfEachWindow(formattedRecords)
    # print(totalTimeElapsed.getTime())

    for window in totalTimeOfEachWindow:
        print(window.name)
        print(window.getTime())
