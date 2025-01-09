from Class_NovaPoshta import NovaPoshta

def test_parcel_status():
    tracker = NovaPoshta()    # Ініціалізовуємо клас

    try:
        tracker.open_np_site()   # Відкриваємо сайт

        tracking_number = "20400000000000"

        tracker.input_tr_number(tracking_number)  # Вводимо номер накладної
        actual_status = tracker.get_status()   # Отримуємо статус посилки

        expected_status = "Посилка отримана"
        assert actual_status == expected_status, f"Очікуваний статус: {expected_status}, але актуальний статус: {actual_status}"
        print(f"Результат тесту: {actual_status}")
    finally:
        tracker.close()
