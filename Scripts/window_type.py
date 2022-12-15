import sqlite3
import pygetwindow


class WindowType:
    """Class window type use to store name type and rating of window"""

    window_name: str
    window_type: str
    window_rating: int

    def __init__(self, window_name: str, window_type: str, window_rating: int) -> None:
        self.window_name = window_name  # self.name_chooser(window_name)
        self.window_type = window_type
        self.window_rating = int(window_rating)

    def name_chooser(self, window_full_name: str):
        """lets you pick what part of the full name do you want this window to use"""
        separated_window_name = window_full_name.split("- ")
        print(separated_window_name)
        index = input("What name would you like to put")
        print("input ")
        return separated_window_name[int(index)]

    def __str__(self) -> str:
        return f"name: {self.window_name}\ntype: {self.window_type}\nrating: {self.window_rating}"


class WindowTypeIn(WindowType):
    """inherits from class window type have functions to enter data in database"""

    def __init__(self, window_name: str, window_type: str, window_rating: int) -> None:
        super().__init__(window_name, window_type, window_rating)

    def record_in_database(self):
        """enter the data to data base"""
        conn = sqlite3.connect("pyTrack.db")
        c = conn.cursor()
        c.execute(
            """INSERT INTO windowTypes(windowName, windowType, windowRating) VALUES(?,?,?)""",
            (self.window_name, self.window_type, self.window_rating),
        )
        conn.commit()
        conn.close()
        print("successfully added to database")


class WindowFilter:
    def __init__(self, windows: list) -> None:
        self.windows = windows

    def full_filter(self):
        """uses all the filter in the class"""

        self.filter_ignored_windows()
        self.filter_windows_that_are_on_database()

    def filter_windows_that_are_on_database(self):
        """cycles to the list of windows(Input) and checks if there is an entry of that window"""
        filtered_windows = []
        for window in self.windows:
            splitted_name = window.title.split()
            result = None
            for part in splitted_name:
                result = find_window_on_database_by_name(part)
                if result != []:
                    break
                else:
                    pass
            filtered_windows.append(window)
        self.windows = filtered_windows
        return filtered_windows

    def filter_ignored_windows(self) -> list:
        """filters the windows that you want to ignore and returns a list of windows"""
        filtered_windows = []
        ignored_window_names = [
            "",
            "Settings",
            "Microsoft Text Input Application",
            "Program Manager",
            "Clock",
        ]

        for window in self.windows:
            splitted_title: list[str] = window.title.split("- ")
            # print(window.title)
            if splitted_title[-1] in ignored_window_names:
                # print(f"this window is ignored name: {window.title}")
                pass
            else:
                filtered_windows.append(window)

        self.windows = filtered_windows
        return filtered_windows

    def __str__(self) -> str:
        return f"{self.windows}"


def find_window_on_database_by_name(query_name: str) -> WindowType | list:
    """find window on data base by name returns windowType object"""
    conn = sqlite3.connect("pyTrack.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM windowTypes WHERE windowName = ?""", (query_name,))
    results = c.fetchall()
    if results != []:
        window = WindowType(results[0][1], results[0][2], results[0][3])
        conn.commit()
        conn.close()
        return window

    else:
        conn.commit()
        conn.close()
        return results


def check_app_type(title: str) -> str:
    '''Takes a window checks and returns string "bad" or "good"'''

    productive_apps = ["Visual Studio Code"]
    bad_apps = ["Opera"]
    app_type = ""

    separated_title: list[str] = title.split("- ")
    for app in productive_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is an productive app {str(separated_title)}")
            app_type = "good"
    for app in bad_apps:
        if separated_title[-1].upper() == app.upper():
            print(f"this is a bad app {str(separated_title)}")
            app_type = "bad"

    return app_type


if __name__ == "__main__":
    windowType: WindowTypeIn = WindowTypeIn("discord", "bad", 50)

    # windows = pygetwindow.getAllWindows()
    # window_filter = WindowFilter(windows)
    # window_filter.filter_ignored_windows()

    # for window in window_filter.windows:
    #     print(window.title)
