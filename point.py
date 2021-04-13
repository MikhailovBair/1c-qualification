import math
import numpy as np
from config import *


def get_dist2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def is_correct_black_point(x, y, img):
    size_x = np.shape(img)[0]
    size_y = np.shape(img)[1]
    return 0 <= x < size_x and 0 <= y < size_y and img[x][y] == 0


def update_lines(x, y, lines):
    no_repeat = True
    for x1, y1 in lines:
        if get_dist2(x, y, x1, y1) <= MAX_ALLOW_DIF_SQ:
            no_repeat = False
            break

    if no_repeat:
        lines.append((x, y))


def find_unique_angles(x, y, lines):
    angles = set()
    for x1, y1 in lines:
        angle = math.atan2(x1 - x, y1 - y)
        should_add = 1
        for angle_other in angles:
            if abs(angle - angle_other) < 0.1 or abs(abs(angle - angle_other) - math.pi) < 0.1:
                angles.remove(angle_other)
                should_add = 0
                break

        if should_add:
            angles.add(angle)
    return angles


def is_intersection(x, y, img):
    lines = []
    for i in range(-MAX_RADIUS, MAX_RADIUS + 1):
        for j in range(-MAX_RADIUS, MAX_RADIUS + 1):
            x1 = x + i
            y1 = y + j
            if MIN_RADIUS_SQ <= i * i + j * j <= MAX_RADIUS_SQ and is_correct_black_point(x1, y1, img):
                update_lines(x1, y1, lines)

    if len(lines) == 4:
        angles = find_unique_angles(x, y, lines)
        return len(angles) == 0
