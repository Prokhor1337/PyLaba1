import json
from datetime import datetime, timedelta
from collections import defaultdict

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.taken_times = 0
        self.total_read_days = 0
        self.returned_count = 0

    def __repr__(self):
        return f"{self.title} ({self.author.name})"

class User:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.history = []
        self.current_loans = {}

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]

    def search_books(self, query):
        return [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.name.lower()]

    def issue_book(self, title, user):
        for book in self.books:
            if book.title == title and title not in self.current_loans:
                self.current_loans[title] = {'user': user, 'issue_date': datetime.now()}
                book.taken_times += 1
                self.history.append({
                    'book': book,
                    'user': user,
                    'issue_date': datetime.now(),
                    'return_date': None
                })
                return f"Книга '{title}' видана користувачу {user.name}"
        return f"Книга '{title}' недоступна для видачі"

    def return_book(self, title):
        if title in self.current_loans:
            loan = self.current_loans.pop(title)
            return_date = datetime.now()
            delta = return_date - loan['issue_date']
            days = delta.days
            for entry in reversed(self.history):
                if entry['book'].title == title and entry['return_date'] is None:
                    entry['return_date'] = return_date
                    entry['book'].total_read_days += days
                    entry['book'].returned_count += 1
                    break
            if days <= 14:
                return "Книга повернута вчасно"
            else:
                return f"Книга повернута із простроченням: {days - 14} днів"
        return f"Книга '{title}' не була видана"

    def get_statistics(self):
        popularity = defaultdict(int)
        return_rate = {}
        avg_read_time = {}

        for book in self.books:
            popularity[book.title] = book.taken_times
            return_rate[book.title] = round(book.returned_count / book.taken_times * 100, 2) if book.taken_times else 0
            avg_read_time[book.title] = round(book.total_read_days / book.returned_count, 2) if book.returned_count else 0

        return {
            "Популярність книг": dict(popularity),
            "Відсоток повернення": return_rate,
            "Середній час читання (днів)": avg_read_time
        }

    def export_statistics_to_json(self, filename="library_statistics.json"):
        stats = self.get_statistics()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=4)

def main():
    library = Library()
    users = {}

    while True:
        print()
        print("Меню бібліотеки")
        print("1. Додати книгу")
        print("2. Пошук книг")
        print("3. Видати книгу")
        print("4. Повернути книгу")
        print("5. Показати статистику")
        print("6. Експортувати статистику")
        print("0. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            title = input("Назва книги: ")
            author_name = input("Ім’я автора: ")
            author = Author(author_name)
            library.add_book(Book(title, author))
            print("Книгу додано.")

        elif choice == "2":
            query = input("Пошук (назва або автор): ")
            results = library.search_books(query)
            if results:
                print("Результати пошуку:")
                for book in results:
                    print(book)
            else:
                print("Нічого не знайдено.")

        elif choice == "3":
            user_name = input("Ім’я користувача: ")
            title = input("Назва книги: ")
            user = users.setdefault(user_name, User(user_name))
            print(library.issue_book(title, user))

        elif choice == "4":
            title = input("Назва книги: ")
            print(library.return_book(title))

        elif choice == "5":
            stats = library.get_statistics()
            for category, data in stats.items():
                print(category + ":")
                for key, value in data.items():
                    print(f"{key}: {value}")

        elif choice == "6":
            library.export_statistics_to_json()
            print("Статистика збережена у файлі 'library_statistics.json'.")

        elif choice == "0":
            break

        else:
            print("Невірна опція. Повторіть.")

if __name__ == "__main__":
    main()
