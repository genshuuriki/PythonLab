import os
from bs4 import BeautifulSoup

def create_sample_html_file():
    # Создаем путь к рабочему столу
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, "sample.html")

    # Создаем HTML файл с разнообразием тегов
    with open(file_path, "w") as file:
        file.write("""
            <html>
                <head>
                    <title>Пример HTML</title>
                </head>
                <body>
                    <h1>Заголовок 1</h1>
                    <p>Первый абзац</p>
                    <p>Второй абзац</p>
                    <div>
                        <p>Третий абзац</p>
                    </div>
                    <article>
                        <p>Абзац внутри статьи</p>
                    </article>
                </body>
            </html>
        """)

    return file_path

def count_html_tags(html_file_path, tag_name):
    # Открываем HTML файл и парсим его
    with open(html_file_path, "r") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    # Используем метод find_all для поиска всех тегов с указанным именем
    tags = soup.find_all(tag_name)

    # Фильтруем только те теги, которые имеют как открывающую, так и закрывающую часть
    valid_tags = [tag for tag in tags if tag.text.strip() != '']

    # Возвращаем количество найденных тегов
    return len(valid_tags)

if __name__ == "__main__":
    # Создаем пример HTML файла на рабочем столе
    html_file_path = create_sample_html_file()

    # Указываем имя тега, который нужно подсчитать
    tag_name = "p"

    # Вызываем функцию для подсчета тегов
    tag_count = count_html_tags(html_file_path, tag_name)

    # Выводим результат
    print(f"Количество тегов '{tag_name}' в HTML файле: {tag_count}")
