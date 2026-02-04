from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton


def start_command(update, context):
    print(update.message.from_user.id)
    update.message.reply_text(text="Salom men Nuriddin04_botman!")


def show_menu(update, context):
    buttons = [
        [KeyboardButton(text="Send Contact", request_contact=True),
         KeyboardButton(text="Send Location", request_location=True)],
        [KeyboardButton(text="Menu 3"), KeyboardButton(text="Menu 4")],
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
    )


def message_handler(update, context):
    message = update.message.text
    if message == 'salom':
        update.message.reply_text(text=f"Salom do'stim men Nuriddin_Botman\n Nimaga qiziqasiz Sport, Kitoblar?")
    if message == 'kitob':
            update.message.reply_text(text=f"Sizga qaysi janrdagi kitoblar yoqadi?")
    elif message == 'diniy':
            update.message.reply_text(text=f"Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
    elif message == 'detektiv':
            update.message.reply_text(text=f"Sizga 'Shaytanat' kitobini sovg'a qilamiz!")
    else:
            update.message.reply_text(text=f"Sizga qiziq bo'lishi mumkin bo'lgan turli kitoblarimiz bor!")

def contact_handler(update, context):
    phone_number = update.message.contact.phone_number
    # update.message.reply_text(text=f"Sizning nomeringiz '{phone_number}'")
    context.bot.send_message(chat_id=*******, text=f"yangi foydalanuvchi raqami: {phone_number}")


def location_handler(update, context):
    location = update.message.location
    # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
    context.bot.send_location(chat_id=7192734058, latitude=location.latitude, longitude=location.longitude)
    update.message.reply_text(f"latitude={location.latitude},longitude={location.longitude}")

def main():
    updater = Updater(token="*****************************************")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(MessageHandler(Filters.location, location_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


