from telegram.ext import (
    Updater,
    CommandHandler,
)

from .config import settings
from .handlers import commands


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", commands.start_command))

    updater.start_polling()
    updater.idle()
