"""
Даны пять действительных чисел: x, y, xc, yc, r.
Проверьте, принадлежит ли точка (x,y) кругу с центром (xc, yc) и радиусом r.
Если точка принадлежит кругу, выведите слово YES, иначе выведите слово NO.
"""


def is_point_in_circle(x, y, xc, yc, r):
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2


if __name__ == "__main__":
    x = float(input())
    y = float(input())
    xc = float(input())
    yc = float(input())
    r = float(input())
    if is_point_in_circle(x, y, xc, yc, r):
        print("YES")
    else:
        print("NO")

