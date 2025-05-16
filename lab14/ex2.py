def search_notes():
    filename = "travel_journal.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл щоденника не знайдено.")
        return

    query = input("Введіть дату (YYYY-MM-DD) або ключове слово для пошуку: ").strip()
    entries = content.split("-" * 40)

    found = False
    for entry in entries:
        if query in entry:
            print("\nЗнайдений запис:\n")
            print(entry.strip())
            found = True

    if not found:
        print("Записів за цим запитом не знайдено.")

if __name__ == "__main__":
    search_notes()
