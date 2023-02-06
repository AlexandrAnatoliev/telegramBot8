# telegramBot8
# работает на pytelegrambotapi (не telebot!)
# цикл уроков mastergroosha
# https://mastergroosha.github.io/telegram-tutorial/docs/pyTelegramBotAPI/lesson_00/
# простой echo-бот

from config import token
import telebot

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()  # бот будет стараться не прекращать работу при возникновении каких-либо ошибок


