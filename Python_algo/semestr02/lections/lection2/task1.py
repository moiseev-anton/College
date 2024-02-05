if __name__ == "__main__":
    k = int(input("Введите число дней: "))
    k %= 3
    if k == 0:
        print("GCV")
    elif k == 1:
        print("VGC")
    else:
        print("CVG")

    # k %= 3
    # ans = "GCV" if k == 0 else ("VGC" if k == 1 else "CVG")
    # print(ans)

# 1 GCV
#   GVC
# 2 VGC
#   VCG
# 3 CVG
#   CGV
# 4 GCV

