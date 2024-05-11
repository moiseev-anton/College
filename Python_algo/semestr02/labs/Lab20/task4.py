"""
Дана строка, представляющая государственный регистрационный номер.
Необходимо определить, соответствует ли каждый номер стандарту:
Строка состоит из 6 символов.
Первый символ и последние два - буква из множества
 A, B, C, E, H, K, M, O, P, T, X, Y.
За первым символом следуют три цифры от 0 до 9.
"""


def check_number(s):
    chars = set("ABCEHKMOPTXY")
    if len(s) != 6:
        return False
    if not s[1:4].isdigit():
        return False
    if s[0] not in chars or s[-2] not in chars or s[-1] not in chars:
        return False
    return True


bus_num = input().strip()
ans = "YES" if check_number(bus_num) else "NO"
print(ans)