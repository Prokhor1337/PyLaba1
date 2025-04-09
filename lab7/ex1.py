import random

objects = ["кіт", "монітор", "дракон", "стілець", "привид"]
answer = random.choice(objects)
attempts = 0
max_attempts = 6

print("Вгадай, хто або що я. Це може бути живе, неживе або вигадане.")

while attempts < max_attempts:
    guess = input("Ваша здогадка: ").strip().lower()
    attempts += 1

    if not guess.isalpha():
        print("Введіть одне слово без цифр і символів.")
        continue

    if guess == answer:
        print(f"Правильно! Це був(а) {answer}. Ви вгадали за {attempts} спроб.")
        break
    else:
        print("Неправильно. Спробуйте ще.")

if guess != answer:
    print(f"На жаль, ви не вгадали. Це був(а) {answer}.")
