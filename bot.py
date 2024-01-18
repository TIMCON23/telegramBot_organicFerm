import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('new client')
    update.message.reply_text('Дякую, що завітали до нас! Чекаємо запитань!')
    
def talk_to_me(update, context):
    text = update.message.text 
    print(text)
    update.message.reply_text(text)
    
def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('бот на старті')
    mybot.start_polling()#достукування до платформи
    mybot.idle()
if __name__ == '_main_':    
    main()#визиваємо функцію
    