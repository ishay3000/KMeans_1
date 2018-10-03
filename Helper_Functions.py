"""
@author Ishay Muchtar
HELPER FUNCTIONS FOR K-MEANS
"""
import random

from Center import Center
from Point import Point


# reads the Points data from a file
def read_points_from_file(path = r"C:\Users\Ishay Cena\Documents\אורט סינגאלובסקי\יד\בית ספר\ML\K-means clustering 2.txt"):
    lst_points = []
    with open(path, "r") as file:
        for line in file:
            x, y = line.split()
            lst_points.append(Point(float(x), float(y)))

    return lst_points


# gets min and max points from the points list
def get_min_max_points(lst_points):
    # get max & min x
    x_min = min(lst_points, key=lambda point: point.x).x
    x_max = max(lst_points, key=lambda point: point.x).x

    # get max & min y
    y_min = min(lst_points, key=lambda point: point.y).y
    y_max = max(lst_points, key=lambda point: point.y).y

    point_min = Point(x_min, y_min)
    point_max = Point(x_max, y_max)
    return point_min, point_max


# initiates the center's coordination by guessing a location
def initiate_center(point_min: Point, point_max: Point):
    x_center = random.uniform(point_min.x, point_max.y)
    y_center = random.uniform(point_max.x, point_max.y)

    center = Center(Point(x_center, y_center))
    return center


# assign each point to its corresponding center
def assign_points_to_centers(center1: Center, center2: Center, lst_points):
    lst_center1 = []
    lst_center2 = []
    for point in lst_points:
        result1 = point.calculate_distance(center1)
        result2 = point.calculate_distance(center2)
        # if point is closer to the first center, assign it to center1
        if result1 < result2:
            lst_center1.append(point)
        # point is closer to center2
        else:
            lst_center2.append(point)

    # assign lists to each center
    center1.lst_point = lst_center1
    center2.lst_point = lst_center2


# calculates the average for the circle and re-assigns it new coordination
def calculate_average_for_center(center: Center):
    sum_x = 0.0
    sum_y = 0.0
    avg_x, avg_y = 0.0, 0.0
    count = len(center.lst_point)
    for point in center.lst_point:
        sum_x += point.x
        sum_y += point.y
    try:
        avg_x = sum_x / count
        avg_y = sum_y / count
    except ZeroDivisionError:
        print('div by zero caught')
    return avg_x, avg_y


# updates the center according to the average of its points
def update_center(center: Center):
    x, y = calculate_average_for_center(center)
    center.point.x = x
    center.point.y = y


# does KMeans algorithm on two centers and a bunch of points
def k_means(center1: Center, center2: Center, lst_points):
    for i in range(3):
        assign_points_to_centers(center1, center2, lst_points)
        # calculate average for each center, and re-assign it new coordination
        update_center(center1)
        update_center(center2)
