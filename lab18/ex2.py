from aiogram import Router, types
from aiogram.filters import Command
from weather import get_weather

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🌦 Привіт! Я бот прогнозу погоди. Напиши /help щоб побачити команди.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "/weather [місто] — повна погода\n"
        "/temp [місто] — температура\n"
        "/desc [місто] — опис погоди\n"
        "/info — про бота\n"
        "/exit — завершити"
    )

@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer("Цей бот показує прогноз погоди для будь-якого міста 🌍")

@router.message(Command("exit"))
async def cmd_exit(message: types.Message):
    await message.answer("Бувай! ☁️")

@router.message(Command("weather"))
async def cmd_weather(message: types.Message):
    city = message.text[len("/weather "):].strip()
    if not city:
        await message.answer("Введи місто після /weather")
        return
    result = await get_weather(city)
    await message.answer(result)

@router.message(Command("temp"))
async def cmd_temp(message: types.Message):
    city = message.text[len("/temp "):].strip()
    if not city:
        await message.answer("Введи місто після /temp")
        return
    result = await get_weather(city, "temp")
    await message.answer(result)

@router.message(Command("desc"))
async def cmd_desc(message: types.Message):
    city = message.text[len("/desc "):].strip()
    if not city:
        await message.answer("Введи місто після /desc")
        return
    result = await get_weather(city, "desc")
    await message.answer(result)
