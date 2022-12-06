import pygetwindow as gw
import time
import datetime as dt
import entry


class app():
    def __init__(self) -> None:
        print("helloWorld")
        self.run()


    # this is the main loop
    def run(self):
        lastActiveWindow = None

        dtNow = dt.datetime.now()
        timeStarted = (dtNow.hour, dtNow.minute, dtNow.second)
        timeFinished = None

        while True:
            # get the active window
            newActiveWindow = gw.getActiveWindow()
            time.sleep(5)

            dtNow = dt.datetime.now()
            timeFinished = (dtNow.hour, dtNow.minute, dtNow.second)

            # if the window changed
            if newActiveWindow != lastActiveWindow:
                # if there is both time started and finished this means that we changed from another window
                # to another in this case we will record it on the database
                if timeFinished is not None and timeStarted is not None and lastActiveWindow is not None:
                    windowEntry = entry.WindowEntryIn(lastActiveWindow.title,
                                                      timeStarted, timeFinished)
                    windowEntry.recordInDatabase()

                # set the last active window to the current window
                lastActiveWindow = newActiveWindow

                timeStarted = (dtNow.hour, dtNow.minute, dtNow.second)

            # check if the window app is productive or not
            if lastActiveWindow is not None:
                appType = checkAppType(lastActiveWindow)
                if timeFinished is not None and timeStarted is not None:
                    elapsedTime = getElapsedTime(timeStarted, timeFinished)
                    print(elapsedTime)

            else:
                lastActiveWindow = newActiveWindow


def checkAppType(lastActiveWindow) -> str:
    productiveApps = ["Visual Studio Code"]
    badApps = ["Opera"]
    appType = ""

    separatedTitle: list = lastActiveWindow.title.split("- ")
    for app in productiveApps:
        if separatedTitle[-1].upper() == app.upper():
            print(f"this is an productive app {str(separatedTitle)}")
            appType = "good"
    for app in badApps:
        if separatedTitle[-1].upper() == app.upper():
            print(f"this is a bad app {str(separatedTitle)}")
            appType = "bad"

    return appType


# get time elapsed from time started and time finished
def getElapsedTime(timeStarted, timeFinished) -> tuple:
    hours: float = timeFinished[0] - timeStarted[0]
    minutes: float = timeFinished[1] - timeStarted[1]
    seconds: float = timeFinished[2] - timeStarted[2]

    # check if the time became negative and compensate
    if seconds < 0:
        minutes -= 1
        seconds += 60
    if minutes < 0:
        hours -= 1
        minutes += 60

    timeSpent = (hours, minutes, seconds)
    return timeSpent


if __name__ == "__main__":
    app1 = app()
