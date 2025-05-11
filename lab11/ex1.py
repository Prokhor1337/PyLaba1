phonebook = [
    {"ім'я": "Іван", "прізвище": "Петренко", "телефон": "123456789", "місто": "Київ"},
    {"ім'я": "Олена", "прізвище": "Іваненко", "телефон": "987654321", "місто": "Львів"},
    {"ім'я": "Сергій", "прізвище": "Коваль", "телефон": "456789123", "місто": "Одеса"},
    {"ім'я": "Марія", "прізвище": "Шевченко", "телефон": "321654987", "місто": "Київ"},
    {"ім'я": "Андрій", "прізвище": "Бондар", "телефон": "741852963", "місто": "Харків"},
]

def printphonebook(book):
    print(f"{'Ім\'я':<10}{'Прізвище':<15}{'Телефон':<15}{'Місто':<10}")
    for contact in book:
        print(f"{contact['ім\'я']:<10}{contact['прізвище']:<15}{contact['телефон']:<15}{contact['місто']:<10}")

def searchcontacts(book):
    field = input("Пошук за (ім'я / прізвище / місто): ").strip().lower()
    if field not in ["ім'я", "прізвище", "місто"]:
        print("Неправильне поле для пошуку")
        return
    value = input(f"Введіть значення для пошуку за '{field}': ").strip()
    if not value:
        print("Порожній запит")
        return
    results = [contact for contact in book if contact[field].lower() == value.lower()]
    if results:
        printphonebook(results)
    else:
        print("Контакти не знайдено")

def updatecontact(book):
    phone = input("Введіть номер телефону контакту для оновлення: ").strip()
    for contact in book:
        if contact["телефон"] == phone:
            print("Знайдено контакт:")
            print(contact)
            confirm = input("Підтвердити оновлення? (так/ні): ").strip().lower()
            if confirm == "так":
                contact["ім'я"] = input("Нове ім'я: ").strip()
                contact["прізвище"] = input("Нове прізвище: ").strip()
                contact["місто"] = input("Нове місто: ").strip()
                print("Контакт оновлено")
            return
    print("Контакт не знайдено")

def deletecontact(book):
    phone = input("Введіть номер телефону контакту для видалення: ").strip()
    for i, contact in enumerate(book):
        if contact["телефон"] == phone:
            print("Знайдено контакт:")
            print(contact)
            confirm = input("Підтвердити видалення? (так/ні): ").strip().lower()
            if confirm == "так":
                del book[i]
                print("Контакт видалено")
            return
    print("Контакт не знайдено")

def analytics(book):
    cities = set(contact["місто"] for contact in book)
    print(f"Унікальні міста: {cities}")
    citycounts = {}
    for contact in book:
        city = contact["місто"]
        citycounts[city] = citycounts.get(city, 0) + 1
    print("Кількість контактів по містах:")
    for city, count in citycounts.items():
        print(f"{city}: {count}")
    maxcity = max(citycounts, key=citycounts.get)
    print(f"Місто з найбільшою кількістю контактів: {maxcity}")

def menu():
    while True:
        print("\nТелефонна книга")
        print("1. Показати всі контакти")
        print("2. Пошук")
        print("3. Оновити контакт")
        print("4. Видалити контакт")
        print("5. Аналітика")
        print("6. Вийти")
        try:
            choice = int(input("Виберіть опцію: "))
        except ValueError:
            print("Введіть число від 1 до 6")
            continue
        if choice == 1:
            printphonebook(phonebook)
        elif choice == 2:
            searchcontacts(phonebook)
        elif choice == 3:
            updatecontact(phonebook)
        elif choice == 4:
            deletecontact(phonebook)
        elif choice == 5:
            analytics(phonebook)
        elif choice == 6:
            break
        else:
            print("Невірний вибір")

if __name__ == "__main__":
    menu()
