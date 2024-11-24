# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumbersIterator:
    def __init__(self, N):
        self.N = N
        self.current = 0  # починаємо з 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.N:  # якщо перевищуємо значення N
            raise StopIteration
        even_number = self.current  # зберігаємо поточне парне число
        self.current += 2           # переходимо до наступного парного числа
        return even_number

N = 22
even_numbers = EvenNumbersIterator(N)

for num in even_numbers:
    print(num)
