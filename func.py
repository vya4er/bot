# from time import sleep
from random import randint
from const import *


def start(update, context):
    user_id = update.message.chat_id
    name = update.message.from_user.first_name
    context.bot.send_message(chat_id=user_id, text='Привет {}'.format(name))


def text_answer(update, context):
    user_id = update.message.chat_id
    text = update.message.text
    text = text.lower()
    if text in DCT.keys():
        context.bot.send_message(chat_id=user_id, text=(DCT.get(text)[randint(0, 2)]))
