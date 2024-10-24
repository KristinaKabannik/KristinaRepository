from homeworks import new_list, sum_ev_numb, check_unique_symbols, need_h

# Позитивний тест на функцію new_list
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 1.345, 'Hello']
expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum', 'Hello']

lst2 = new_list(lst1)
assert lst2 == expected_result, f"Expected result: {expected_result}, Actual result: {lst2}"
print("Позитивний тест пройшов успішно!")

