# Базовий образ Python
FROM python:3.9-slim

# Встановлюємо залежності
RUN pip install psycopg2 pytest selenium webdriver-manager

# Додаємо код додатку
COPY . /app

# Встановлюємо робочу директорію
WORKDIR /app

# Вказуємо команду для запуску тестів
CMD ["test_database.py"]
