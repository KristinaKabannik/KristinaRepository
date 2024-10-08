# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()


symbols = input('Input some symbols: ')
unique_symbols = set(symbols)
unique_symbols_count = len(unique_symbols)
if unique_symbols_count > 10:
    print(True)
else:
    print(False)