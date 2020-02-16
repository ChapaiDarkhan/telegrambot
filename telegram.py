import telebot
bot = telebot.TeleBot('1042017850:AAHwrmjUPZNidl4npFOz6PHJ8a77wSoAir8')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello, Telegram chatbot")


bot.polling()
