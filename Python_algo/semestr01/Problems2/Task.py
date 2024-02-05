num = int(input())
for i in range(num):
    space = ' ' * (num - 1 - i)
    symbols = '*' * (i * 2 + 1)
    print(space, symbols)