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
        try:
            # get the active window
            newActiveWindow = gw.getActiveWindow()
            time.sleep(5)

            # if the window changed
            if newActiveWindow != lastActiveWindow:

                dtNow = dt.datetime.now()
                timeFinished = (dtNow.hour, dtNow.minute, dtNow.second)

                #  if there is both time started and finished this means that we changed from another window
                # to another in this case we will record it on the database
                if timeFinished is not None and timeStarted is not None and lastActiveWindow is not None:
                    windowEntry = entry.WindowEntry(lastActiveWindow.title,
                                                    timeStarted, timeFinished)
                    windowEntry.record_in_database()

                # set the last active window to the current window
                lastActiveWindow = newActiveWindow

                timeStarted = (dtNow.hour, dtNow.minute, dtNow.second)

            else:
                pass

        except:
            print("error has occurred")
            quit()


if __name__ == "__main__":
    main()
