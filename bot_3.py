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
    context.bot.send_message(chat_id=7192734058, text=f"yangi foydalanuvchi raqami: {phone_number}")


def location_handler(update, context):
    location = update.message.location
    # update.message.reply_location(latitude=location.latitude, longitude=location.longitude)
    context.bot.send_location(chat_id=7192734058, latitude=location.latitude, longitude=location.longitude)
    update.message.reply_text(f"latitude={location.latitude},longitude={location.longitude}")

def main():
    updater = Updater(token="7926665974:AAGFadnhmF4QLRG2Y7xR85J07JLXYzdkIWw")
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


# qiziqish = input("Nimaga qiziqasiz: ").lower()
# if "kitob" in qiziqish:
#     janr = input("Sizga qaysi janrdagi kitoblar yoqadi? ").lower()
#     if "diniy" in janr:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     elif "detektiv" in janr:
#         print("Sizga 'Shaytanat' kitobini sovg'a qilamiz!")
#     else:
#         print("Sizga qiziq bo'lishi mumkin bo'lgan turli kitoblarimiz bor!")
# elif "sport" in qiziqish:
#     tur = input("Sizga qaysi sport turi yoqadi? ").lower()
#     if "futbol" in tur:
#         club = input("Qaysi klubga muhlislik qilasiz? ").lower()
#         if "real" in club or "barsa" in club or "barcelona" in club:
#             print("Sizga El Clasico o'yiniga chipta sovg'a qilamiz!")
# # else larni GPT maslahat berdi tepani o'zim yozdim
#         else:
#             print("Sizga sevimli jamoangizning maxsus sovg'asini beramiz!")
#     else:
#         print("Sizning sportga qiziqishingiz biz uchun qiziq, sovg'a tayyorlaymiz!")
# else:
#     print("Ajoyib! Sizning qiziqishingizni bilish biz uchun muhim!")
