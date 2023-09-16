from datetime import datetime

def days_between_dates(date1, date2):
    # Проверяем, что оба объекта являются экземплярами datetime
    if not isinstance(date1, datetime) or not isinstance(date2, datetime):
        raise ValueError("Оба аргумента должны быть объектами datetime")

    # Рассчитываем разницу между двумя датами
    delta = abs(date1 - date2)

    # Извлекаем количество дней из разницы и возвращаем его по модулю
    return delta.days

# Пример использования функции
date1 = datetime(2023, 9, 1)
date2 = datetime(2023, 9, 16)
result = days_between_dates(date1, date2)
print(f"Число дней между датами: {result}")
