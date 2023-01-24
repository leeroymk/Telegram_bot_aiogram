from aiogram import Bot, Dispatcher, executor, types
import secret

API_TOKEN: str = secret.BOT_TOKEN
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# @dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


async def send_photo_echo(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)


async def send_sticker_echo(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)


async def send_audio_echo(message: types.Message):
    await message.answer_audio(message.audio.file_id)


async def process_sent_audio(message: types.Message):
    print(message)
    await message.answer(text='Вы прислали аудио!')


# async def process_any_updates(message: types.Message):
#     await message.answer(text='Вы что-то прислали')


async def send_echo(message: types.Message):
    await message.reply(message.text)


dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(send_photo_echo, content_types=['photo'])
dp.register_message_handler(send_sticker_echo, content_types=['sticker'])
dp.register_message_handler(send_audio_echo, content_types=['audio'])
# dp.register_message_handler(process_any_updates, content_types=['any'])
dp.register_message_handler(process_sent_audio, content_types=['audio'])
dp.register_message_handler(send_echo)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
