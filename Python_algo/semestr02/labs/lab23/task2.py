"""
Даны два действительных числа x и y.
Проверьте, принадлежит ли точка с координатами (x,y) заштрихованному квадрату
(включая его границу). Если точка принадлежит квадрату,
выведите слово YES, иначе выведите слово NO. На рисунке сетка проведена с шагом 1.
"""


def is_point_in_square(x, y):
    return (abs(x) <= 1) and (abs(y) <= 1)


if __name__ == "__main__":
    x = float(input())
    y = float(input())
    if is_point_in_square(x, y):
        print("YES")
    else:
        print("NO")

