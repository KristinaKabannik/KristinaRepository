import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logging.basicConfig(filename='test_search.log', level=logging.INFO,      # Налаштування логування
                    format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope='class')      # Фікстура для аутентифікації
def authenticated_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    response = session.post(auth_url, auth=HTTPBasicAuth('test_user', 'test_pass'))    # Аутентифікація
    assert response.status_code == 200

    access_token = response.json()['access_token']   # Отримання токену
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    return session


@pytest.mark.parametrize("sort_by, limit", [   # Параметризація тестів з різними значеннями sort_by і limit
    ("price", 8),
    ("year", 7),
    ("engine_volume", 4),
    ("price", 5),
    ("brand", 9)
])
def test_car_search(authenticated_session, sort_by, limit):
    params = {}       # Формування параметрів запиту
    if sort_by:
        params['sort_by'] = sort_by
    if limit:
        params['limit'] = limit

    search_url = f"{BASE_URL}/cars"

    response = authenticated_session.get(search_url, params=params)    # GET запит для пошуку автомобілів
    assert response.status_code == 200

    cars = response.json()

    logging.info(f"Параметри тесту: sort_by={sort_by}, limit={limit}, повернено {len(cars)} автомобілів.")   # Логування результатів



