# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

lst = [1, 2, 3, 6, 9, 5, 6, 7, 8]
even_numbers_sum = sum(number for number in lst if number % 2 == 0)
print(f"Сума усіх парних чисел: {even_numbers_sum}")