def sum_list_recursive(lst):
    if not isinstance(lst, list):
        return "Помилка: аргумент має бути списком"
    if not lst:
        return 0
    if not isinstance(lst[0], (int, float)):
        return "Помилка: всі елементи мають бути числами"
    return lst[0] + sum_list_recursive(lst[1:])

lst = list(map(float, input("Введіть числа через пробіл: ").split()))
print("Сума:", sum_list_recursive(lst))
