import cv2
import sys

from point import *

origin = cv2.imread(sys.argv[1])

gray = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
SIZEx = np.shape(gray)[0]
SIZEy = np.shape(gray)[1]


def show_intersections(intersections):
    for x, y in intersections:
        for i in range(-7, 7):
            for j in range(-7, 7):
                x1 = x + i
                y1 = y + j

                if 0 <= x1 < SIZEx and 0 <= y1 < SIZEy:
                    origin[x1][y1] = (0, 0, 255)


def count_intersection():
    intersections = []
    for x in range(SIZEx):
        for y in range(SIZEy):
            if gray[x][y] == 0 and is_intersection(x, y, gray):
                update_lines(x, y, intersections)

    show_intersections(intersections)

    cv2.imshow("Intersections", origin)
    return len(intersections)


print(count_intersection())
if cv2.waitKey(0) & 0xFF == ord("q"):
    exit(0)
