import matplotlib.pyplot as pyplot

from entry import *


def example():
    left_coordinates = [1, 2, 3, 4, 5]
    heights = [10, 20, 30, 150, 40]
    bar_labels = [
        "window One",
        "Window Two",
        "Window Three",
        "Window Four",
        "Window Five",
    ]
    pyplot.bar(
        left_coordinates,
        heights,
        tick_label=bar_labels,
        width=0.6,
        color=["blue", "gray"],
    )
    pyplot.xlabel("Time")
    pyplot.ylabel("Windows")
    pyplot.title("A simple bar graph")
    pyplot.show()


def plotBarGraph(timeOfEachWindow: list[WindowTime]):
    pass


if __name__ == "__main__":
    windowUtil = WindowRecordUtils()
    timeOfEachWindow = windowUtil.getTimeOfEachWindow()
