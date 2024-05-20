import spacy
from spacy import Language

from manager.manager import Manager
import settings
from nlp import lemmatize

BOT_TOKEN = '6171710263:AAG4FRtb60Da5kZ6Bwx4yhJNjLmzAYY8hxI'

import logging
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/address', '/phone', '/time', '/date'],
                  ['/site', '/work_time', '/help']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

status = dict()

N = 5

manager: Manager
nlp: Language


def main():
    global nlp
    nlp = spacy.load('ru_core_news_sm')
    global manager
    manager = Manager()

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("certificate", certificate))
    application.add_handler(CommandHandler("news", news))
    application.add_handler(CommandHandler("cost_of_education", cost_of_education))
    application.add_handler(CommandHandler("military_department", military_department))
    application.add_handler(CommandHandler("retakes", retakes))
    application.add_handler(CommandHandler("additional_education", additional_education))

    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.run_polling()
    application.start()


async def echo(update, context):
    user_id = update.effective_user.id
    message = update.message.text

    manager.user_manager.GetUser(user_id, update.effective_user.name)
    cur_state = manager.user_manager.GetStateId(user_id)
    where = manager.state_manager.WhereCanMove(cur_state, message)

    global nlp
    message = lemmatize(message, nlp)

    where = where.union(manager.state_manager.WhereCanMove(cur_state, message))
    next_state = 0
    if len(where) > 0:
        next_state = where.pop()
        if next_state > 100:
            manager.user_manager.Move(user_id, next_state, message)
    if next_state == 0:
        await update.message.reply_text("Извините, я Вас не понял, попробуйте задать свой вопрос еще раз")
    else:
        await update.message.reply_text(manager.state_manager.GetStateUrl(next_state))


async def start(update, context):
    await update.message.reply_text("Привет!")


async def news(update, context):
    await update.message.reply_text(settings.news_url)


async def certificate(update, context):
    await update.message.reply_text(settings.certificate_url)


async def cost_of_education(update, context):
    await update.message.reply_text(settings.cost_of_education_url)


async def military_department(update, context):
    await update.message.reply_text(settings.military_department_url)


async def selection_procedure_for_the_military_department_info(update, context):
    await update.message.reply_text(settings.selection_procedure_for_the_military_department_info_url)


async def retakes(update, context):
    await update.message.reply_text(settings.retakes_url)


async def additional_education(update, context):
    await update.message.reply_text(settings.additional_education_url)


async def cost_of_additional_education(update, context):
    await update.message.reply_text(settings.cost_of_additional_education_url)


async def schedule(update, context):
    await update.message.reply_text(settings.schedule_url)


async def educational_process_schedules(update, context):
    await update.message.reply_text(settings.educational_process_schedules_url)


async def dormitory(update, context):
    await update.message.reply_text(settings.dormitory_url)


if __name__ == '__main__':
    main()
