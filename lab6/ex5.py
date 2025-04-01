import random

try:
    wood = int(input("Скільки деревини ви зібрали для плоту? (1-10): "))
    if wood < 3:
        print("Деревини занадто мало, пліт затонув! Гру завершено.")
        exit()
except ValueError:
    print("Це не число! Гру завершено.")
    exit()

choice = input('Як ви хочете врятуватися? ("бігти", "сховатися", "битися"): ').lower()
if choice not in ["бігти", "сховатися", "битися"]:
    print("Такого варіанту немає, пірати вас спіймали! Гру завершено.")
    exit()

secret_code = random.randint(10, 99)
try:
    user_code = int(input("Введіть код скрині (двозначне число): "))
    if user_code != secret_code:
        print("Неправильний код, скриня вибухнула! Гру завершено.")
    else:
        print("Скарб ваш, ви врятовані!")
except ValueError:
    print("Це не число! Гру завершено.")

finally:
    print("Гра завершена. Дякуємо за участь у пригоді!")
