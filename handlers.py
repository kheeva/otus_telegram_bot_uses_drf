import logging

from parser_helpers import (
    fetch_otus_json_data,
    calc_avg_price,
    get_first_image_url_from_results,
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def price_handler(bot, update):
    query = ' '.join(update.message.text.split(' ')[1:])

    otus_json_data = fetch_otus_json_data(query)
    avg_price = otus_json_data and calc_avg_price(otus_json_data) or None

    if not avg_price:
        update.message.reply_text('Нет цен на курс по %s' % query)
    else:
        update.message.reply_text('Средняя цена: %s рублей.' % avg_price)

        image_url_to_show = get_first_image_url_from_results(otus_json_data)
        bot.send_photo(
            chat_id=update.message.chat_id,
            photo=image_url_to_show,
        )


def error(bot, update, _error):
    logger.warning('Update "%s" caused error "%s"', update, _error)
