import pygetwindow as gw
import time
import datetime as dt
import entry


# this is the main loop
def main():
    lastActiveWindow = None
    timeStarted = None
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
                windowEntry = entry.WindowEntry(lastActiveWindow.title,
                                                timeStarted, timeFinished)
                windowEntry.record_in_database()

            # set the last active window to the current window
            lastActiveWindow = newActiveWindow

            timeStarted = (dtNow.hour, dtNow.minute, dtNow.second)

        # check if the windo/app is productive or not
        if lastActiveWindow is not None:
            appType = check_app_type(lastActiveWindow)
            elapsedTime = getElapsedTime(timeStarted, timeFinished)
            print(elapsedTime)

        else:
            pass


def check_app_type(lastActiveWindow) -> str:
    productiveApps = ["Visual Studio Code"]
    badApps = ["Opera"]
    appType = ""

    seperatedTitle: list = lastActiveWindow.title.split("- ")
    for app in productiveApps:
        if seperatedTitle[-1].upper() == app.upper():
            print(f"this is an productive app {app}")
            appType = "good"
    for app in badApps:
        if seperatedTitle[-1].upper() == app.upper():
            print(f"this is a bad app {app}")
            appType = "bad"

    return appType


def getElapsedTime(timeStarted, timeFinished) -> tuple:
    hours = timeFinished[0] - timeStarted[0]
    minutes = timeFinished[1] - timeStarted[1]
    seconds = timeFinished[2] - timeStarted[2]
    timeSpent = (hours, minutes, seconds)
    return timeSpent


if __name__ == "__main__":
    main()
