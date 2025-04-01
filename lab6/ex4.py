try:
    points = int(input("Введіть кількість очок (0-100): "))

    if points < 0 or points > 100:
        raise ValueError("Некоректне введення!")

    multiplier, rating = (1, "Початківець") if points < 50 else \
                         (1.5, "Срібний гравець") if points < 70 else \
                         (2, "Золотий гравець") if points < 90 else \
                         (3, "Платиновий гравець")

    final_points = int(points * multiplier)
    print(f"Ваш рейтинг: {rating}! Ви отримали {final_points} балів (множник ×{multiplier})!")

except ValueError:
    print("Некоректне введення! Кількість очок повинна бути в межах від 0 до 100.")
