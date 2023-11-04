# Даны три целых числа. Найдите наибольшее из них 
# (программа должна вывести ровно одно целое число).
# Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# max_num = a

# if b > max_num:
#     max_num = b

# if c >  max_num:
#     max_num = c

# print(max_num)    

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    print(b)
else:
    print(c)