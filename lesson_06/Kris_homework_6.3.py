# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
lst2 = [element for element in lst1 if isinstance(element, str)]
print(lst2)