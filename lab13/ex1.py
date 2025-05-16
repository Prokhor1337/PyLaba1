import json
from tkinter import messagebox

def load_phones_from_json(path="data/phones.json"):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data.get("data", [])
            return data
    except Exception as e:
        messagebox.showerror("Помилка", f"Не вдалося зчитати JSON: {e}")
        return []
