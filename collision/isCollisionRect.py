class RectCorrectError(Exception):
    pass

def isCollisionRect(coords1, coords2):
    (x11, y11), (x12, y12) = coords1
    (x21, y21), (x22, y22) = coords2

    if x11 >= x12 or y11 >= y12:
        raise RectCorrectError("1й прямоугольник некоректный")
    if x21 >= x22 or y21 >= y22:
        raise RectCorrectError("2й прямоугольник некоректный")

    return x11 < x22 and x12 > x21 and y11 < y22 and y12 > y21

# try:
#     print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
#     print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
#     print(isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
# except RectCorrectError as e:
#     print(e)
