# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_generator(N):
    a, b = 0, 1  # Початкові два числа послідовності Фібоначчі
    while a <= N:
        yield a
        a, b = b, a + b  # Оновлюємо числа за формулою Фібоначчі

N = 100
for num in fibonacci_generator(N):
    print(num)
