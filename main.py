class RectCorrectError(Exception):
    pass

from collision import isCorrectRect
from collision import isCollisionRect
from collision import intersectionAreaRect
from collision import intersectionAreaMultiRect


print(isCorrectRect.isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect.isCorrectRect([(-7, 9), (3, 6)]))

try:
    print(isCollisionRect.isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
    print(isCollisionRect.isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
    print(isCollisionRect.isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
except RectCorrectError as e:
    print(e)

try:
    print(intersectionAreaRect.intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
    print(intersectionAreaRect.intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
    print(intersectionAreaRect.intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
except RectCorrectError as e:
    print(e)

rectangles = [
    [(2, 2), (5, 4)],
    [(0, 1), (2, 2)],
    [(1, 1), (4, 4)],
    [(2, -1), (3, 3)]
]

result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")

incorrect_rectangles = [
    [(-3, 1), (9, 10)],
    [(3, 17), (13, 1)]
]

try:
    intersectionAreaMultiRect(incorrect_rectangles)
except RectCorrectError as e:
    print(e)
