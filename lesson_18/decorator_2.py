# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

import functools
def exception_catch(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            return result
        except Exception as exc:
            print(f"Виникла помилка у функції {func.__name__}: {exc}")  # Логуємо та оброблюємо помилку
            return None
    return wrapper

@exception_catch    # Використовуємо декоратор
def rectangle_area(a, b):
    return a * b

result = rectangle_area(5, 12)   # Викликаємо функцію з правильними аргументами
print(f"1.Площа прямокутника: {result}")

result = rectangle_area('abc', 12)  # Викликаємо функцію з неправильними аргументами
print(f"2.Виникла помилка: {result} - неправильний тип даних аргументів")
