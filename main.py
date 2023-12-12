import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")




updater telegram.ext.Updater (TOKEN, use_context = True)
dispatch updater.dispatcher

updater.start_pooling()
updater.idle()
