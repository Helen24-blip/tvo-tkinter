import tkinter as tk


# Функция для вставки символов в поле ввода
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(button))


# Функция для очистки поля ввода
def clear():
    entry.delete(0, tk.END)


# Функция для выполнения вычисления
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")


# Создание основного окна приложения
root = tk.Tk()
root.title("Простой калькулятор")

# Поле для ввода и отображения результата
entry = tk.Entry(root, width=35, borderwidth=5, font=("Helvetica", 18))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Создание кнопок для калькулятора
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Размещение кнопок на сетке
row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':  # Кнопка очистки
        tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 18), command=clear).grid(row=row_val,
                                                                                                   column=col_val)
    elif button == '=':  # Кнопка равно
        tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 18), command=evaluate).grid(row=row_val,
                                                                                                      column=col_val)
    else:  # Остальные кнопки
        tk.Button(root, text=button, padx=20, pady=20, font=("Helvetica", 18), command=lambda b=button: click(b)).grid(row=row_val, column=col_val)


    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Запуск основного цикла приложения
root.mainloop()
