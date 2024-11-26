class RectCorrectError(Exception): # создаем собственный тип исключения, унаследованный от базового класса Exception
    pass

def intersectionAreaRect(coords1, coords2):
    (x11, y11), (x12, y12) = coords1
    (x21, y21), (x22, y22) = coords2

    if x11 >= x12 or y11 >= y12: # проверка корректности прямоугольников
        raise RectCorrectError("Первый прямоугольник некорректный.")
    if x21 >= x22 or y21 >= y22:
        raise RectCorrectError("Второй прямоугольник некорректный.")

    intersection_x1 = max(x11, x21) # это максимальные значения координат левого нижнего угла пересекающегося прямоугольника, так как пересечение начинается от максимального значения левых нижних углов исходных прямоугольников
    intersection_y1 = max(y11, y21)
    intersection_x2 = min(x12, x22) # это минимальные значения координат правого верхнего угла пересекающегося прямоугольника, чтобы определить, до какого момента пересекаются прямоугольники
    intersection_y2 = min(y12, y22)

    if intersection_x1 < intersection_x2 and intersection_y1 < intersection_y2: # проверяем, пересекаются ли прямоугольники. для этого левый нижний угол пересечения должен быть меньше, чем правый верхний угол
        intersection_area = (intersection_x2 - intersection_x1) * (intersection_y2 - intersection_y1) # если пересечение существует, рассчитываем его площадь
        return intersection_area
    else:
        return 0

def intersectionAreaMultiRect(rectangles):
    for index, rect in enumerate(rectangles, start=1): # перебираем все прямоугольники в списке. enumerate используется, чтобы получить индекс каждого прямоугольника, начиная с 1
        if len(rect) != 2 or not all(isinstance(cord, tuple) and len(cord) == 2 for cord in rect): # проверяем, что каждый прямоугольник состоит ровно из двух элементов(кортежей) и что каждый из этих элементов является кортежем длины 2
            raise RectCorrectError(f"{index} прямоугольник некорректный: должна быть пара кортежей.")
        
        (x1, y1), (x2, y2) = rect # извлекаем координаты и делаем повторную проверку
        if x1 >= x2 or y1 >= y2:
            raise RectCorrectError(f"{index} прямоугольник в списке прямоугольников неккоректный.")

    unique_areas = set()
    
    for i in range(len(rectangles)): # два цикла используются для проверки всех пар прямоугольников. Если площадь пересечения больше 0, то она добавляется в множество unique_areas
        for j in range(i + 1, len(rectangles)):
            area = intersectionAreaRect(rectangles[i], rectangles[j])
            if area > 0:
                unique_areas.add(area)

    return sum(unique_areas) # возвращаем сумму всех уникальных площадей пересечения прямоугольников

rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
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