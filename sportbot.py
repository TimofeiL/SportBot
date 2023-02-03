import telebot
import random
answer = '1'
rand = 1
rand2 = 1

Telegram_key = '' # Ключ от бота котрого вы создадите "https://t.me/BotFather"

bot = telebot.TeleBot(Telegram_key, parse_mode=None)
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    if message.text == 'Что мне сделать?':
        rand = random.randint(0, 5)
        if rand <= 4:
            rand2 = random.randint(10, 50)
        else:
            rand2 = random.randint(1, 15)
        if rand == 1:
            answer = 'Отжимания '
        elif rand == 2:
            answer = 'Скручивания '
        elif rand == 3:
            answer = 'Приседания '
        elif rand == 4:
            answer = 'Берпи '
        else:
            answer = 'Подтягивания '
        bot.send_message(message.chat.id, answer)
        bot.send_message(message.chat.id, str(rand2))
bot.polling(none_stop = True)
