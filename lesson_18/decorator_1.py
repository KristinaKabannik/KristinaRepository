# Напишіть декоратор, який логує аргументи та результати викликаної функції.
import functools

def log_arguments_and_results(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Функція {fn.__name__} має аргументи: {args}")  # Логуємо аргументи функції
        result = fn(*args, **kwargs)

        print(f"Результат функції {fn.__name__}: {result}")    # Логуємо результат функції
        return result

    return wrapper

@log_arguments_and_results   # Використовуємо декоратор

def rectangle_area(a, b):
    return a * b
result = rectangle_area(5, 12)  # Викликаємо функцію з декоратором
