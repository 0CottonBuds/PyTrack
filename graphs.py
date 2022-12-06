import matplotlib.pyplot as pyplot
from entry import WindowTime
from entry import retrieveRawEntries
from entry import formatRawEntries
from entry import getTotalTimeElapsed
from entry import getTimeOfEachWindow


left_coordinates = [1, 2, 3, 4, 5]
heights = [10, 20, 30, 15, 40]
bar_labels = ["One", "Two", "Three", "Four", "Five"]
pyplot.bar(
    left_coordinates, heights, tick_label=bar_labels, width=0.6, color=["red", "black"]
)
pyplot.xlabel("X-axis")
pyplot.ylabel("Y-axis")
pyplot.title("A simple bar graph")
pyplot.show()


def plotData(data: list[WindowTime]):
    pass


if __name__ == "__main__":
    retrieveEntries = retrieveRawEntries()
    formattedEntries = formatRawEntries(retrieveEntries)
    totalTimeElapsed = getTotalTimeElapsed(formattedEntries)
    totalTimeOfEachWindow = getTimeOfEachWindow(formattedEntries)
    print(totalTimeElapsed.get_time)

    for time in totalTimeOfEachWindow:
        print(f"name:{time.name} time:{time.get_time()}")
