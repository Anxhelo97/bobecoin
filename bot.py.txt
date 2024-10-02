from telegram import Bot, Update, Game
from telegram.ext import CommandHandler, Updater

# Telegram bot token from BotFather
TOKEN = "7964270079:AAEY5L8RxIiKVnGYl9izJF4PLLG2Jg6BCAo"

def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_game(chat_id=chat_id, game_short_name="BOBE_Coin")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
