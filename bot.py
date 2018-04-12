import os
import sys
from threading import Thread

from telegram.ext import Updater, CommandHandler, Filters

from handlers import start, error, price_handler

from dotenv import load_dotenv


def get_configured_updater():
    load_dotenv()
    updater = Updater(os.getenv('BOT_TOKEN'))

    def stop_and_restart():
        updater.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def restart(bot, update):
        update.message.reply_text('Bot is restarting...')
        Thread(target=stop_and_restart).start()

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("price", price_handler))
    dp.add_handler(CommandHandler(
        'r',
        restart,
        filters=Filters.user(username='@kheeva'))
    )
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    get_configured_updater()
