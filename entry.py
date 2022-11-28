import sqlite3
import datetime as dt

# all the code needs for entrying data is in this block


class WindowEntryIn():
    def __init__(self, windowTitle, timeStarted, timeFinished):
        self.windowTitle = windowTitle
        self.timeStarted = timeStarted
        self.timeFinished = timeFinished
        self.timeElapsed = self.convert_time_format()

    def recordInDatabase(self):

        conn = sqlite3.connect("pyTrack.db")

        c = conn.cursor()

        c.execute("""
                    INSERT INTO windowTimeEntries VALUES(?,?,?)

        """, (self.windowTitle, self.timeElapsed, str(dt.date.today())))

        conn.commit()

        conn.close()

        print("successfully added to database")

    def convert_time_format(self):
        # minus the time started to time finished and convert it to a more readable format
        hours = self.timeFinished[0] - self.timeStarted[0]
        minutes = self.timeFinished[1] - self.timeStarted[1]
        seconds = self.timeFinished[2] - self.timeStarted[2]
        timeElapsed = f"{hours}, {minutes}, {seconds}"
        return timeElapsed


# all the code need for querying processing and showing the data in this block

# clss window record to handle and store data that is retrieved from the database
class WindowRecord():
    def __init__(self, entry):
        windowName: str = entry[0]
        timeElapsed: str = entry[1]
        dateEntried: str = entry[2]

        splitWindowName = windowName.split("- ")

        self.windowShortName: str = splitWindowName[-1]
        self.windowFullName: str = windowName
        self.windowTimeElapsed = WindowTime(timeElapsed)
        self.windowDateEntried = dateEntried


# class window time for keeping data(time)
class WindowTime():
    name: str

    def __init__(self, timeElapsed: str) -> None:
        splitTimeElapsed = timeElapsed.split(", ")

        self.hours: float = float(splitTimeElapsed[0])
        self.minutes: float = float(splitTimeElapsed[1])
        self.seconds: float = float(splitTimeElapsed[2])

    def get_time(self) -> tuple:
        time = (self.hours, self.minutes, self.seconds)
        return time

    def add_time(self, hours=0, minutes=0, seconds=0):
        self.hours += hours
        self.minutes += seconds
        self.seconds += minutes

        if self.seconds >= 61:
            self.seconds -= 60
            self.minutes += 1
        if self.minutes >= 61:
            self.minutes -= 60
            self.hours += 1


# format raw entry list output is a list of Class WindowRecord
def format_raw_entries(rawEntries: list) -> list[WindowRecord]:
    formattedEntries = []
    for entry in rawEntries:
        record = WindowRecord(entry)
        formattedEntries.append(record)
    return formattedEntries


# get all entries as raw list
def retrieve_raw_entries(q=None):
    conn = sqlite3.connect("pyTrack.db")

    c = conn.cursor()

    c.execute("SELECT * FROM windowTimeEntries")

    rawEntries = c.fetchall()

    conn.commit()
    conn.close

    return rawEntries


# get total time elapsed
def get_total_time_elapsed(formattedEntries: list[WindowRecord]) -> WindowTime:
    hours = 0
    minutes = 0
    seconds = 0

    # cycle through the formatted entries and format the time
    for entry in formattedEntries:
        hours += entry.windowTimeElapsed.hours
        minutes += entry.windowTimeElapsed.minutes

        if minutes >= 61:
            minutes -= 60
            hours += 1
        seconds += entry.windowTimeElapsed.seconds
        if seconds >= 61:
            seconds -= 60
            minutes += 1

    # format and return time
    time = WindowTime(f"{hours}, {minutes}, {seconds}")
    return time


# get time elapsed on each windoww
def get_time_of_each_window(formattedEntries: list[WindowRecord]) -> list[WindowTime]:
    uniqueWindows: list[WindowTime] = []

    # loop through the entries
    for entry in formattedEntries:

        # loop through the unique window list find if there is a match or not
        isUnique: bool = True
        for window in uniqueWindows:
            # if unique add time elapsed to the object that it matched
            if window.name == entry.windowShortName:
                isUnique = False
                timeToAdd = entry.windowTimeElapsed.get_time()
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
    retrieveEntries = retrieve_raw_entries()
    formattedEntries = format_raw_entries(retrieveEntries)
    totalTimeElapsed = get_total_time_elapsed(formattedEntries)
    totalTimeOfEachWindow = get_time_of_each_window(formattedEntries)
    print(totalTimeElapsed.get_time)

    for time in totalTimeOfEachWindow:
        print(f"name:{time.name} time:{time.get_time()}")
