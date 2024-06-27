"""
python 27-dars "Kirill-Lotin" telegram botini yaratish
Nasiba Abdulloyevna
27.06.2024
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN='7398985359:AAEYbZ0fm1arpII8aNQwxJMetNNsglWOric'
bot=telebot.TeleBot(TOKEN,parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
        answer="Assalomu aleykum. Xush kelibsiz!\nMatnni kiriting: "
        bot.reply_to(message,answer)

@bot.message_handler(func=lambda message:True)
def trans(message):
        msg = message.text
        answer = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
        bot.reply_to(message,answer)
bot.polling()






































