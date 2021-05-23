import telebot
import time

TOKEN = "1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])

def start(message):
      bot.send_message(message.chat.id, "Xoşgəldin :)")


@bot.message_handler(commands=["hello", "hi"])

def hello(message):
    bot.send_message(message.chat.id, "Hi dude!")


@bot.message_handler(content_types=['text'])    
def send_text(message):
 if message.text.lower() == 'salam':
  bot.send_message(message.chat.id, 'Aleykum Salam ay ' + message.chat.first_name + '!') 
 elif message.text.lower() == 'slm':
  bot.send_message(message.chat.id, 'Aleykum Salam ay  ' + message.chat.first_name + '!')
 elif message.text.lower() == 'sağol':
  bot.send_message(message.chat.id, 'Öpürəm ay ' + message.chat.first_name + '!')
 elif message.text.lower() == 'necəsən':
  bot.send_message(message.chat.id, 'Təki sən yaxşı ol canım ay ' + message.chat.first_name + '!')
 elif message.text.lower() == 'necəsən?':
  bot.send_message(message.chat.id, 'Təki sən yaxşı ol canım ay ' + message.chat.first_name + '!')


while True:
    try:
        bot.polling()
    except:
        time.sleep(5)
