"""
Даны два четырёхзначных числа: задуманное число и предложенное.
Необходимо определить количество быков и коров.

Бык - это цифра, стоящая на своем месте в обоих числах.
Корова - это цифра, встречающаяся в обоих числах, но не на своем месте.
"""

secret, guess = input().split()
bulls = 0
cows = 0
for i in range(len(secret)):
    if secret[i] == guess[i]:
        bulls += 1
    elif secret[i] in guess:
        cows += 1
print(bulls, cows)

