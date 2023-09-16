def extract_values_from_dict(input_dict):
    # Используем генераторное выражение для создания списка значений ключей словаря
    # Мы просто перебираем значения входного словаря и добавляем их в список
    values_list = [value for value in input_dict.values()]

    # Возвращаем список значений
    return values_lis


# Пример использования функции:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = extract_values_from_dict(my_dict)
print(result)  # Выведет: [1, 2, 3]
