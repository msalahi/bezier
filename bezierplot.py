from collections import namedtuple
from bezier import bezier
import matplotlib.pyplot as plt
import numpy as np


MPL_STYLE = "ggplot"
plt.style.use(MPL_STYLE)


def default_style_colors():
    global MPL_STYLE
    style = plt.style.library[MPL_STYLE]
    return style["axes.color_cycle"]


def get_extrema(x, y):
    return np.min(x), np.max(x), np.min(y), np.max(y)


def get_margin(min_x, max_x, min_y, max_y, margin_ratio=.05):
    return max(max_x - min_x, max_y - min_y) * margin_ratio
    

def axis_bounds(x, y, margin_ratio=.05):
    min_x, max_x, min_y, max_y = get_extrema(x, y)
    margin = get_margin(
        min_x, max_x, min_y, max_y,
        margin_ratio=margin_ratio)
    return min_x - margin, max_x + margin, min_y - margin, max_y + margin


def plot_bezier_curve(control_points, **kwargs):
    colors = default_style_colors()
    x, y = list(zip(*control_points))
    times = np.linspace(0, 1, num=1000)
    curve = [bezier(control_points, t) for t in times]
    curve_x, curve_y = zip(*curve)
    plot_kwargs = {"color": colors[1], "marker": "o"}  # set default style
    plot_kwargs.update(kwargs)
    plt.plot(x, y, **plot_kwargs)
    plt.plot(curve_x, curve_y, color=colors[0])
    plt.axis(axis_bounds(x, y))
    plt.show()
