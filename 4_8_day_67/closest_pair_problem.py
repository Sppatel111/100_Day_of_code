# Closest pair problem - The closest pair of points problem or
# closest pair problem is a problem of computational geometry: given n points in metric space,
# find a pair of points with the smallest distance between them.

import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_recursive(points_x, points_y):
    if len(points_x) <= 3:
        min_dist = float('inf')
        for i in range(len(points_x)):
            for j in range(i + 1, len(points_x)):
                min_dist = min(min_dist, distance(points_x[i], points_x[j]))
        return min_dist

    mid = len(points_x) // 2
    mid_point = points_x[mid]
    # print(mid_point)

    points_left_y = []
    points_right_y = []

    for point in points_y:
        if point[0] <= mid_point[0]:
            points_left_y.append(point)
        else:
            points_right_y.append(point)

    d_left = closest_pair_recursive(points_x[:mid], points_left_y)
    d_right = closest_pair_recursive(points_x[mid:], points_right_y)

    d = min(d_left, d_right)

    strip = []
    for point in points_y:
        if abs(point[0] - mid_point[0]) < d:
            strip.append(point)

    ##
    min_strip_dist = float('inf')
    for i in range(len(strip)):
        for j in range(i+1,len(strip)):
            if (strip[j][1] - strip[i][1]) >= d:
                break
            min_strip_dist = min(min_strip_dist, distance(strip[i], strip[j]))

    return min(d, min_strip_dist)


def closest_pair(points):
    points_x = sorted(points, key=lambda point: point[0])
    points_y = sorted(points, key=lambda point: point[1])
    return closest_pair_recursive(points_x, points_y)


points = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (1, 0)]
print(f"The closest distance is: {closest_pair(points)}")
