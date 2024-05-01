import asyncio
import os
import random
from tkinter import Image

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from os import getenv
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=getenv("TOKEN"))
dp = Dispatcher()


def get_random_photo():
    image_file = random.choice(os.listdir("images"))
    image_path = os.path.join("images", image_file)
    photo = types.FSInputFile(image_path)

    return photo


@dp.message(Command("start"))
async def start(message: types.Message):
    unique_users = set()
    unique_users.add(message.from_user.id)
    num_unique_users = len(unique_users)
    await message.answer(f"Привет, {message.from_user.first_name} наш бот обслуживает уже {num_unique_users} пользователя”.")


@dp.message(Command("random_pic"))
async def random_pic(message: types.Message):
    photo = get_random_photo()
    await message.answer_photo(
        photo=photo,
        caption="Пухлый кот"
    )

@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    photo = get_random_photo()
    await message.answer_photo(
        photo=photo,
        caption=f"Ваш айди: {message.from_user.id}\n Ваше имя: {message.from_user.first_name}\n Ваш никнейм: {message.from_user.username}")

async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
