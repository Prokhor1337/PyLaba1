import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from assistant import Assistant

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()
assistant = Assistant()
user_states = {}

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Вітаю! Я Telegram-асистент.\nДоступні команди: /add, /list, /search")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Команди:\n/add — додати нотатку\n/list — список\n/search — пошук")

@dp.message(Command("add"))
async def cmd_add(message: Message):
    user_states[message.chat.id] = "adding"
    await message.answer("Введіть текст нотатки:")

@dp.message(Command("list"))
async def cmd_list(message: Message):
    notes = assistant.list_notes()
    if notes:
        await message.answer("\n".join(f"- {n}" for n in notes))
    else:
        await message.answer("Немає нотаток.")

@dp.message(Command("search"))
async def cmd_search(message: Message):
    user_states[message.chat.id] = "searching"
    await message.answer("Введіть ключове слово:")

@dp.message()
async def handle_message(message: Message):
    state = user_states.get(message.chat.id)
    if state == "adding":
        assistant.add_note(message.text)
        await message.answer("Нотатку додано.")
        user_states[message.chat.id] = None
    elif state == "searching":
        results = assistant.search_notes(message.text)
        if results:
            await message.answer("\n".join(f"- {n}" for n in results))
        else:
            await message.answer("Нічого не знайдено.")
        user_states[message.chat.id] = None
    else:
        await message.answer("Невідома команда. Використовуйте /help.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
