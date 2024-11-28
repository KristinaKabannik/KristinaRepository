# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseOutputIterator:
    def __init__(self, list):
        self.list = list
        self.index = len(list)  # починаємо з останнього індексу

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration  # зупиняємось, коли індекс дійшов до нульового елементу списку
        self.index -= 1
        return self.list[self.index]  # повертаємо елемент за поточним індексом


proposed_list = [1, 3, 7, 10, 12, 13, 18, 20, 38]
reverse_output = ReverseOutputIterator(proposed_list)

for el in reverse_output:
    print(el)
