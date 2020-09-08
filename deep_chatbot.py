import logging
import os 

from Adafruit_IO  import Data
YOUR_AIO_USERNAME = os.getenv('YOUR_AIO_USERNAME')  #ADAFRUIT_IO_USERNAME
YOUR_AIO_KEY = os.getenv('YOUR_AIO_KEY') #ADAFRUIT_IO_KEY
from Adafruit_IO import Client, Feed
aio = Client(YOUR_AIO_USERNAME,YOUR_AIO_KEY) 
  
#create feed
new= Feed(name='ledbot') 
result= aio.create_feed(new) 

#logging exception handler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

from telegram.ext import Updater, CommandHandler,MessageHandler, Filters 
import requests #Getting the data from the cloud

def start(bot,update):
    bot.message.reply_text('HI, IM LIGHT CONTROL CHATBOT')
    bot.message.reply_text('type /led_on to turn on the bulb')
    bot.message.reply_text('type /led_off to turn off the bulb')
    
def led_off(bot,update):
    value = Data(value=0) #Sending a value to a feed
    value_send = aio.create_data('ledbot',value)
    chat_id = bot.message.chat_id
    bot.message.reply_text('Light is turning off... wait for a moment')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://toppng.com/uploads/preview/light-bulb-on-off-png-11553940208oq66nq8jew.png", caption="Light turned off!")
    
def led_on(bot,update):
    value = Data(value=1)
    value_send = aio.create_data('ledbot',value)
    chat_id = bot.message.chat_id
    bot.message.reply_text('Light is turning on... wait for a moment')
    update.bot.sendPhoto(chat_id=chat_id, photo="https://toppng.com/uploads/preview/light-bulb-on-off-png-11553940194wdc9uy3j5o.png", caption="Light turned on!")
    
def echo(bot, update):
    #Echo the user message
    bot.message.reply_text(bot.message.text)

def main():
  BOT_TOKEN= os.getenv("BOT_TOKEN")
  u = Updater(BOT_TOKEN, use_context=True)
  dp = u.dispatcher
  dp.add_handler(CommandHandler("start",start))
  dp.add_handler(CommandHandler("led_off",led_off))
  dp.add_handler(CommandHandler("led_on",led_on))
  dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
  u.start_polling()
  u.idle()
  
if __name__ == '__main__':
    main()
