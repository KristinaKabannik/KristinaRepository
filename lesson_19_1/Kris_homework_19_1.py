import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()  # Якщо status code = 200, парсимо JSON
    photos = data.get('photos', [])

    if photos:
        os.makedirs('photos')   # Створюємо директорію для збереження фото

        for i, photo in enumerate(photos, start=1):
            photo_url = photo['img_src']
            photo_data = requests.get(photo_url).content  # Завантажуємо фото
            photo_filename = f'photos/photo{i}.jpg'

            with open(photo_filename, 'wb') as f:   # Зберігаємо фото
                f.write(photo_data)

            print(f'Saved: {photo_filename}')

    else:
        print('Фото не знайдене')
else:
    print(f"Очікуваний статус код має бути 200, а актуальний: {response.status_code}")
