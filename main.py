import telegram.ext
from dotenv import load_dotenv
import os
import urllib3  # Make sure to import urllib3 if needed

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Welcome to PanindiaFilmZ Main Bot.")

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(telegram.ext.CommandHandler("start", start))

updater.start_polling()
updater.idle()
