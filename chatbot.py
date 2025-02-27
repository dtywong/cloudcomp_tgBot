## this file is based on version 13.7 of python telegram chatbot
## and version 1.26.18 of urllib3
## chatbot.oy
import telegram
from telegram.ext import Updater, MessageHandler, Filters
# The messageHandler is used for all ressage updates
import configparser
import logging

def main():
    # Load your token and create an Updater for your Bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=(config['TELEGRAM']['ACCESS_TOKEN']), use_context=True)
    dispatcher = updater.dispatcher
    # You car set this loggirg nocule,
    # so you will <row wher and why tnings da not work as expected
    logging. basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging. INFO)

    # register a dispatcher to handle message:
    # here we register an echo dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher. add_handler(echo_handler)

    # To start tne bot:
    updater .start_polling()
    updater. idle()

def echo(update, context):
    reply_message = update.message. text.upper()
    logging.info("“Update: " + str(update))
    logging.info("“context: " + str(context))
    context. bot.send_message(chat_id=update.effective_chat.id, text= reply_message)

if __name__ == '__main__':
    main()