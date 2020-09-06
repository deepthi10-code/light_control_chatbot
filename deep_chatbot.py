pip install python-telegram-bot
pip install adafruit-io 

import os
YOUR_AIO_USERNAME = os.getenv('YOUR_AIO_USERNAME')  #ADAFRUIT_IO_USERNAME
YOUR_AIO_KEY = os.getenv('YOUR_AIO_KEY') #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(YOUR_AIO_USERNAME,YOUR_AIO_KEY)
  
#create feed
new= Feed(name='ledbot1') 
result= aio.create_feed(new)

from Adafruit_IO  import Data
from telegram.ext import Updater, CommandHandler
import requests  # Getting the data from the cloud

def start(bot,update):
    update.message.reply_text("Hi, I'M LED CONTROL CHATBOT")
    update.message.reply_text("type /led_on to turn on the bulb")
    update.message.reply_text("type /led_off to turn on the bulb")
    
def led_off(bot,update):
    value = Data(value=0) # Sending a value to a feed
    value_send = aio.create_data('ledbot1',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="light is turning off")
    bot.send_photo(chat_id,photo='https://toppng.com/uploads/preview/light-bulb-on-off-png-11553940208oq66nq8jew.png')
    bot.send_message(chat_id=chat_id, text="light turned off")


def led_on(bot,update):
    value = Data(value=1)
    value_send = aio.create_data('ledbot1',value)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="light is turning on")
    bot.send_photo(chat_id,photo='https://www.freeiconspng.com/thumbs/lightbulb-png/light-bulb-png-bulb-png1247-12.png')
    bot.send_message(chat_id=chat_id, text="light turned on")

BOT_TOKEN= os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN, use_context=True)
dp = u.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('led_off',led_off))
dp.add_handler(CommandHandler('led_on',led_on))
u.start_polling()
u.idle()

