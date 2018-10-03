class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    # calculates the distance between a point at a center
    def calculate_distance(self, center):
        point = center.point
        result = ((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)
        return result
