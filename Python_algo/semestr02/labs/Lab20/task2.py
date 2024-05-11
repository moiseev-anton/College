"""
В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент этого списка."""

from random import sample

# генерируем список случайных уникальных целых чисел
nums = sample(range(-30, 31), 6)
print(*nums)

min_num = min(nums)
max_num = max(nums)

min_index = nums.index(min_num)
max_index = nums.index(max_num)

nums[min_index], nums[max_index] = max_num, min_num
print(*nums)
