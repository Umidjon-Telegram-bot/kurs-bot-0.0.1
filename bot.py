import requests

import logging


API_KEY = 'd8472cdf8fdb28c91e66aea8'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5739371292:AAEdsyWIO5hFYp6VjNbRCH_yvlKNPVdS2LY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Assalomu alaykum {message.chat.full_name} Valyuta kurs botimizga xush kelibsiz!")
    await message.answer("Dollarni kiriting men sizga so'mga o'girib beraman!")

@dp.message_handler()
async def send_Uzs(message: types.Message):
    if message.text.isnumeric():
        r = requests.get(url)
        res = r.json()
        usd = int(message.text)
        usd_1 = res['conversion_rate']
        uzs = int(usd_1 * usd)
        await message.answer(f"{usd}(usd) - {uzs} so'm")
    else:
        await message.reply("Iltimos son kiriting!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
