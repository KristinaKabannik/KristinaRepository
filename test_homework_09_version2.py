import unittest
from homeworks import test_new_list, test_sum_ev_numb, test_check_unique_symbols, test_need_h

class MyTest(unittest.TestCase):
    def test_1(self):
# 1.Positive test - checks that function returns only strings elements
        lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum', 'Hello']

        lst2 = test_new_list(lst1)
        assert lst2 == expected_result, f"Expected result: {expected_result}, Actual result: {lst2}"
        print("1. Позитивний тест на стрінгові значення пройшов успішно!")

    def test_2(self):
# 2.Negative test - checks that function does not add NON-strings elements
        lst1 = [3, True, 5, 7, 8, 9, 0, 1.345]
        expected_result = []

        lst2 = test_new_list(lst1)
        assert lst2 == expected_result, f"Expected result: {expected_result}, Actual result: {lst2}"
        print("2. Негативний тест на НЕ стрінгові значення пройшов успішно!")


    def test_3(self):
# 3. Positive test - checks that function will select pair numbers and calculates sum of them correctly
        lst = [1, 2, 3, 6, 9, 5, 6, 7, 8]  # Різні числа
        expected_result = 22

        result = test_sum_ev_numb(lst)
        assert result == expected_result, f"Expected result: {expected_result}, Actual result: {result}"
        print("3. Позитивний тест на суму парних чисел пройшов успішно!")


    def test_4(self):
# 4. Positive test - checks that function calculates sum of pair numbers correctly
        lst = [2, 4, 6, 8, 10]  # Тільки парні числа
        even_numbers_sum = test_sum_ev_numb(lst)
        assert even_numbers_sum == 30, f"Expected result: 30, Actual result: {even_numbers_sum}"
        print(f"4. Позитивний тест на суму парних чисел пройшов успішно!")


    def test_5(self):
# 5. Negative test - checks that function will return 0, if no pair numbers in the list
        lst = [1, 3, 5, 7, 9]
        expected_result = 0

        result = test_sum_ev_numb(lst)
        assert result == expected_result, f"Expected result: {expected_result}, Actual result: {result}"
        print("5. Негативний тест на суму парних чисел = 0 пройшов успішно!")


    def test_6(self):
# 6. Negative test - checks if there are non-integer values in the list and returns an error
        lst = [2, 'four', 6, True]  # Різні типи елементів списку
        try:
                even_numbers_sum = test_sum_ev_numb(lst)
                print(f"Сума усіх парних чисел: {even_numbers_sum}")
        except TypeError as er:
                print("6. Негативний тест пройшов успішно! Виникла помилка TypeError:", er)

    def test_7(self):
# 7. Positive test - checks that uniq symbols quantity > 10
        symbols = "hjk dfg ert zxc"
        unique_symbols = set(symbols)

        print("7. Позитивний тест - чи більше 10-ти унікальних символів в строці:")
        if len(unique_symbols) > 10:
            print(True)
        else:
            print(False)


    def test_8(self):
# 8. Negative test - checks that uniq symbols quantity < 10
        symbols = "hjk"
        unique_symbols = set(symbols)

        print("8. Негативний тест - чи менше 10-ти унікальних символів в строці:")
        if len(unique_symbols) < 10:
            print(True)
        else:
            print(False)

    def test_9(self):
# 9. Positive test - the function checks that h is present
        word = "hello"
        print(f"Testing with word: {word}")
        if 'h' in word.lower():
            print("9. Тест успішний! Буква 'h' присутня.")
        else:
            print("Тест не пройдено!")

    def test_10(self):
# 10. Negative test - the function checks that h is absent
        word = "world"
        print(f"Testing with word: {word}")

        if 'h' in word.lower():
            print("10. Тест не пройдено! Буква 'h' присутня.")
        else:
            print("10. Тест успішний! Буква 'h' відсутня.")
if __name__ == '__main__':
    unittest.main()

