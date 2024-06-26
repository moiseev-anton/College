"""
Напишите программу, которая для одного данного слова определяет его синоним.
Формат входных данных
На вход программе подается количество пар синонимов n.
Далее следует n строк, каждая строка содержит два слова-синонима.
После этого следует одно слово, синоним которого надо найти."""

synonyms = {}

n = int(input())

for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

search_word = input()

# Выводим синоним найденного слова
print(synonyms.get(search_word, "Не найдено"))

