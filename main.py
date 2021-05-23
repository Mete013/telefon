import telebot
import time

TOKEN = "1803905332:AAGxCo_YavzdhsvFXliBxii5xMdjQ5ttkEQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])

def start(message):
      bot.send_message(message.chat.id, "Xoşgəldin :)")


@bot.message_handler(commands=["hello", "hi"])

def hello(message):
    bot.send_message(message.chat.id, "Aleykum")


@bot.message_handler(content_types=['text'])    
def send_text(message):
 if message.text.lower() == 'salam':
  bot.send_message(message.chat.id, 'Aleykum Salam ay ' + message.chat.first_name + '!') 
 elif message.text.lower() == 'slm':
  bot.send_message(message.chat.id, 'Aleykum Salam ay  ' + message.chat.first_name + '!')



while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
