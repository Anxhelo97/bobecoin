from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a start function to welcome users
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your Telegram bot. How can I assist you today?')

# Echo function to repeat whatever the user sends
def echo(update: Update, context: CallbackContext):
    user_message = update.message.text
    update.message.reply_text(f'You said: {user_message}')

# Function to handle errors
def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

def main():
    # Define the bot token
    bot_token = "7964270079:AAEY5L8RxIiKVnGYl9izJF4PLLG2Jg6BCAo"

    # Create the Updater and pass it your bot's token
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handlers
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
