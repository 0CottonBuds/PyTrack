class PointTracker:
    points: int

    def __init__(self) -> None:
        self.points = 0

    def add_points(self, point_to_add: int):
        self.points += point_to_add

    def subtract_points(self, point_to_add: int):
        self.points -= point_to_add


def pasas():
    pass
