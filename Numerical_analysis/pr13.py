from random import uniform
from math import log10
# uniform генерует случайные чисела с равномерным распределением в диапазоне [a, b]

def func(x):
    return x*x*log10(x)


def monte_carlo(a, b, n):
    total = sum(func(uniform(a,b)) for _ in range(n))
    return (b-a)*total/n

def monte_carlo(a, b, n):
    total = 0

    for _ in range(n):
        x = uniform(a,b)
        total += func(x)

    integral = (b-a)*total/n
    return integral

if __name__ == '__main__':
    a = 1.4
    b = 3
    for n in (10, 20, 30, 100000):
        result = monte_carlo(a, b, n)
        print(f"При {n = }\nРезультат ≈ {result:.6f}\n")

