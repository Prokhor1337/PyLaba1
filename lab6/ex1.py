try:
    coins = int(input("Скільки золотих монет знайдено? (1-1000): "))
    people = int(input("Скільки людей у команді?: "))

    result = coins // people
    remainder = coins % people
    print(f"Кожен отримав по {result} монет. Залишок: {remainder} монет.")
except ValueError:
    print("Помилка! Введіть ціле число.")
except ZeroDivisionError:
    print("Помилка! Ділити на нуль не можна.")
finally:
    print("Пригоди тривають!")
