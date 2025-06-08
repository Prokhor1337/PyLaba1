import aiohttp
from unidecode import unidecode

API_KEY = ""

async def get_weather(city, mode="full"):
    city_latin = unidecode(city)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_latin}&appid={API_KEY}&units=metric&lang=ua"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                if mode == "temp":
                    return f"🌡 Температура в {city}: {data['main']['temp']}°C"
                elif mode == "desc":
                    return f"📝 Погода в {city}: {data['weather'][0]['description']}"
                else:
                    return (
                        f"📍 {city.capitalize()}\n"
                        f"🌡 Температура: {data['main']['temp']}°C\n"
                        f"📝 Стан: {data['weather'][0]['description']}\n"
                        f"💨 Вітер: {data['wind']['speed']} м/с"
                    )
            else:
                return "❌ Місто не знайдено або помилка сервера."
