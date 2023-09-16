def sum_of_elements(input_list):
    # Проверяем, что входной список содержит ровно три элемента
    if len(input_list) != 3:
        raise ValueError("Входной список должен содержать ровно три элемента")

    # Считаем сумму элементов списка и возвращаем результат
    result = sum(input_list)
    return result


# Пример использования функции:
input_list = [2, 5, 8]
total_sum = sum_of_elements(input_list)
print("Сумма элементов списка:", total_sum)
