from .notification import NotificationManager
from .window_type import WindowType


class PointTracker:
    points: int

    def __init__(self) -> None:
        self.points = 450

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

        POINT_THRESHOLD_TAKE_A_BREAK = 1650
        POINT_THRESHOLD_GET_BACK_TO_WORK = 0

        if self.points >= POINT_THRESHOLD_TAKE_A_BREAK:
            notification_manager = NotificationManager()
            notification_manager.take_a_break()
        if self.points <= POINT_THRESHOLD_GET_BACK_TO_WORK:
            notification_manager = NotificationManager()
            notification_manager.get_back_to_work()

    def __str__(self) -> str:
        return f"Points: {self.points}"


if __name__ == "__main__":
    point = PointTracker()
    point.points = 0
    point.check_point_threshold()
