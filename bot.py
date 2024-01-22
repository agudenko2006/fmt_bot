import asyncio
import logging
import sys
from os import getenv
import re
from typing import Any

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import BufferedInputFile, Message, message
from aiogram.filters import Command, CommandObject
import scraper

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

@dp.message(Command("generate"))
async def generate(message: Message, command: CommandObject) -> Any:
    url = message.text.split()[-1]
    text = scraper.create_template(scraper.scrape(url))
    file = BufferedInputFile(str.encode(text), filename="infourok.html")
    await message.answer_document(file)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
