# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
from math import remainder

alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)



# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті

all_lapky = [char for char in alice_in_wonderland if char == "'"]
print("Всі символи одинарні лапки в тексті:", all_lapky)



# task 03 == Виведіть змінну alice_in_wonderland на друк

print (alice_in_wonderland)



"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total = black_sea + azov_sea
print("Загальна площа:", total, "км2")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
storage_1_2_3 = 375291
storage1_2 = 250449
storage2_3 = 222950

storage_3 = storage_1_2_3 - storage1_2
storage_1 = storage_1_2_3 - storage2_3
storage_2 = storage_1_2_3 - (storage_1 + storage_3)
print("Кількість товарів на складі 1:", storage_1, "шт")
print("Кількість товарів на складі 2:", storage_2, "шт")
print("Кількість товарів на складі 3:", storage_3, "шт")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

months = 18
payment = 1179
total_cost = months * payment
print(f"Вартість комп'ютера: {total_cost} грн")



# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

a1 = 8019
a2 = 8
remains_a = a1 % a2

b1 = 9907
b2 = 9
remains_b = b1 % b2

c1 = 2789
c2 = 5
remains_c = c1 % c2

d1 = 7248
d2 = 6
remains_d = d1 % d2

e1 = 7128
e2 = 5
remains_e = e1 % e2

f1 = 19224
f2 = 9
remains_f = f1 % f2

print(f"Остача від відення - приклад a: {remains_a}")
print(f"Остача від відення - приклад b: {remains_b}")
print(f"Остача від відення - приклад c: {remains_c}")
print(f"Остача від відення - приклад d: {remains_d}")
print(f"Остача від відення - приклад e: {remains_e}")
print(f"Остача від відення - приклад f: {remains_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_quantity = 4
big_pizza_cost = 274
mid_pizza_quantity = 2
mid_pizza_cost = 218
juice_quintity = 4
juice_cost = 35
cake_quintity = 1
cake_cost = 350
water_quintity = 3
water_cost = 21

total_cost = (big_pizza_cost * big_pizza_quantity + mid_pizza_cost * mid_pizza_quantity + juice_cost * juice_quintity + cake_cost * cake_quintity + water_cost * water_quintity)
print(f"Кількість грошей: {total_cost} грн")



# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

photo = 232
page = 8
page_quintity = photo / page
print(f"Кількість сторінок для фотографій: {int(page_quintity)} шт")




# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
consumption = 9
each = 100
tank = 48
gas_strength = distance * consumption / each
refueling = gas_strength / tank

print("1 - Знадобиться бензину для подорожі Харків-Будапешт:", int(gas_strength), "л")
print("2 - Щонайменше необхідно буде заїхати на заправку:", int(refueling), "разів")
