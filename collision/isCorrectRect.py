def isCorrectRect(coords):
    if len(coords) != 2:
        return False
    
    left_bottom, right_up = coords
    
    if len(left_bottom) != 2 or len(right_up) != 2:
        return False
    
    x1, y1 = left_bottom
    x2, y2 = right_up

    if x1 < x2 and y1 < y2:
        return True
    else:
        return False

print(isCorrectRect([(-3.4, 1), (9.2, 10)]))
print(isCorrectRect([(-7, 9), (3, 6)]))
