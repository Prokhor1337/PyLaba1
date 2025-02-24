import requests

response = requests.get("https://zenquotes.io/api/random")

if response.status_code == 200:
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        quote = data[0]["q"]
        author = data[0]["a"]
        print(f'"{quote}" - {author}')

        with open("quote.txt", "w", encoding="utf-8") as file:
            file.write(f'"{quote}" - {author}')
    else:
        print("не вдалось отримати цитату")
else:
    print("помилка при запиті до API")
