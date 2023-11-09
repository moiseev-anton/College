# Определите количество четных элементов в последовательности,
# завершающейся числом 0.

num = int(input("n="))
count = 0
while num != 0:
    if num % 2 == 0:
        count += 1
    num = int(input("n="))    
print(f"result = {count}") 
