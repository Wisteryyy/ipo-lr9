class RectCorrectError(Exception): # пользовательский класс исключения RectCorrectError, который наследует от базового класса Exception
    pass

def intersectionAreaRect(coords1, coords2): # функция
    (x11, y11), (x12, y12) = coords1 # распаковка координат
    (x21, y21), (x22, y22) = coords2

    if x11 >= x12 or y11 >= y12: # проверка на корректность 
        raise RectCorrectError("Первый прямоугольник некорректный.")
    if x21 >= x22 or y21 >= y22:
        raise RectCorrectError("Второй прямоугольник некорректный.")

    cross_x1 = max(x11, x21) # это максимальные значения координат левого нижнего угла пересекающегося прямоугольника, так как пересечение начинается от максимального значения левых нижних углов исходных прямоугольников
    cross_y1 = max(y11, y21)
    cross_x2 = min(x12, x22) # это минимальные значения координат правого верхнего угла пересекающегося прямоугольника, чтобы определить, до какого момента пересекаются прямоугольники
    cross_y2 = min(y12, y22)

    if cross_x1 < cross_x2 and cross_y1 < cross_y2: # проверяем, пересекаются ли прямоугольники. для этого левый нижний угол пересечения должен быть меньше, чем правый верхний угол
        intersection_area = (cross_x2 - cross_x1) * (cross_y2 - cross_y1) # если пересечение существует, рассчитываем его площадь как произведение ширины (intersection_x2 - intersection_x1) и высоты (intersection_y2 - intersection_y1)
        return intersection_area
    else:
        return 0
    
try:
    print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))
    print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))
    print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
except RectCorrectError as e:
    print(e)