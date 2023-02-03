import telebot
import random
answer = '1'
rand = 1
rand2 = 1
bot = telebot.TeleBot("1910814053:AAHxMH_uGn07OvE0jPUzNcsbNakIq_xtsiY", parse_mode=None)
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