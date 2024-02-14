# По данному целому числу N распечатайте все квадраты натуральных
# чисел, не превосходящие N, в порядке возрастания.

n = int(input("N = "))
i = 1
while i*i <= n:
    print(f"{i}^2 = {i*i}")
    i += 1