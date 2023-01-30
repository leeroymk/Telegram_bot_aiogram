from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
from aiogram.types.web_app_info import WebAppInfo

import secret

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
API_TOKEN: str = secret.BOT_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard.row('1', '2', '3').row('4', '5', '6').insert('7')

# Добавляем кнопки в клавиатуру
# keyboard.add(KeyboardButton(text='Start Web App', web_app=WebAppInfo(url="https://stepik.org/")))
# keyboard.add(KeyboardButton(text='Отправить телефон', request_contact=True))
# keyboard.add(KeyboardButton(text='Отправить геолокацию', request_location=True))
# keyboard.add(KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType(type=types.PollType.REGULAR)))
# keyboard.add(KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType(type=types.PollType.QUIZ)))
# keyboard.add('Button 1', '2')

# # Создаем объекты кнопок
# button_1: KeyboardButton = KeyboardButton('Собак 🦮')
# button_2: KeyboardButton = KeyboardButton('Огурцов 🥒')

# Этот хэндлер будет срабатывать на команду "/start" и отправлять в чат клавиатуру
async def process_start_command(message: types.Message):
    await message.answer('Экспериментируем со специальными кнопками', reply_markup=keyboard)


# Этот хэндлер будет срабатывать на ответ "Собак 🦮" и удалять клавиатуру
async def process_dog_answer(message: types.Message):
    await message.answer('Да, несомненно, кошки боятся собак. Но вы видели как они боятся огурцов?')


# Этот хэндлер будет срабатывать на ответ "Огурцов 🥒" и удалять клавиатуру
async def process_cucumber_answer(message: types.Message):
    await message.answer('Да, иногда кажется, что огурцов кошки боятся больше')


# Регистрируем хэндлеры
dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_dog_answer, text='Собак 🦮')
dp.register_message_handler(process_cucumber_answer, text='Огурцов 🥒')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
