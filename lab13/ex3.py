import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tasks.task2_search import search_and_sort

def save_to_db(phone):
    conn = sqlite3.connect("phones.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price INTEGER,
            rating REAL,
            reviews INTEGER,
            description TEXT
        )
    """)
    cursor.execute("INSERT OR IGNORE INTO favorites VALUES (?, ?, ?, ?, ?, ?)", (
        phone["id"], phone["title"], phone["price"],
        phone["rating"], phone["reviews"], phone["description"]
    ))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успіх", f"'{phone['title']}' додано до бази даних!")

def create_gui(phones):
    def on_search(*args):
        keyword = search_entry.get()
        sort_by = sort_var.get()
        results = search_and_sort(phones, keyword, sort_by)
        listbox.delete(0, tk.END)
        for phone in results:
            listbox.insert(tk.END, phone["title"])
        update_details(None)

    def update_details(event):
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            phone = search_and_sort(phones, search_entry.get(), sort_var.get())[index]
            details_var.set(
                f"Назва: {phone['title']}\nЦіна: {phone['price']} грн\nРейтинг: {phone['rating']}\n"
                f"Відгуків: {phone['reviews']}\nОпис: {phone['description']}"
            )
            save_button.config(command=lambda: save_to_db(phone))
        else:
            details_var.set("")

    root = tk.Tk()
    root.title("Телефони з JSON")

    tk.Label(root, text="Пошук:").grid(row=0, column=0, sticky="w")
    search_entry = tk.Entry(root)
    search_entry.grid(row=0, column=1, sticky="we")

    sort_var = tk.StringVar(value="price")
    sort_menu = ttk.Combobox(root, textvariable=sort_var, values=["price", "rating", "reviews"], state="readonly")
    sort_menu.grid(row=0, column=2)

    listbox = tk.Listbox(root, height=10)
    listbox.grid(row=1, column=0, columnspan=3, sticky="nsew")

    scrollbar = tk.Scrollbar(root, orient="vertical", command=listbox.yview)
    scrollbar.grid(row=1, column=3, sticky="ns")
    listbox.config(yscrollcommand=scrollbar.set)

    details_var = tk.StringVar()
    details_label = tk.Label(root, textvariable=details_var, justify="left", anchor="w")
    details_label.grid(row=2, column=0, columnspan=3, sticky="w")

    save_button = tk.Button(root, text="Зберегти до бази")
    save_button.grid(row=3, column=0, columnspan=3, pady=5)

    search_entry.bind("<KeyRelease>", on_search)
    sort_menu.bind("<<ComboboxSelected>>", on_search)
    listbox.bind("<<ListboxSelect>>", update_details)

    root.grid_columnconfigure(1, weight=1)
    root.mainloop()
