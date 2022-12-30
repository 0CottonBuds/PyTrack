from .notification import NotificationManager
from .window_type import WindowType
import configparser


class PointTracker:
    points: int

    def __init__(self) -> None:
        self.read_settings_config_file()
        self.points = self.starting_points

    def change_points(self, window: WindowType):
        """add and subtracts points based on app type. \n"""

        if window.window_type == "good":
            self.add_points(window.window_rating)
            print(f"added {window.window_rating} points\ntotal points: {self.points}")
        elif window.window_type == "bad":
            self.subtract_points(window.window_rating)
            print(
                f"subtract {window.window_rating} points\ntotal points: {self.points}"
            )
        else:
            print(window.window_name)
            print("this window does not have a label")

    def add_points(self, point_to_add: int):
        self.points += point_to_add

    def subtract_points(self, point_to_add: int):
        self.points -= point_to_add

    def check_point_threshold(self):
        """check point threshold. \n
        calls the notification module to fire notification when threshold is reached."""
        # self.read_settings_config_file()

        if self.points >= self.POINT_THRESHOLD_TAKE_A_BREAK:
            notification_manager = NotificationManager()
            notification_manager.take_a_break()
        if self.points <= self.POINT_THRESHOLD_GET_BACK_TO_WORK:
            notification_manager = NotificationManager()
            notification_manager.get_back_to_work()

    def read_settings_config_file(self):
        config_parser = configparser.ConfigParser()
        config_parser.read("PytrackUtils\settings\settingsConfig.ini")  # type: ignore

        self.starting_points = int(config_parser["App"]["starting_points"])
        self.POINT_THRESHOLD_GET_BACK_TO_WORK = int(
            config_parser["App"]["warning_threshold"]
        )
        self.POINT_THRESHOLD_TAKE_A_BREAK = int(config_parser["App"]["break_threshold"])

    def __str__(self) -> str:
        return f"Points: {self.points}"


if __name__ == "__main__":
    point = PointTracker()
    point.points = 0
    point.check_point_threshold()
