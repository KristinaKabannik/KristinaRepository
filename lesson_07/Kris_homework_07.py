# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True:   #заміняємо на while Truе
        result = number * multiplier
        if  result > 25:   #заміняємо вказаний тип з str на int
            break # якщо досягнута умова result > 25, виходимо з циклу
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1  # the name of variable is not initialized, therefore it is changed from multi to multiplier

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def two_numbers_sum(number1, number2):
    return number1 + number2

result = two_numbers_sum(1,2)
print("Сума двох чисел:", result)



# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers_list):
    return sum(numbers_list)/len(numbers_list)

number_list = [1,2,3,4]
print(f"Середнє арифметичне списку чисел", number_list, ":", arithmetic_mean(number_list))
print(f"Середнє арифметичне списку чисел заданого ренджу (20):", arithmetic_mean(range(20)))



# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
#Case with input:
def change_sequence(some_row):
    some_row = input('Введіть речення: ')

    return some_row[::-1]
result = change_sequence(some_row="")
print("Речення у зворотньому порядку:", result)


#Case with predefined sentence:
def change_sequence(some_row):
    return some_row[::-1]

result = change_sequence("Hello world!")
print("Речення у зворотньому порядку:", result)


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def define_longest_word(words_list):
    longest_word = max(words_list, key=len)
    return longest_word

words_list = ['cat', 'dog', 'octopus', 'horse', 'rabbit']
result = define_longest_word(words_list)
print("Найдовше слово у спику:", result)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
result = find_substring(str1, str2)
print("Індекс першого входження другого рядка у перший рядок", result) # поверне 7

# str1 = "The quick brown fox jumps over the lazy dog"
# str2 = "cat"
# result = find_substring(str1, str2)
# print("Індекс першого входження другого рядка у перший рядок", result) # поверне -1


# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Task 7
# Initial task - 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими.

# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
# lst2 = [element for element in lst1 if isinstance(element, str)]
# print(lst2)

''' Виконання за допомогою функції:'''

def new_list(lst1):
    lst2 = [element for element in lst1 if isinstance(element, str)] #проходимо по списку і визначаємо, чи є елемент стрінговим
    return lst2

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
lst2 = new_list(lst1)
print(lst2)



# Task 8
# Initial task - 6.4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

# lst = [1, 2, 3, 6, 9, 5, 6, 7, 8]
# even_numbers_sum = sum(number for number in lst if number % 2 == 0)
# print(f"Сума усіх парних чисел: {even_numbers_sum}")

''' Виконання за допомогою функції:'''

def sum_ev_numb(lst):
    even_numbers_sum = sum(number for number in lst if number % 2 == 0)  # проходимо по списку і сумуємо парні числа
    return even_numbers_sum

lst = [1, 2, 3, 6, 9, 5, 6, 7, 8]
even_numbers_sum = sum_ev_numb(lst)
print(f"Сума усіх парних чисел: {even_numbers_sum}")


#Task 9
# Initial task - 6.1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

# symbols = input('Input some symbols: ')
# unique_symbols = set(symbols)
# unique_symbols_count = len(unique_symbols)
# if unique_symbols_count > 10:
#     print(True)
# else:
#     print(False)

''' Виконання за допомогою функції:'''

def check_unique_symbols():
    symbols = input("Input some symbols: ")  # вводимо строку
    unique_symbols = set(symbols)       # Створюємо множину для зберігання унікальних символів

    if len(unique_symbols) > 10:       # Порівнюємо кількість унікальних символів
        print(True)
    else:
        print(False)

check_unique_symbols()



#Task 10
# Initial task - 6.2
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі). Цикл не повинен завершитися,
# якщо користувач ввів слово без букви "h".

# while True:
#     word = input("Введіть слово, в якому є буква 'h'(or 'H'): ")
#     if 'h' in word.lower():
#         print("Правильно! Буква 'h' присутя")
#         break
#     else:
#         print("Відсутня буква 'h' ('H'). Введіть слово ще раз:")

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