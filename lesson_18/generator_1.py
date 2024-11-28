# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers_generator(N):
    for num in range(0, N + 1, 2):  # перебираємо числа з кроком 2
        yield num  # повертає парне число при кожній ітерації

N = 25
for num in even_numbers_generator(N):
    print(num)
