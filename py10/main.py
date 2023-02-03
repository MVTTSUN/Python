import logging
from random import randint
import openai
from aiogram import Bot, Dispatcher, executor, types
from logger import logger

openai.api_key = "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"
API_TOKEN = '5952090498:AAElZWZ-h4I-RCuQfPmZU2JYnSZwt0y193c'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.username
  user_message = message.text
  logger(user_id, user_name, user_message)

  btn_help = types.KeyboardButton('/help')
  btn_fox = types.KeyboardButton('/fox')
  btn_duck = types.KeyboardButton('/duck')
  btns = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btns.add(btn_help, btn_fox, btn_duck)
  await bot.send_message(message.chat.id, 'Начало работы с ботом', reply_markup=btns)

@dp.message_handler(commands=['help'])
async def quit_handler(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.username
  user_message = message.text
  logger(user_id, user_name, user_message)

  await message.answer('/help - описание всех функций бота\n\n/fox - рандомная картинка лисы\n\n/duck - рандомная картинка утки\n\nПростой набор сообщения в чат - общение с нейронной сетью')

@dp.message_handler(commands=['fox'])
async def quit_handler(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.username
  user_message = message.text
  logger(user_id, user_name, user_message)

  url = f'https://randomfox.ca/images/{randint(1, 121)}.jpg'
  await bot.send_photo(message.chat.id, types.InputFile.from_url(url))

@dp.message_handler(commands=['duck'])
async def quit_handler(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.username
  user_message = message.text
  logger(user_id, user_name, user_message)

  url = f'https://random-d.uk/api/{randint(1, 121)}.jpg'
  await bot.send_photo(message.chat.id, types.InputFile.from_url(url))

@dp.message_handler(content_types="text")
async def quit_handler(message: types.Message):
  user_id = message.from_user.id
  user_name = message.from_user.username
  user_message = message.text
  logger(user_id, user_name, user_message)
  
  model_engine = "text-davinci-003"
  prompt = message.text
  max_tokens = 128
  completion = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      temperature=0.5,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )
  await message.answer(completion.choices[0].text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)