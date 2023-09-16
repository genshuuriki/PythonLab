import numpy as np  # Импортируем библиотеку NumPy

def calculate_determinant(matrix):
    try:
        # Проверяем, является ли входной аргумент матрицей (двумерным массивом)
        if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
            raise ValueError("Входной аргумент должен быть двумерной матрицей")

        # Проверяем, является ли матрица квадратной (количество строк равно количеству столбцов)
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("Матрица должна быть квадратной")

        # Вычисляем определитель матрицы с помощью функции det из библиотеки NumPy
        determinant = np.linalg.det(matrix)

        return determinant

    except Exception as e:
        return str(e)  # Возвращаем сообщение об ошибке в случае исключения

# Пример использования функции:
matrix = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

result = calculate_determinant(matrix)
if isinstance(result, str):
    print(result)  # Выводим сообщение об ошибке, если функция вернула строку
else:
    print(f"Определитель матрицы:\n{result}")
