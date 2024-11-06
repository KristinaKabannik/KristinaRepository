import json
import logging

files_list = [
    "localizations_en.json",
    "localizations_ru.json",
    "login.json",
    "swagger.json"]

# Логер:
logging.basicConfig(
    filename='json__Kabannyk.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validate_files_on_json_format(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            json.load(file)                  # Завантажуємо JSON
        print(f"The following file is a VALID json: {file_name}")
    except json.JSONDecodeError as err:
        logging.error(f"INVALID json: {file_name}: {err}")  # Логування помилки
        print(f"The following file is an INVALID json: {file_name}")

for file in files_list:
    validate_files_on_json_format(file)

