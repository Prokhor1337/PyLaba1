def add_note():
    filename = \
        "travel_journal.txt"
    print("Додавання нового запису в щоденник мандрівника.")

    date = input("Введіть дату (формат YYYY-MM-DD): ")
    location = input("Введіть локацію: ")
    text = input("Введіть текст запису: ")

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"Дата: {date}\n")
        f.write(f"Локація: {location}\n")
        f.write(f"Текст: {text}\n")

    print(f"Запис успішно додано у файл '{filename}'")

if __name__ == "__main__":
    add_note()
