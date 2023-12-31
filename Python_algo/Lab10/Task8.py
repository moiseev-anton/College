# Есть две коробки, первая размером A₁×B₁×C₁, вторая размером A₂×B₂×C₂.
# Определите, можно ли разместить одну из этих коробок внутри другой, при условии,
# что поворачивать коробки можно только на 90 градусов вокруг ребер. Программа получает
# на вход числа A₁,B₁,C₁,A₂,B₂,C₂.Программа должна вывести одну из следующих строчек: 
# Коробки одинаковые,Первая коробка меньше чем вторая, если первая коробка может быть
# положена во вторую, Первая коробка больше чем вторая, если вторая 
# коробка может быть положена в первую, Коробки несравнимы, во всех остальных случаях.

a1, b1, c1 = map(int, input("Введите размеры первой коробки (через пробел): ").split())
a2, b2, c2 = map(int, input("Введите размеры второй коробки (через пробел): ").split())


if ((a1 == a2 and b1 == b2 and c1 == c2) or
    (a1 == a2 and b1 == c2 and c1 == b2) or
    (a1 == b2 and b1 == a2 and c1 == c2) or
    (a1 == b2 and b1 == c2 and c1 == a2) or
    (a1 == c2 and b1 == a2 and c1 == b2) or
    (a1 == c2 and b1 == b2 and c1 == a2)):
    print("Коробки одинаковые")

elif (
    (a1 <= a2 and b1 <= b2 and c1 <= c2) or
    (a1 <= a2 and b1 <= c2 and c1 <= b2) or
    (a1 <= b2 and b1 <= a2 and c1 <= c2) or
    (a1 <= b2 and b1 <= c2 and c1 <= a2) or
    (a1 <= c2 and b1 <= a2 and c1 <= b2) or
    (a1 <= c2 and b1 <= b2 and c1 <= a2)
):
    print("Первая коробка меньше чем вторая")

elif (
    (a2 <= a1 and b2 <= b1 and c2 <= c1) or
    (a2 <= a1 and b2 <= c1 and c2 <= b1) or
    (a2 <= b1 and b2 <= a1 and c2 <= c1) or
    (a2 <= b1 and b2 <= c1 and c2 <= a1) or
    (a2 <= c1 and b2 <= a1 and c2 <= b1) or
    (a2 <= c1 and b2 <= b1 and c2 <= a1)
):
    print("Первая коробка больше чем вторая")

else:
    print("Коробки несравнимы")

