dec = int(input("dec = "))
bin = 0
place = 1
while dec > 0:
    bin += dec%2 * place
    dec //= 2
    place *=10
print(f"bin = {bin}")