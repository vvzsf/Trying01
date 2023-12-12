import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello! Welcome to PanindiaFilmZ Main Bot.")

updater telegram.ext.Updater (TOKEN, use_context = True)
dispatch updater.dispatcher

updater.start_pooling()
updater.idle()
