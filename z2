def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

filename = "quote.txt"
word_count = count_words(filename)

if word_count is not None:
    print(f"Кількість слів у файлі '{filename}': {word_count}")
