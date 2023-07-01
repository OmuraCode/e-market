from django.http import HttpResponse
from telegram_bot import bot_handler


def telegram_webhook(request):
    bot_handler.run_bot()

    return HttpResponse("Bot is running.")
