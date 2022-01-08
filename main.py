#Deməli belə 1.Dil fayllarını daxil elə. 2.Buton qoy

#daxil elədik

import telebot
import time
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from googletrans import Translator 
translator = Translator()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def to_az(bot, update):
    content = update.message.text[3:] # `/az `
    translate = translator.translate(content, dest='az') 
    bot.send_message(chat_id=update.message.chat_id, text=f'{content} = {translate.text}')

def to_eng(bot, update):
    content = update.message.text[3:] # `/eng `
    translate = translator.translate(content, dest='en')
    bot.send_message(chat_id=update.message.chat_id, text=f'{content} = {translate.text}')    
    
def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', bot, update.error)
    

def main():
    updater = Updater("1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("az", to_az))
    dp.add_handler(CommandHandler("en", to_eng))
    

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()    
    

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
