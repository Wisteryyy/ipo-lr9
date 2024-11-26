class RectCorrectError(Exception):
    pass

from collision import isCorrectRect
from collision import isCollisionRect
from collision import intersectionAreaRect
from collision import intersectionAreaMultiRect

print("--------Проверяемые функции--------")
print("------1. isCorrectRect-------------")
print("------2. isCollisionRect-----------")
print("------3. intersectionAreaRect------")
print("------4. intersectionAreaMultiRect-")

a = int(input("Введите номер проверяемой функции: "))

if a == 1:
    while True:
        try:
            x1 = float(input("Введите координату x1: "))
            y1 = float(input("Введите координату y1: "))
            x2 = float(input("Введите координату x2: "))
            y2 = float(input("Введите координату y2: "))
            print(isCorrectRect([(x1, y1),(x2, y2)]))
            break
        except ValueError:
            print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.")
        
if a == 2:
    while True:
        try:
            x11 = float(input("Введите координату x11: "))
            y11 = float(input("Введите координату y11: "))
            x12 = float(input("Введите координату x12: "))
            y12 = float(input("Введите координату y12: "))
            x21 = float(input("Введите координату x21: "))
            y21 = float(input("Введите координату y21: "))
            x22 = float(input("Введите координату x22: "))
            y22 = float(input("Введите координату y22: "))
            try:
                print(isCollisionRect([(x11, y11), (x12, y12)], [(x21, y21), (x22, y22)]))
            except RectCorrectError as e:
                print(e)
            break
        except ValueError:
            print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.")
            
if a == 3:
    while True:
        try:
            x11 = float(input("Введите координату x11: "))
            y11 = float(input("Введите координату y11: "))
            x12 = float(input("Введите координату x12: "))
            y12 = float(input("Введите координату y12: "))
            x21 = float(input("Введите координату x21: "))
            y21 = float(input("Введите координату y21: "))
            x22 = float(input("Введите координату x22: "))
            y22 = float(input("Введите координату y22: "))
            try:
                print(intersectionAreaRect([(x11, y11), (x12, y12)], [(x21, y21), (x22, y22)]))
            except RectCorrectError as e:
                print(e)
            break
        except ValueError:
            print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.")
            
if a == 4:
    while True:
        try:
            b = int(input("Введите количество прямоугольников в списке прямоугольников: "))
            rectangles = []
            
            for i in range(b):
                print(f"Введите координаты для прямоугольника {i + 1}:")
                while True:
                    try:
                        x1 = float(input("Введите x1: "))
                        y1 = float(input("Введите y1: "))
                        x2 = float(input("Введите x2: "))
                        y2 = float(input("Введите y2: "))
                        
                        rectangles.append([(x1, y1), (x2, y2)])
                        break
                    except ValueError:
                        print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.")

            result = intersectionAreaMultiRect(rectangles)
            print(f"Уникальная площадь пересечения: {result}")
            break
        except ValueError:
            print("Введенное Вами число должно быть целое. Попробуйте еще раз.")

if a < 1 or a > 4:
    print("Введенное Вами число некорректно. Попробуйте еще раз.")
