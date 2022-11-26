import sqlite3
import datetime as dt


class WindowEntryIn():
    def __init__(self, windowTitle, timeStarted, timeFinished):
        self.windowTitle = windowTitle
        self.timeStarted = timeStarted
        self.timeFinished = timeFinished
        self.timeElapsed = self.convert_time_format()

    def record_in_database(self):

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


class WindowRecord():
    def __init__(self, entry):
        windowName: str = entry[0]
        timeElapsed: str = entry[1]
        dateEntried: str = entry[2]

        splitWindowName = windowName.split("- ")

        self.windowShortName: str = splitWindowName[-1]
        self.windowFullName: str = windowName
        self.windowTimeElapsed = WindowTimeElapsed(timeElapsed)
        self.windowDateEntried = dateEntried


class WindowTimeElapsed():
    def __init__(self, timeElapsed: str) -> None:
        splitTimeElapsed = timeElapsed.split(", ")

        self.hoursElapsed = splitTimeElapsed[0]
        self.minutesElapsed = splitTimeElapsed[1]
        self.secondsElapsed = splitTimeElapsed[2]


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


if __name__ == "__main__":
    retrieveEntries = retrieve_raw_entries()
    formattedEntries = format_raw_entries(retrieveEntries)
    print(formattedEntries[1].windowTimeElapsed.secondsElapsed)


# calculate how the time is being used
# next is to read all the data used in the data base
