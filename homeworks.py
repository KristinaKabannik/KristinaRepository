# Task 1
# Initial task - 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими.
''' Виконання за допомогою функції:'''

def new_list(lst1):
    lst2 = [element for element in lst1 if isinstance(element, str)] #проходимо по списку і визначаємо, чи є елемент стрінговим
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
lst2 = new_list(lst1)
print(lst2)





# Task 2
# Initial task - 6.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
''' Виконання за допомогою функції:'''

def sum_ev_numb(lst):
    even_numbers_sum = sum(number for number in lst if number % 2 == 0)  # проходимо по списку і сумуємо парні числа
    return even_numbers_sum

lst = [1, 2, 3, 6, 9, 5, 6, 7, 8]
even_numbers_sum = sum_ev_numb(lst)
print(f"Сума усіх парних чисел: {even_numbers_sum}")





# Task 3
# Initial task - 6.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()
''' Виконання за допомогою функції:'''

def check_unique_symbols():
    symbols = input("Input some symbols: ")  # вводимо строку
    unique_symbols = set(symbols)       # Створюємо множину для зберігання унікальних символів

    if len(unique_symbols) > 10:       # Порівнюємо кількість унікальних символів
        print(True)
    else:
        print(False)

check_unique_symbols()






# Task 4
# Initial task - 6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися,
# якщо користувач ввів слово без букви "h".
''' Виконання за допомогою функції:'''

def need_h():
    while True:
        word = input("Введіть слово, в якому є буква 'h'(or 'H'): ")    # вводимо слово
        if 'h' in word.lower():   # Перевіряємо, чи є в слові 'h' або 'H'
            print("Правильно! Буква 'h' присутя")
            break  # Завершуємо цикл, якщо умова виконана
        else:
            print("Відсутня буква 'h' ('H'). Введіть слово ще раз:")


need_h()