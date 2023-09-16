def count_numbers(data):
    # Инициализируем счетчики для целых чисел и чисел с плавающей точкой
    int_count = 0
    float_count = 0

    # Проходим по каждому элементу в списке
    for item in data:
        # Проверяем тип элемента
        if isinstance(item, int):
            # Если элемент - целое число, увеличиваем счетчик целых чисел
            int_count += 1
        elif isinstance(item, float):
            # Если элемент - число с плавающей точкой, увеличиваем счетчик чисел с плавающей точкой
            float_count += 1

    # Возвращаем кортеж с количеством целых чисел и чисел с плавающей точкой
    return int_count, float_count

# Пример использования функции
my_list = [1, 2.5, 3, 4.0, 5.7, "hello"]
int_count, float_count = count_numbers(my_list)
print("Количество целых чисел:", int_count)
print("Количество чисел с плавающей точкой:", float_count)
