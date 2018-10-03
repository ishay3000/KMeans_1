from Point import Point


class Center:
    def __init__(self, point: Point):
        self.point = point
        self.lst_point = []

    def __str__(self):
        return self.point.__str__()