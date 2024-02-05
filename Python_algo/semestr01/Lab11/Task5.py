# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов 
# этой последовательности равны друг другу.

num = int(input("n="))
max_count = 0
count = 0
prev = 0
while num != 0:
    if num != prev:
        count = 1
    else:
        count += 1
    if max_count < count:
        max_count = count
    prev = num    
    num = int(input("n="))
        
print(f"result = {max_count}")
