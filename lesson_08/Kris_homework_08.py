def sum_of_numbers_of_each_element(s):
    try:
        numbers = s.split(',')  # Розділяємо комою рядок з номерами

        each_element_sum = sum(int(n) for n in numbers)   # Переводимо все в int і знаходимо суму чисел
        return each_element_sum
    except ValueError:
        return "Не можу це зробити!" # Вертаємо повідомлення про помилку, якщо не вийде перевести дані в тип int

lst = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for s in lst:   # Проходимо по кожному елементу списку і виводимо результат
    result = sum_of_numbers_of_each_element(s)
    print(result)

