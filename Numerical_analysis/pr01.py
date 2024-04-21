# Функция нахождения относительной погрешности
def find_otn_pogr(real, proxy):
    abs_pogr = abs(real - proxy)
    return abs_pogr / abs(proxy) * 100

# Программа
if __name__ == "__main__":
    # Присваивание значений
    a_real = 5/13
    a_proxy = 0.385
    b_real = 13 ** 0.5
    b_proxy = 3.61

    # Нахождение относительных погрешностей для a и b
    a_otn_pogr = find_otn_pogr(a_real, a_proxy)
    b_otn_pogr = find_otn_pogr(b_real, b_proxy)

    # Вывод относительных погрешностей для a и b (для наглядности)
    print(f"Относительная погрешность a = {a_otn_pogr:.4f}")
    print(f"Относительная погрешность b = {b_otn_pogr:.4f}")

    # Сравнение
    if a_otn_pogr < b_otn_pogr:
        print("Первое точнее")
    elif a_otn_pogr > b_otn_pogr:
        print("Второе точнее")
    else:
        print("Точность равна")

