"""
Напишите программу создания небольшого словаря сленговых программерских выражений,
чтобы она потом по запросу возвращала значения из этого словаря. """

dictionary = {}

n = int(input())

for _ in range(n):
    word, definition = input().split(": ")
    dictionary[word.lower()] = definition

m = int(input())

for _ in range(m):
    search_word = input().lower()
    definition = dictionary.get(search_word, "Не найдено")
    print(definition)

