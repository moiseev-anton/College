if __name__ == "__main__":
    weights = list(map(int, input("Введите массы толстяков через пробел: ").split()))
    min_w = 94
    max_w = 727
    result = 0
    for w in weights:
        if w < min_w or w > max_w:
            result = "Error"
            break
        result = max(result, w)
    print(result)


    # min_w, max_w = 94, 727
    # ans = max(weights) if all(min_w <= w <= max_w for w in weights) else "Error"
    # print(ans)
