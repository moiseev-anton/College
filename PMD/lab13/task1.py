from functools import wraps


def password(pswd: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user_input = input("Введите пароль: ")
            if user_input == pswd:
                return func(*args, **kwargs)
            else:
                print("Пароль не верный!")
                return None
        return wrapper
    return decorator


@password("1234")
def gcd(a: int, b: int) -> int:
    """НОД по алгоритму Евклида"""
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    result = gcd(48, 18)
    if result is not None:
        print(f"НОД: {result}")



