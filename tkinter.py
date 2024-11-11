import tkinter as tk
from tkinter import ttk
from collections import Counter

class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Заголовок та розміри вікна
        self.title("Програма для розв'язання трьох задач")
        self.geometry("500x400")
        self.resizable(True, True)

        # Змінні для перемикання стилю
        self.dark_mode = False

        # Інформація про програму та автора
        self.create_info_section()

        # Перемикач стилю
        self.create_style_switch_button()

        # Вкладки для задач
        self.create_task_tabs()

    def create_info_section(self):
        info_frame = tk.Frame(self)
        info_frame.pack(pady=10)

        student_label = tk.Label(info_frame, text="Студент: Ім'я Прізвище, Кафедра: Програмування, Університет: KPI", font=("Arial", 10))
        student_label.pack()

        description_label = tk.Label(info_frame, text="Програма виконує три задачі:", font=("Arial", 12, "bold"))
        description_label.pack()

    def create_style_switch_button(self):
        switch_button = tk.Button(self, text="Перемкнути стиль", command=self.switch_style)
        switch_button.pack(pady=10)

    def switch_style(self):
        if not self.dark_mode:
            self.configure(bg="#2b2b2b")
            for widget in self.winfo_children():
                widget.configure(bg="#2b2b2b", fg="white")
        else:
            self.configure(bg="SystemButtonFace")
            for widget in self.winfo_children():
                widget.configure(bg="SystemButtonFace", fg="black")
        self.dark_mode = not self.dark_mode

    def create_task_tabs(self):
        tab_control = ttk.Notebook(self)
        tab_control.pack(expand=1, fill="both")

        # Створення вкладок для задач
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab3 = ttk.Frame(tab_control)

        tab_control.add(tab1, text='Задача 1')
        tab_control.add(tab2, text='Задача 2')
        tab_control.add(tab3, text='Задача 3')

        # Задача 1: Найкоротше слово
        self.create_task_1(tab1)

        # Задача 2: Підрахунок символів
        self.create_task_2(tab2)

        # Задача 3: Найчастіший символ
        self.create_task_3(tab3)

    def create_task_1(self, tab):
        def find_shortest_word_length():
            sentence = entry.get()
            words = sentence.split()
            if words:
                shortest_word = min(words, key=len)
                result_label.config(text=f"Довжина найкоротшого слова: {len(shortest_word)}")
            else:
                result_label.config(text="Введіть речення.")

        instruction_label = tk.Label(tab, text="Введіть речення:", font=("Arial", 10))
        instruction_label.pack(pady=5)

        entry = tk.Entry(tab, width=50)
        entry.pack(pady=5)

        button = tk.Button(tab, text="Знайти", command=find_shortest_word_length)
        button.pack(pady=5)

        result_label = tk.Label(tab, text="", font=("Arial", 10, "bold"))
        result_label.pack(pady=5)

    def create_task_2(self, tab):
        def count_character_occurrences():
            sequence = entry_seq.get()
            character = entry_char.get()
            count = sequence.count(character)
            result_label.config(text=f"Символ '{character}' зустрічається {count} раз(и).")

        instruction_label_seq = tk.Label(tab, text="Введіть послідовність символів:", font=("Arial", 10))
        instruction_label_seq.pack(pady=5)

        entry_seq = tk.Entry(tab, width=50)
        entry_seq.pack(pady=5)

        instruction_label_char = tk.Label(tab, text="Введіть символ для підрахунку:", font=("Arial", 10))
        instruction_label_char.pack(pady=5)

        entry_char = tk.Entry(tab, width=5)
        entry_char.pack(pady=5)

        button = tk.Button(tab, text="Порахувати", command=count_character_occurrences)
        button.pack(pady=5)

        result_label = tk.Label(tab, text="", font=("Arial", 10, "bold"))
        result_label.pack(pady=5)

    def create_task_3(self, tab):
        def find_most_frequent_char():
            text = entry.get()
            if text:
                most_common_char, count = Counter(text).most_common(1)[0]
                result_label.config(text=f"Найчастіший символ: '{most_common_char}', зустрічається {count} раз(и).")
            else:
                result_label.config(text="Введіть рядок.")

        instruction_label = tk.Label(tab, text="Введіть рядок:", font=("Arial", 10))
        instruction_label.pack(pady=5)

        entry = tk.Entry(tab, width=50)
        entry.pack(pady=5)

        button = tk.Button(tab, text="Знайти", command=find_most_frequent_char)
        button.pack(pady=5)

        result_label = tk.Label(tab, text="", font=("Arial", 10, "bold"))
        result_label.pack(pady=5)

# Запуск програми
if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
