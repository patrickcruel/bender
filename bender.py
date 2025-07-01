import telebot
import random
from openai import OpenAI
import logging
from dotenv import load_dotenv
import os

# === CONFIG ===
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_KEY"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# === LOGGING ===
logging.basicConfig(level=logging.INFO)


# === HANDLER ===
@bot.message_handler(func=lambda message: 'bender' in message.text.lower())

def handle_message(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":message.text}]
	)
    reply = response.choices[0].message.content
    bot.reply_to(message, reply)
    


	#@bot.message_handler(func=lambda message: True)
	#def echo_all(message):
	#	bot.reply_to(message, message.text)



	#@bot.message_handler(commands=['clear'])
	#def clear_channel_history(message):
		#bot.channels.


bot.infinity_polling()