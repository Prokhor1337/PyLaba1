from assistant import Assistant

def main():
    assistant = Assistant()

    print("Консольний асистент. Доступні команди: /add, /list, /search, /exit")

    while True:
        cmd = input(">>> ").strip()

        if cmd == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)
            print("Нотатку додано.")
        elif cmd == "/list":
            notes = assistant.list_notes()
            if notes:
                print("\n".join(f"- {n}" for n in notes))
            else:
                print("Немає нотаток.")
        elif cmd == "/search":
            keyword = input("Введіть ключове слово: ")
            results = assistant.search_notes(keyword)
            print("\n".join(f"- {n}" for n in results) if results else "Збігів не знайдено.")
        elif cmd == "/exit":
            print("До побачення!")
            break
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()
