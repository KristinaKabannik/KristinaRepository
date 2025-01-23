# Базовий образ Python
FROM python:3.13

# Встановлюємо залежності
RUN pip install pytest psycopg2-binary
RUN pip install pytest-allure-adaptor allure-pytest

# Додаємо код додатку
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Вказуємо команду для запуску тестів
CMD ["pytest" "test_database"]
