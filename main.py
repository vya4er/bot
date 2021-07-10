from telegram.ext import Updater,CommandHandler, MessageHandler, Filters
from const import TOKEN
from func import *
u = Updater(token=TOKEN, workers=4)
d = u.dispatcher
d.add_handler(CommandHandler('start',callback=start, run_async=True))
d.add_handler(MessageHandler(Filters.text, callback=text_answer))
u.start_polling(drop_pending_updates=True)