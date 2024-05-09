import json
import random

from manager.StateManager import StateManager
from manager.UserManager import UserManager
from manager.manager import Manager

BOT_TOKEN = '6171710263:AAG4FRtb60Da5kZ6Bwx4yhJNjLmzAYY8hxI'

import logging
import time
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/address', '/phone', '/time', '/date'],
                  ['/site', '/work_time', '/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

status = dict()

N = 5


def main():
    manager = Manager()
    # manager.Move(1, 1, 'новости')
    # manager.Move(1, 2, 'где корпус')


    # application = Application.builder().token(BOT_TOKEN).build()
    #
    # # 1         справка
    # application.add_handler(CommandHandler("справка", start))
    # # 1.1       что является студентом
    # # 1.2       справку в военкомат
    # # 1.3       справку - вызов
    #
    # # 2         оплата обучения
    # application.add_handler(CommandHandler("оплата", help_command))
    # # 2.1       до какого числа надо оплатить
    # # 2.2       сколько надо оплатить
    # # 2.3       реквизиты
    #
    # # 3         новости
    # application.add_handler(CommandHandler("новости", address))
    #
    # # 4         военная кафедра
    # application.add_handler(CommandHandler("военная кафедра", phone))
    #
    # # 5         пересдачи
    # application.add_handler(CommandHandler("пересдачи", phone))
    #
    # # 6         пересдачи
    # application.add_handler(CommandHandler("дополнительное образование", phone))
    #
    # # 7         расписание
    # application.add_handler(CommandHandler("дополнительное образование", phone))
    #
    # # 8         стипендии
    # application.add_handler(CommandHandler("дополнительное образование", phone))
    #
    # # 9         общежитие
    # application.add_handler(CommandHandler("дополнительное образование", phone))
    #
    # # 9         корпуса
    # application.add_handler(CommandHandler("дополнительное образование", phone))
    #
    #
    # text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    #
    # # Регистрируем обработчик в приложении.
    # application.add_handler(text_handler)
    #
    # # Запускаем приложение.
    # application.run_polling()
    # application.start()


async def echo(update, context):
    user_id = update.effective_user.id
    id = status[user_id]['status']

    if id == -1:
        return

    if status[user_id]['questions'][id]['q'] == update.message.text:
        status[user_id]['score'] += 1
    if id == N - 1:
        status[user_id]['status'] = -1
        await update.message.reply_text('Ваш результат: ' + str(status[user_id]['score']))
    else:
        status[user_id]['status'] += 1
        await update.message.reply_text(status[user_id]['questions'][status[user_id]['status']]['q'])


def jsonn(x):
    with open('json.json') as cat_file:
        data = json.load(cat_file)
    return random.sample(data['test'], x)


async def start(update, context):
    user_id = update.effective_user.id
    status[user_id] = dict([('status', 0), ('questions', jsonn(N)), ('score', 0)])
    await update.message.reply_text(status[user_id]['questions'][0]['q'])


if __name__ == '__main__':
    main()