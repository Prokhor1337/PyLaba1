import random

options = ["камінь", "ножиці", "папір", "ящірка", "спок"]
win_conditions = {
    "камінь": ["ножиці", "ящірка"],
    "ножиці": ["папір", "ящірка"],
    "папір": ["камінь", "Спок"],
    "ящірка": ["папір", "спок"],
    "спок": ["ножиці", "камінь"]
}

player_choice = input("Оберіть: камінь, ножиці, папір, ящірка, спок: ")
computer_choice = random.choice(options)

if player_choice not in options:
    print("Помилка! Невірний вибір.")
elif player_choice == computer_choice:
    print(f"Нічия! Обидва вибрали {player_choice}.")
elif computer_choice in win_conditions[player_choice]:
    print(f"Ви виграли! {player_choice} перемагає {computer_choice}.")
else:
    print(f"Ви програли! {computer_choice} перемагає {player_choice}.")
