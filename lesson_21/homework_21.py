import re
from datetime import datetime
import logging

logging.basicConfig(filename='hb_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') #логер

def parse_file(file_path, key):
    filtered_log = []
    with open(file_path, 'r') as file:
        for line in file:
            if key in line:
                timestamp_pos = line.find("Timestamp ") + len("Timestamp ") #шукаємо час у строці
                timestamp = line[timestamp_pos:timestamp_pos + 8]  # Отримуємо час у форматі HH:MM:SS
                filtered_log.append(timestamp)
    return filtered_log

def analyze_file(timestamps):
    for i in range(1, len(timestamps)):
        time_format = "%H:%M:%S"
        current_time = datetime.strptime(timestamps[i], time_format)
        previous_time = datetime.strptime(timestamps[i-1], time_format)
        time_difference = (current_time - previous_time).total_seconds()  #різниця в секундах

        if 31 < time_difference < 33:
            logging.warning(f"Heartbeat delay is {time_difference} seconds between {timestamps[i-1]} and {timestamps[i]}")
        elif time_difference >= 33:
            logging.error(f"Heartbeat delay is {time_difference} seconds between {timestamps[i-1]} and {timestamps[i]}")

key = "TSTFEED0300|7E3E|0400" #фільтруємо логи
log_file_path = "hblog.txt"
timestamps = parse_file(log_file_path, key)  # Отримуємо відфільтровані логи з файла
analyze_file(timestamps)  # Аналізуємо інтервали сигналів
