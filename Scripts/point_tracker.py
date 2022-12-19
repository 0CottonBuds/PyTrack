from notification import NotificationManager


class PointTracker:
    points: int

    def __init__(self) -> None:
        self.points = 450

    def add_points(self, point_to_add: int):
        self.points += point_to_add

    def subtract_points(self, point_to_add: int):
        self.points -= point_to_add

    def check_point_threshold(self):
        """check point threshold and notify to take a break or get back to work"""
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
