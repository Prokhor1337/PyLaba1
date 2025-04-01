import random

code = random.randint(100, 999)
attempts = 5

print("Зламайте код сейфу! У вас 5 спроб.")

while attempts > 0:
    try:
        user_input = int(input("Введіть тризначний код: "))

        if user_input == code:
            print("Вітаємо! Ви зламали сейф!")
            break
        elif user_input < code:
            print("Код більший!")
        else:
            print("Код менший!")

        attempts -= 1
        print(f"Залишилось спроб: {attempts}")

    except ValueError:
        print("Помилка! Введіть число.")

if attempts == 0:
    print(f"Ви програли! Код був: {code}")
