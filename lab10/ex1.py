def factorial_recursive(n):
    try:
        n = int(n)
        if n < 0:
            return "Помилка: введіть невід’ємне ціле число"
    except ValueError:
        return "Помилка: введіть саме ціле число"

    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

user_input = input("Введіть число для обчислення факторіалу: ")
print("Результат:", factorial_recursive(user_input))
