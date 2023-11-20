# Описать множество гласных и согласных букв русского языка.
# Определить количество гласных и согласных букв в предложении,
# введенном с клавиатуры.

vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
vowels |= {char.upper() for char in vowels}

text = input("Введите текст: ")

count_vowels = 0
count_consonants = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

print(f"\nГласных: {count_vowels}\nСогласных: {count_consonants}")