"""
Напишите программу, которая заполняет массив
первыми N натуральными числами и выводит его.
"""
n = int(input())
nums = [i+1 for i in range(n)]
for num in nums:
    print(num, end=' ')

