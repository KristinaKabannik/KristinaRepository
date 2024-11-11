import csv

file1 = 'r-m-c.csv'
file2 = 'random-michaels.csv'
result_file = 'result_Kabannyk.csv'

def delete_duplicates(file1, file2, result_file):
    unique_rows = set()

    # Читаємо файл 'r-m-c.csv'
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        for row in reader1:
            unique_rows.add(tuple(row))  # Додаємо кожен рядок

    # Читаємо файл 'random-michaels.csv'
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        for row in reader2:
            unique_rows.add(tuple(row))  # Додаємо кожен рядок

    # Записуємо унікальні рядки в файл 'result_Kabannyk.csv'
    with open(result_file, 'w', newline='') as result:
        writer = csv.writer(result)
        for row in unique_rows:
            writer.writerow(row)


delete_duplicates(file1, file2, result_file)

print(f"Результат записано у файл {result_file}")
