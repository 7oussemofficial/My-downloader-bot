import os
import telebot

bot = telebot.TeleBot("123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أنا بوت التحميل الخاص بك. أرسل لي رابطاً لتجربتي (قيد التطوير حالياً).")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"لقد استلمت رسالتك: {message.text}\nجاري العمل على إضافة ميزة التحميل المباشر.")

if __name__ == "__main__":
    bot.infinity_polling()
  
