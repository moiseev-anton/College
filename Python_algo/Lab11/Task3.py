# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите количество элементов этой последовательности,
# которые равны ее наибольшему элементу.

num = int(input("n="))
max = num
count = 1
while num != 0:
    num = int(input("n="))
    if num == max:
        count += 1
    elif num > max:
        max = num
        count = 1
print(f"result = {count}")
