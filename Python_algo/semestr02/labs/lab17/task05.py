"""
В единственной строке содержится слово.
Оно представляет собой непустую строку, длиной не более 100000 символов,
содержащую только большие и маленькие буквы английского алфавита
Выведите «Yes», если слово является рунным и «No» в противном случае.
Руна представляет собой сочетание 2-4 латинских букв
 1-я из которых заглавная, остальные строчные
  """

s = input()
prev = -4

for i in range(len(s)):
    if s[i].isupper():
        if 1 < i - prev < 5:
            prev = i
        else:
            print("NO")
            break
else:
    if 1 < len(s) - prev < 5:
        print("YES")
    else:
        print("NO")
