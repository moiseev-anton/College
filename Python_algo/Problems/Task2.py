num = int(input("n = "))
result = 1
while num > 0:
    curr = num % 10
    num //= 10
    result *= curr
print(result)
