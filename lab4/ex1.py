import tkinter as tk

def add_to_expression(symbol):
    entry_field.insert(tk.END, symbol)

def calculate():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except Exception:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Помилка")

def clear():
    entry_field.delete(0, tk.END)

window = tk.Tk()
window.title("Калькулятор")

entry_field = tk.Entry(window, width=25, font=('Arial', 18), borderwidth=2, relief="ridge")
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        action = calculate
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: add_to_expression(x)
    
    button = tk.Button(window, text=text, width=5, height=2, font=('Arial', 18), command=action)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(6):
    window.rowconfigure(i, weight=1)
for i in range(4):
    window.columnconfigure(i, weight=1)

window.mainloop()
