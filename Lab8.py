from PIL import Image


def rotate_image(image_path):
    try:
        # Открываем изображение
        img = Image.open(image_path)

        # Вращаем изображение на 90 градусов
        rotated_img = img.rotate(90, expand=True)

        # Сохраняем изображение по тому же пути
        rotated_img.save(image_path)

        print(f"Изображение {image_path} успешно повернуто на 90 градусов и сохранено.")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


# Укажите путь к изображению, которое вы хотите повернуть
image_path = "C:\\Users\\savel\\Downloads\\Shredder.webp"  # Замените это на фактический путь к изображению
rotate_image(image_path)
