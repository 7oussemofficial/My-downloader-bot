import os
import telebot
from flask import Flask
from threading import Thread

# إنشاء سيرفر ويب وهمي لتخطي القيود المجانية على ريندر
app = Flask('')

@app.route('/')
def home():
    return "Bot is Alive and Running!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# التوكن الخاص بك (يمكنك تركه هكذا وتعديله لاحقاً بالتوكن الحقيقي)
BOT_TOKEN = "123456789:ABCdefGh..." 
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! البوت الخاص بك يعمل الآن بنجاح على السيرفر المستقل والمجاني 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلتني رسالتك: {message.text}")

if __name__ == "__main__":
    keep_alive() # تشغيل سيرفر الويب في الخلفية
    bot.infinity_polling()

  
