import os
import sqlite3
import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox
from tkinter import ttk
import PyPDF2
from docx import Document
from ebooklib import epub

# Определяем путь к рабочему столу текущего пользователя
desktop_path = os.path.expanduser("~/Desktop")

# Полный путь к файлу базы данных на рабочем столе
db_file_path = os.path.join(desktop_path, "library.db")

# Проверяем, существует ли файл базы данных
if not os.path.exists(db_file_path):
    # Если файл не существует, создаем новую базу данных
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Создаем таблицу books
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre TEXT,
            file_path TEXT,
            book_data BLOB
        )
    ''')
    conn.commit()
else:
    # Если файл уже существует, просто подключаемся к нему
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

# Создаем основное окно приложения
root = tk.Tk()
root.title("Библиотека")

# Функция для добавления книги в базу данных
def add_book_to_database(title, author, genre, file_path):
    try:
        with open(file_path, 'rb') as file:
            book_data = file.read()
            cursor.execute(
                "INSERT INTO books (title, author, genre, file_path, book_data) VALUES (?, ?, ?, ?, ?)",
                (title, author, genre, file_path, book_data)
            )
            conn.commit()
        return True
    except Exception as e:
        tkinter.messagebox.showerror("Ошибка", f"Ошибка при добавлении книги в базу данных: {str(e)}")
        return False

# Функция для чтения книги EPUB
def read_epub(book_path):
    try:
        book = epub.read_epub(book_path)
        content = ""
        for item in book.get_items():
            if item.get_type() == epub.ITEM_DOCUMENT:
                content += item.get_content().decode('utf-8')
        return content
    except Exception as e:
        return str(e)

# Функция для чтения книги Word (docx)
def read_docx(book_path):
    try:
        doc = Document(book_path)
        content = ""
        for paragraph in doc.paragraphs:
            content += paragraph.text + "\n"
        return content
    except Exception as e:
        return str(e)

# Функция для чтения книги PDF
def read_pdf(book_path):
    try:
        pdf = PyPDF2.PdfReader(open(book_path, 'rb'))
        content = ""
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            content += page.extract_text()
        return content
    except Exception as e:
        return str(e)

# Функция для открытия выбранной книги
def open_selected_book():
    selected_item = tree.selection()
    if not selected_item:
        tkinter.messagebox.showwarning("Предупреждение", "Выберите книгу для чтения.")
        return

    # Получаем идентификатор книги из дерева
    selected_item = selected_item[0]
    book_id = tree.item(selected_item, 'values')[0]

    try:
        cursor.execute("SELECT title, author, genre, file_path, book_data FROM books WHERE id=?", (book_id,))
        row = cursor.fetchone()
        if row:
            title, author, genre, file_path, book_data = row
            file_extension = os.path.splitext(file_path)[-1].lower()

            if file_extension == '.epub':
                content = read_epub(file_path)
            elif file_extension == '.docx':
                content = read_docx(file_path)
            elif file_extension == '.pdf':
                content = read_pdf(file_path)
            else:
                tkinter.messagebox.showwarning("Предупреждение", "Неподдерживаемый формат книги.")
                return

            # Открываем окно для чтения книги
            book_window = tk.Toplevel(root)
            book_window.title(title)
            book_text = tk.Text(book_window)
            book_text.pack()
            book_text.insert(tk.END, content)
        else:
            tkinter.messagebox.showwarning("Предупреждение", "Книга не найдена в базе данных.")
    except Exception as e:
        tkinter.messagebox.showerror("Ошибка", f"Ошибка при чтении книги: {str(e)}")

# Создаем и настраиваем дерево для отображения списка книг
tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Genre"))
tree.heading("#1", text="Номер")
tree.heading("#2", text="Название")
tree.heading("#3", text="Автор")
tree.heading("#4", text="Жанр")
tree["show"] = "headings"
tree.pack()

# Функция для обновления списка книг в дереве
def refresh_book_list():
    # Очищаем дерево
    for item in tree.get_children():
        tree.delete(item)

    # Запрашиваем список книг из базы данных
    cursor.execute("SELECT id, title, author, genre FROM books")
    rows = cursor.fetchall()

    # Добавляем книги в дерево
    for row in rows:
        tree.insert("", "end", values=row)

# Вызываем функцию обновления списка книг при запуске приложения
refresh_book_list()

# Кнопка "Добавить книгу"
def add_book():
    file_path = filedialog.askopenfilename(filetypes=[("EPUB files", "*.epub"), ("Word files", "*.docx"), ("PDF files", "*.pdf")])
    if file_path:
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        if title and author:
            if add_book_to_database(title, author, genre, file_path):
                refresh_book_list()
                title_entry.delete(0, tk.END)
                author_entry.delete(0, tk.END)
                genre_entry.delete(0, tk.END)
                file_label.config(text=f"Выбран файл: {file_path}")
        else:
            tkinter.messagebox.showwarning("Предупреждение", "Заполните поля 'Название' и 'Автор'.")

add_button = tk.Button(root, text="Добавить книгу", command=add_book)
add_button.pack()

# Поля ввода для информации о книге
title_label = tk.Label(root, text="Название:")
title_label.pack()
title_entry = tk.Entry(root)
title_entry.pack()

author_label = tk.Label(root, text="Автор:")
author_label.pack()
author_entry = tk.Entry(root)
author_entry.pack()

genre_label = tk.Label(root, text="Жанр:")
genre_label.pack()
genre_entry = tk.Entry(root)
genre_entry.pack()

file_label = tk.Label(root, text="Выбран файл:")
file_label.pack()

# Кнопка "Читать книгу"
read_book_button = tk.Button(root, text="Читать книгу", command=open_selected_book)
read_book_button.pack()

# Запускаем приложение
root.mainloop()

# Закрываем соединение с базой данных при выходе из приложения
conn.close()
