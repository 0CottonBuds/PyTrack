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


class PlotBarGraph:
    def __init__(self, timeOfEachWindow: list[WindowTime]) -> None:
        self.timeOfEachWindow = timeOfEachWindow

    def plotBarGraph(self):
        barNames = self.getBarName()
        xCoordinates = [i for i in range(len(self.timeOfEachWindow))]
        heights = [40 for i in range(len(self.timeOfEachWindow))]

        pyplot.bar(
            xCoordinates,
            heights,
            tick_label=barNames,
            width=0.3,
            color=["blue", "black"],
        )
        pyplot.xlabel("time")
        pyplot.ylabel("Windows")
        pyplot.title("Window Times")
        pyplot.show()

    def getBarName(self):
        barNames = []
        for window in self.timeOfEachWindow:
            barNames.append(window.name)
        return barNames


if __name__ == "__main__":
    windowUtil = WindowRecordUtils()
    timeOfEachWindow = windowUtil.getTimeOfEachWindow()

    barGraph = PlotBarGraph(timeOfEachWindow)
    barGraph.plotBarGraph()
