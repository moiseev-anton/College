# Проверить являются ли два слова анаграммой

def check_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    count1 = {}
    count2 = {}

    for i in range(len(word1)):
        count1[word1[i]] = count1.get(word1[i], 0) + 1
        count2[word2[i]] = count2.get(word2[i], 0) + 1

    return count1 == count2

word1, word2 = input().lower().split()
ans = "YES" if check_anagram(word1, word2) else "NO"
print(ans)

