import kompvision
import парспергугл
import random
import telebot
import uuid
from config import telegram_token

token = telegram_token
bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=['photo'])
def photo(message):
    # скачивание файла
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)

    extn = '.' + str(path.file_path).split('.')[-1]
    name = 'images/' + str(uuid.uuid4()) + extn

    # создаем файл и записываем туда данные
    with open(name, 'wb') as new_file:
        new_file.write(downloaded_file)

    pic = kompvision.vision(name)
    pic = парспергугл.getpics(pic)
    user = message.chat.id
    if pic:
        bot.send_photo(user, pic)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Отправь фотку')

bot.polling(none_stop=True)
