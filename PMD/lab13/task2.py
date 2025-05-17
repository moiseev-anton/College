def uppercase(func):
    def wrapper(*args):
        func(*map(str.upper, args))
    return wrapper


print = uppercase(print)


if __name__ == '__main__':
    print(input())


