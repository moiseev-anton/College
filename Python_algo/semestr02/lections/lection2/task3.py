if __name__ == "__main__":
    a1, a2, a3 = map(int, input("Введите три числа через пробел: ").split())
    if a1 + a2 == a3 or a1 + a3 == a2 or a2 + a3 == a1:
        print("YES")
    else:
        print("NO")


    # ans = "YES" if a1 + a2 == a3 or a1 + a3 == a2 or a2 + a3 == a1 else "NO"
    # print(ans)
