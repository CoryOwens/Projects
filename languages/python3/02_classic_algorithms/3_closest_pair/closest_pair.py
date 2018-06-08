import math
from copy import deepcopy

def distance(a, b):
    return math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)

def closest_pair_brute(points, copy=True):
    """Brute force solution. Compares each point to each other point."""
    if len(points) < 2:
        raise ValueError('Provide 2 or more points. points: {}'.format(points))
    if copy:
        points = deepcopy(points)
    shortest_pair = None
    shortest_distance = None
    for i in range(len(points)):
        point_a = points[i]
        for j in range(i+1, len(points)):
            point_b = points[j]
            d = distance(point_a, point_b)
            if shortest_distance is None or d < shortest_distance:
                shortest_pair = (point_a, point_b)
                shortest_distance = d
    return shortest_pair

def closest_pair_recursive(points, copy=True):
    if len(points) < 2:
        raise ValueError('Provide 2 or more points. n:{}'.format(points))
    if len(points) == 2:
        return (points[0], points[1])
    if len(points) == 3:
        return closest_pair_brute(points, copy=False)
    if copy:
        points = deepcopy(points)
        points.sort(key=lambda x: x[0])
    mid = int(len(points) / 2)
    mid_x = points[mid][0]
    min_left = closest_pair_recursive(points[0:mid])
    left_distance = distance(*min_left)
    min_right = closest_pair_recursive(points[mid:len(points)])
    right_distance = distance(*min_right)
    min_distance = min(left_distance, right_distance)
    mids = [x for x in points if abs(x[0]) < abs(mid_x) + min_distance]
    if len(mids) > 1:
        min_mid = closest_pair_brute(mids)
        mid_distance = distance(*min_mid)
        if mid_distance < min_distance:
            return min_mid
    if left_distance < right_distance:
        return min_left
    return min_right
