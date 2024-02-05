# 2. Три сопротивления R1, R2, R3 соединены параллельно.
# Найти сопротивление соединения.

R1 = float(input("R1 = "))
R2 = float(input("R2 = "))
R3 = float(input("R3 = "))

if R1 == 0 or R2 == 0 or R3 == 0:
    print("Ошибка")
else:
    R = 1 / (1 / R1 + 1 / R2 + 1 / R3)
    print("R = ",round(R,2))