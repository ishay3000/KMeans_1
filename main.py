"""
@author Ishay Muchtar
KMeans algorithm
"""
from Helper_Functions import *

# read points from file
lst_points = read_points_from_file()

# get min and max points
point_min, point_max = get_min_max_points(lst_points)

# get random coordination
center1 = initiate_center(point_min, point_max)
center2 = initiate_center(point_min, point_max)

print('centers:\n'
      'Center 1: {}\n'
      'Center 2: {}'.format(center1, center2))

k_means(center1, center2, lst_points)

print('centers:\n'
      'Center 1: {}\n'
      'Center 2: {}'.format(center1, center2))


# assign_points_to_centers(center1, center2, lst_points)
#
# # calculate average for each center, and re-assign it new coordination
# update_center(center1)
# update_center(center2)
#
# print('First centers iteration:\n'
#       'Center 1: {}\n'
#       'Center 2: {}'.format(center1, center2))
#
#
# print('Second centers iteration:\n'
#       'Center 1: {}\n'
#       'Center 2: {}'.format(center1, center2))
#
# assign_points_to_centers(center1, center2, lst_points)
# update_center(center1)
# update_center(center2)
#
# print('Third centers iteration:\n'
#       'Center 1: {}\n'
#       'Center 2: {}'.format(center1, center2))
#
# assign_points_to_centers(center1, center2, lst_points)
# update_center(center1)
# update_center(center2)
#
# print('Fourth centers iteration:\n'
#       'Center 1: {}\n'
#       'Center 2: {}'.format(center1, center2))
#
# assign_points_to_centers(center1, center2, lst_points)
# update_center(center1)
# update_center(center2)