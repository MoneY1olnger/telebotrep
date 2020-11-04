import telebot
import nn
import os

TOKEN = '1399932538:AAG-Qhao9olzrWkSyelQvcjtimaLaOZoweU'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help_handler(message):
    bot.send_message(message.from_user.id,  "Привет, отправь сюда картинку, а я тебе отвечу, кошка или собака на ней")


@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    """Функция обрабатывает сообщение с картинкой"""
    label1 = 'собака'
    label2 = 'кошка'
    directory = '/Users/Matvey/Desktop/images'
    photo = message.photo[-1]
    file_id = photo.file_id
    file_path = bot.get_file(file_id).file_path
    downloaded_file = bot.download_file(file_path)
    name = file_id + ".jpg"
    new_file = open(directory+f'/{name}' , mode = 'wb' )
    new_file.write(downloaded_file)
    new_file.close()
    res = nn.predict_img_from_dir(directory, name)
    sureness1 = res[label1]
    sureness2 = res[label2]
    reply = 'На картинке изображена {}'
    if sureness1 >= sureness2:
         bot.reply_to(message, reply.format(label1))
    # Отправим пользователю сообщение с результатом
    else:
        bot.reply_to(message, reply.format(label2))


@bot.message_handler(func=lambda m: True)
def all_handler(message):
    """Все остальные сообщения будут попадать в эту функцию"""
    bot.send_message(message.from_user.id, "Пожалуйста, отправьте картинку")


# Запустим нашего бота
bot.polling()
