import random

categories = {
    "тварина": ["кіт", "слон", "лисиця"],
    "об'єкт": ["стілець", "телефон", "дзеркало"],
    "вигадане": ["дракон", "русалка", "невидимка"]
}

fake_items = ["зебра", "торт", "шепіт", "тінь", "вітер", "вода"]

print("Спробуй вгадати, що я маю на увазі.")
print("Обери категорію: тварина / об'єкт / вигадане")
user_choice = input("Твій вибір: ").strip().lower()

if user_choice not in categories:
    print("промах. Але ти сам винен, що ускладнив собі гру, продовжуй")
    user_choice = random.choice(list(categories.keys()))

category = user_choice
secret_word = random.choice(categories[category])
attempts = 0
max_attempts = random.randint(4, 7)

print("Добре, почнімо. Що це може бути?..")

while True:
    guess = input("Твоя здогадка: ").strip().lower()
    attempts += 1

    if not guess.isalpha():
        print("щось не те, але ок, приму*смайлік із зневагою*")
        continue

    if guess == secret_word:
        responses = [
            "Це звучить переконливо... але чи точно?",
            "Хмм... цікаво. Дуже цікаво.",
            "Можливо, ти щось знаєш... або це випадковість."
        ]
        print(random.choice(responses))

        if random.choice([True, False]):
            break
        else:
            continue

    if guess in fake_items:
        print("Це щось знайоме... але не зовсім те.")
        continue

    hint_type = random.choice(["none", "category", "fake"])

    if hint_type == "category":
            print("Підказка: це з категорії '" + category + "'.")
    elif hint_type == "fake":
            print("Підказка: це точно не '" + random.choice(fake_items) + "'.")

    if guess in categories[category]:
        print("Можливо, це щось подібне...")
    else:
        print("Схоже на фантазію... хоча хто знає.")

    if random.randint(5, 8) == 3 or attempts >= max_attempts:
        print("Мабуть, досить.")
        break

print("\nБуло загадано:", secret_word)
if guess == secret_word:
    final_responses = [
        "Ти, можливо, вгадав. А може, і ні.",
        "Це справді був твій вибір?..",
        "Збіг? Інтуїція? Хтозна..."
    ]
    print(random.choice(final_responses))
else:
    final_responses = [
        "Це було нелегко... але правильна відповідь перед тобою.",
        "Тепер ти знаєш, що це було. Та чи змінилося щось?",
        "Гра завершена. Та чи справді ти програв?"
    ]
    print(random.choice(final_responses))
