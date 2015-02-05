import numpy


def linear_bezier(point1, point2, t):
    return (1.0 - t) * point1 + t * point2


def interpolate_control_points(points, t):
    return [
        linear_bezier(point1, point2, t)
        for point1, point2 in zip(points, points[1:])]


def bezier(control_points, t, stoplevel=2):
    points = points_as_arrays(control_points)
    while len(points) > stoplevel:
        points = interpolate_control_points(points, t)
    return linear_bezier(points[0], points[1], t)


def points_as_arrays(point_tuples):
    return [numpy.array(point) for point in point_tuples]
