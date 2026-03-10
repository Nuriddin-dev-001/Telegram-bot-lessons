from telegram.ext import Updater, CommandHandler


def start_func(update, context):
    update.message.reply_text(text="Salom men Nuriddin04_botman")
    print(update.message.text)
    print(context.bot)
    print(update.message.from_user)


updater = Updater(token="*********************************************")
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start_func))
updater.start_polling()
updater.idle()
