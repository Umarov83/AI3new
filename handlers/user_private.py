from aiogram import types, Router
from aiogram.filters import CommandStart, Command


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Бот запущен')


# @user_private_router.message(Command('Video'))
# async def menu_cmd(message: types.Message):
#     await message.answer(link)