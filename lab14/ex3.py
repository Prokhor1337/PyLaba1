def analyze_journal():
    filename = "travel_journal.txt"
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл щоденника не знайдено.")
        return

    entries = content.split("-" * 40)
    entries = [e.strip() for e in entries if e.strip()]

    locations = set()
    total_words = 0

    for entry in entries:
        for line in entry.split("\n"):
            if line.startswith("Локація:"):
                loc = line.replace("Локація:", "").strip()
                locations.add(loc)
            elif line.startswith("Текст:"):
                text = line.replace("Текст:", "").strip()
                total_words += len(text.split())

    print(f"Загальна кількість записів: {len(entries)}")
    print(f"Кількість унікальних локацій: {len(locations)}")
    print(f"Загальна кількість слів у записах: {total_words}")

if __name__ == "__main__":
    analyze_journal()
