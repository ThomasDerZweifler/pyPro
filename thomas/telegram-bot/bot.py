# pip3 install python-telegram-bot

# https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/

# https://www.toptal.com/python/telegram-bot-tutorial-python

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests # http
import re #regular expressions

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    print(url)
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1382819143:AAH7OeZ7INgU5tPA0ns3pAAnKOIn8tFoNm0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()