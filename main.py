# Пример ввода 1. isCorrectRect
# isCorrectRect([(-3.4, 1),(9.2, 10)]) # Вернет True
# isCorrectRect([(-7, 9),(3, 6)]) # Вернет False

# Пример ввода 2. isCollisionRect
# isCollisionRect([(-3.4, 1),(9.2, 10)], [(-7.4, 0),(13.2, 12)]) # Вернет True
# isCollisionRect([(1, 1),(2, 2)], [(3, 0),(13, 1)]) # Вернет False
# isCollisionRect([(1, 1),(2, 2)], [(3, 17),(13, 1)]) # Вызовет ошибку

# Пример ввода 3. intersectionAreaRect
# intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]) # Вернет некоторое положительное число
# intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]) # Вернет 0
# intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]) # Вызовет ошибку

# Пример ввода 4. intersectionAreaMultiRect
# rectangles = [ # Корректные прямоугольники, покажет уникальную площадь
#     [(-3, 1), (9, 10)],
#     [(-7, 0), (13, 12)],
#     [(0, 0), (5, 5)],
#     [(2, 2), (7, 7)]
# ]

# incorrect_rectangles = [
#     [(-3, 1), (9, 10)],
#     [(3, 17), (13, 1)]  # Некорректный прямоугольник, вызовет ошибку
# ]
class RectCorrectError(Exception):
    pass

from collision.isCorrectRect import isCorrectRect
from collision.isCollisionRect import isCollisionRect
from collision.intersectionAreaRect import intersectionAreaRect
from collision.intersectionAreaMultiRect import intersectionAreaMultiRect

status = True
while status:
    print("--------Проверяемые функции--------")
    print("------1. isCorrectRect-------------")
    print("------2. isCollisionRect-----------")
    print("------3. intersectionAreaRect------")
    print("------4. intersectionAreaMultiRect-")
    print("------5. Выход из программы--------")

    b = input("Введите номер проверяемой функции: ")
    try:
        a = int(b)
        if a < 1 or a > 5:
            print("Введите корректный номер от 1 до 5.")
            continue
    except ValueError:
        print("Введите число.")
        continue

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

    elif a == 2:
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
                except ValueError as e:
                    print(e)
                break
            except ValueError:
                print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.") 
         
    elif a == 3:
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
                except ValueError as e:
                    print(e)
                break
            except ValueError:
                print("Введенное Вами число должно быть целое или дробное. Попробуйте еще раз.")

    elif a == 4:
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

                try:
                    result = intersectionAreaMultiRect(rectangles)
                    print(f"Уникальная площадь пересечения: {result}")
                except ValueError as e:
                    print(e)
                break

            except ValueError:
                print("Введенное Вами число должно быть целое. Попробуйте еще раз.")

    elif a == 5:
        status = False
