character = "тесла"
hints = [
    "Він був інженером.",
    "Його ім'ям названа компанія.",
    "Жив у 19-20 століттях.",
    "Працював з електрикою."
]

print("Вгадай відому особу. У тебе 4 підказки.")

for i in range(len(hints)):
    show_hint = input("Хочеш підказку? (так/ні): ").strip().lower()
    if show_hint == "так":
        print("Підказка:", hints[i])

    guess = input("Хто це?: ").strip().lower()
    if guess == character:
        print("Вітаю! Ви вгадали!")
        break
    else:
        print("Ні, це не він.")

if guess != character:
    print(f"Гра завершена. Правильна відповідь: {character.capitalize()}.")
