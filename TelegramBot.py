
import telebot
from telebot import types
# импорт pyTelegramBotAPI
# импорт кнопкми

bot = telebot.TeleBot('')
#установка ip ключей

#переход на сайт
@bot.message_handlers(commands=['website'])
def website(message):
    markup = types.InLineKeyboardMarkup()
    markup.add(types.InLineKeyboardButton('Посетить сайт', utr='https://www.yandex.com'))
    bot.send_message(message.chat.id, 'Отличный выбор, нажмите на кнопку', parse_mode='html', reply_markup=markup)

#переход в инста
@bot.message_handlers(commands=['insta'])
def instagram(message):
    markup = types.InLineKeyboardMarkup()
    markup.add(types.InLineKeyboardButton('Посетить Инстаграмм', utr='https://www.instagram.com/'))
    bot.send_message(message.chat.id, 'Отличный выбор, нажмите на кнопку', parse_mode='html', reply_markup=markup)

#ПЕРЕХОД В ВК
#переход в инста
@bot.message_handlers(commands=['vk'])
def vk(message):
    markup = types.InLineKeyboardMarkup()
    markup.add(types.InLineKeyboardButton('Посетить Инстаграмм', utr='https://www.vk.com/'))
    bot.send_message(message.chat.id, 'Отличный выбор, нажмите на кнопку', parse_mode='html', reply_markup=markup)
@bot.message_handlers(commands=['start'])
def start(message):
    send_mess = f"<b>Привет {message.from_user.fist_name}{message.from_user.last_name}</b>!\n Какое направление тебя интересует"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')

bot.polling(none_stop=True)
# запуск проекта на постоянную работу
