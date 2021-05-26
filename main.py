#daxil elədik

import telebot
import time
from googletrans import Translator 

#tokeni falan gösdərdiy

TOKEN = "1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI"
bot = telebot.TeleBot(TOKEN)
translator = Translator()

#bu nədi bilmirəm aq

class Bthelper:
    def __init__(self):
        self.dest = 'en'
        self.src = 'az'

    def set_handler(self,dest,src):
        self.dest = dest
        self.src = src

    def get_handler(self):
        return self.dest, self.src
bt_help = Bthelper()

#start basanda bunu deyəcəy

@bot.message_handler(commands=["start"])

def start(message):
      bot.send_message(message.chat.id, "Salam👋 Xoşgəldiniz :) \n Botdan istifadə etmək üçün '/' işarəsinə klikləyə bilərsiz. \n Azərbaycan dilindən İngilis dilinə tərcümə etmək istıyirsizsə '/en' seçiminə, \n İstənilən dildən Azərbaycan dilinə tərcümə etmək istəsəz isə '/tercume' seçiminə tıklayın.")


#burda gic-gic sözlərə cavab verir sj

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

#bu da nədi bilmirəm aq

while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(5)
