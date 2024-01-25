import asyncio
import os

import requests
from bs4 import BeautifulSoup

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


url = 'https://yandex.ru/video/search?text=porno-hub'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

link_all = []

for video_soup in soup.find_all('div', class_='VideoSnippet2-Content'):
    link = video_soup.div.a['href']
    link_all = link


@user_private_router.message(Command('Video'))
async def menu_cmd(message: types.Message):
    await message.answer(link_all)


asyncio.run(main())
