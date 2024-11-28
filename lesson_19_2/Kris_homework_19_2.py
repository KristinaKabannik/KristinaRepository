import requests

base_url = 'http://127.0.0.1:8080'

file_path = "Flowers.jpg"

# 1. POST- завантажуємо зображення
upload_url = f'{base_url}/upload'

with open(file_path, 'rb') as img:
    files = {'image': img}
    response = requests.post(upload_url, files=files)

if response.status_code == 201:  # Перевірка статус коду
    json_response = response.json()
    image_url = json_response['image_url']
    print(f'Зображення завантажено. URL: {image_url}')
else:
    print(f'Помилка завантаження зображення: {response.text}')
    exit()

# 2. GET - отримуємо посилання на файл
filename = image_url.split('/')[-1]  # Отримуємо ім'я файлу з URL
get_url = f'{base_url}/image/{filename}'

headers = {'Content-Type': 'text'}  # Вказуємо тип даних для отримання URL
response = requests.get(get_url, headers=headers)

if response.status_code == 200:   # Перевірка статус коду
    json_response = response.json()
    print(f"Посилання на зображення: {json_response['image_url']}")
else:
    print(f'Помилка отримання зображення: {response.text}')

# 3. DELETE - видаляємо зображення
delete_url = f'{base_url}/delete/{filename}'
response = requests.delete(delete_url)

if response.status_code == 200:    # Перевірка статус коду
    print(f"Зображення '{filename}' видалено")
else:
    print(f'Помилка видалення зображення: {response.text}')
