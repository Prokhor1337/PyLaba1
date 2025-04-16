text = input("Введи будь-який рядок: ").lower()

vowels = "аеєиіїоуюяaeiou"
vowel_list = [char for char in text if char in vowels]

print("Знайдено голосних:", len(vowel_list))
print("Ось вони:", vowel_list)
