
class WindowEntry():
    def __init__(self, windowTitle, timeStarted, timeFinished):
        self.windowTitle = windowTitle
        self.timeStarted = timeStarted
        self.timeFinished = timeFinished

    def record_in_database(self):
        print(f"window: {self.windowTitle}")
        print(f"time started: {self.timeStarted}")
        print(f"time finished: {self.timeFinished}")

        # minus the time started to time finished and convert it to a more readable format
        hours = self.timeFinished[0] - self.timeStarted[0]
        minutes = self.timeFinished[1] - self.timeStarted[1]
        seconds = self.timeFinished[2] - self.timeStarted[2]
        timeSpent = (hours, minutes, seconds)

        print(
            f"time spent in program : {timeSpent[0]}H {timeSpent[1]}M {timeSpent[2]}S")


if __name__ == "__main__":
    pass
