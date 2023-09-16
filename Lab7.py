# Создаем базовый класс Shape
class Shape:
    def __init__(self):
        pass  # Конструктор не делает ничего, так как у Shape площадь равна нулю

    def area(self):
        return 0  # Метод area() возвращает ноль


# Создаем подкласс Square, который наследует от класса Shape
class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Вызываем конструктор базового класса Shape
        self.length = length

    def area(self):
        return self.length ** 2  # Рассчитываем площадь квадрата


# Пример использования классов
if __name__ == "__main__":
    shape = Shape()
    square = Square(5)

    print(f"Площадь фигуры: {shape.area()}")  # Выводим площадь фигуры (должно быть 0)
    print(f"Площадь квадрата: {square.area()}")  # Выводим площадь квадрата (должно быть 25)
