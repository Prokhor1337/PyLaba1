def fibonacci_recursive(n):
    if not isinstance(n, int) or n < 0:
        return "Помилка: введіть невід’ємне ціле число"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Введіть номер числа Фібоначчі: "))
print("Результат:", fibonacci_recursive(n))
