inventory = [
    {"назва": "Ноутбук", "кількість": 10, "ціна": 15000.0, "категорія": "електроніка"},
    {"назва": "Смартфон", "кількість": 25, "ціна": 8000.0, "категорія": "електроніка"},
    {"назва": "Футболка", "кількість": 50, "ціна": 400.0, "категорія": "одяг"},
    {"назва": "Джинси", "кількість": 30, "ціна": 1200.0, "категорія": "одяг"},
    {"назва": "Молоко", "кількість": 100, "ціна": 30.0, "категорія": "продукти"},
    {"назва": "Хліб", "кількість": 80, "ціна": 20.0, "категорія": "продукти"},
    {"назва": "Мишка", "кількість": 15, "ціна": 500.0, "категорія": "електроніка"},
]

def print_table(items):
    print(f"{'Назва':<15}{'Кількість':<10}{'Ціна':<10}{'Категорія':<15}")
    for item in items:
        print(f"{item['назва']:<15}{item['кількість']:<10}{item['ціна']:<10.2f}{item['категорія']:<15}")

def search_by_name(name):
    return [item for item in inventory if item["назва"].lower() == name.lower()]

def search_by_category(category):
    return [item for item in inventory if item["категорія"].lower() == category.lower()]

def update_item(item):
    try:
        new_quantity = int(input("Нова кількість: "))
        new_price = float(input("Нова ціна: "))
        item["кількість"] = new_quantity
        item["ціна"] = new_price
        print("Товар оновлено успішно.")
    except ValueError:
        print("Помилка: Некоректне значення!")

def edit_item():
    search_type = input("Шукати за (назва/категорія): ").strip().lower()
    if search_type == "назва":
        name = input("Введіть назву товару: ")
        result = search_by_name(name)
    elif search_type == "категорія":
        category = input("Введіть категорію: ")
        result = search_by_category(category)
    else:
        print("Невірний тип пошуку.")
        return

    if result:
        for i, item in enumerate(result, 1):
            print(f"{i}. {item}")
        choice = int(input("Оберіть номер товару для редагування: ")) - 1
        if 0 <= choice < len(result):
            update_item(result[choice])
        else:
            print("Невірний номер.")
    else:
        print("Товар не знайдено.")

def analyze_inventory(items):
    category_totals = {}
    low_stock = []

    for item in items:
        total_value = item["кількість"] * item["ціна"]
        category = item["категорія"]
        category_totals[category] = category_totals.get(category, 0) + total_value

        if item["кількість"] < 5:
            low_stock.append(item)

    print("\nЗагальна вартість по категоріях:")
    for category, total in category_totals.items():
        print(f"{category:<15} — {total:.2f} грн")

    max_category = max(category_totals, key=category_totals.get)
    print(f"\nКатегорія з найбільшою вартістю товарів: {max_category}")

    print("\nТовари з кількістю нижче 5:")
    for item in low_stock:
        print(f"{item['назва']} — {item['кількість']} шт.")

while True:
    print("\n1. Переглянути таблицю\n2. Редагувати товар\n3. Аналітика\n4. Вийти")
    choice = input("Оберіть опцію: ")
    if choice == '1':
        print_table(inventory)
    elif choice == '2':
        edit_item()
    elif choice == '3':
        analyze_inventory(inventory)
    elif choice == '4':
        break
    else:
        print("Невірний вибір.")
