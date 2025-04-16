from collections import Counter

text = input("Введи будь-який текст: ")

counter = Counter(text)

filtered = {char: count for char, count in counter.items() if count > 1}

print("Символи, які зустрічаються більше одного разу:")
for char, count in filtered.items():
    print(f"'{char}': {count} раз(и)")
