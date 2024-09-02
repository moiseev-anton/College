"""
Реализуйте с использованием tkinter программу, которая
при вводе пользователем стороны квадрата выводит его площадь
"""

import tkinter as tk

def calculate_area():
    try:
        side = float(entry.get())
        area = side * side
        result_label.config(text=f"Площадь квадрата: {area}")
    except ValueError:
        result_label.config(text="Введено некорректное число.")



root = tk.Tk()
root.title("Площадь квадрата")

# создаем виджеты
# текст
entry_label = tk.Label(root, text="Введите сторону квадрата:")
entry_label.pack()
# поле ввода
entry = tk.Entry(root)
entry.pack()
# кнопка
calculate_button = tk.Button(root, text="Вычислить площадь", command=calculate_area)
calculate_button.pack()
# текст с результатом
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

