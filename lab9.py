import tkinter as tk
import re

class RegexCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Regex Checker")

        self.create_widgets()

    def create_widgets(self):
        # Текстовое поле для ввода текста
        self.text_label = tk.Label(self.root, text="Введите текст:")
        self.text_label.pack()
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack()

        # Текстовое поле для ввода регулярного выражения
        self.regex_label = tk.Label(self.root, text="Введите регулярное выражение:")
        self.regex_label.pack()
        self.regex_entry = tk.Entry(self.root, width=50)
        self.regex_entry.pack()

        # Кнопка для выполнения проверки
        self.check_button = tk.Button(self.root, text="Проверить", command=self.check_regex)
        self.check_button.pack()

        # Поле для вывода результата
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def check_regex(self):
        # Получение введенного текста и регулярного выражения
        text = self.text_entry.get()
        regex_pattern = self.regex_entry.get()

        try:
            # Попытка скомпилировать регулярное выражение
            regex = re.compile(regex_pattern)

            # Попытка поиска совпадений в тексте
            match = regex.search(text)

            if match:
                # Если совпадение найдено, выделить его в тексте
                start, end = match.span()
                self.result_label.config(text=f"Совпадение найдено: {text[start:end]}", fg="green")
            else:
                self.result_label.config(text="Совпадений не найдено", fg="black")

        except re.error:
            # Если регулярное выражение некорректно, вывести сообщение об ошибке
            self.result_label.config(text="Ошибка в регулярном выражении", fg="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = RegexCheckerApp(root)
    root.mainloop()
