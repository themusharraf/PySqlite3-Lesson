import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from root import TOKEN
from db import Database

db = Database("preson.db")
dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(5611541842, "Bot ishga tushdi! ✅")


async def shutdown__answer(bot: Bot):
    await bot.send_message(5611541842, "Bot ishga to'xtadi!❗️")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}", parse_mode=ParseMode.HTML)
    db.add_user(message.from_user.id, message.from_user.full_name)
    db.get_all_users()

async def main():
    dp.startup.register(startup_answer)
    dp.message.register(cmd_start)
    dp.shutdown.register(shutdown__answer)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
