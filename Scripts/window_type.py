import sqlite3


class WindowType:
    """Class window type use to store name type and rating of window"""

    window_name: str
    window_type: str
    window_rating: int

    def name_chooser(self, window_full_name: str):
        """lets you pick what part of the full name do you want this window to use"""
        separated_window_name = window_full_name.split("- ")
        print(separated_window_name)
        index = input("What name would you like to put (index): ")
        print("input ")
        return separated_window_name[int(index)]

    def check_app_type(self):
        '''Takes a window checks and returns string "bad" or "good"'''

        separated_window_title = self.window_name.split("- ")

        for part in separated_window_title:
            window = find_window_on_database_by_name(part)

            if window != None:
                self.window_name = window.window_name
                self.window_type = window.window_type
                self.window_rating = window.window_rating
                break
            else:
                pass

    def __str__(self) -> str:
        return f"name: {self.window_name}\ntype: {self.window_type}\nrating: {self.window_rating}"


class WindowTypeIn(WindowType):
    """inherits from class window type have functions to enter data in database"""

    def __init__(self, window_name: str) -> None:
        self.window_name = self.name_chooser(window_name)
        self.window_type = input("What type of app is this (good, bad): ")
        self.window_rating = int(input("Rating of application (1-100): "))

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
            "Setup",
            "Calculator",
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


def find_window_on_database_by_name(query_name: str) -> WindowType | None:
    """find window on data base by name returns windowType object"""
    conn = sqlite3.connect("pyTrack.db")
    c = conn.cursor()
    c.execute("""SELECT * FROM windowTypes WHERE windowName = ?""", (query_name,))
    results = c.fetchall()
    if results != []:
        window = WindowType()
        window.window_name = results[0][0]
        window.window_type = results[0][1]
        window.window_rating = results[0][2]
        conn.commit()
        conn.close()
        return window

    else:
        conn.commit()
        conn.close()
        return None


if __name__ == "__main__":
    # windows = pygetwindow.getAllWindows()
    # window_filter = WindowFilter(windows)
    # window_filter.full_filter()

    # for window in window_filter.windows:
    #     temp = WindowTypeIn(window.title)
    #     temp.record_in_database()
    pass
