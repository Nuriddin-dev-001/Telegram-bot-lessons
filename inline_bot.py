import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, BotCommand, InputMediaPhoto, ReplyKeyboardRemove
ADMIN_ID = 392330197
TOKEN = "6255255483:AAEGa_tglVQJK74IcUEGCOsfZkEoVzz74dI"

buttons = [
    [InlineKeyboardButton(text="Send Photo", callback_data="send_photo"),
     InlineKeyboardButton(text="Send Document", callback_data="send_document"),
     InlineKeyboardButton(text="Change Photo", callback_data="change_photo"),
     ],
        [InlineKeyboardButton(text="Send Media Group", callback_data="send_group")]
]
def start_func(update, context):
    # commands = [BotCommand(command='start', description="Botga start berish"),
    #             BotCommand(command='info', description="Bot haqida ma'lumot"),
    #             ]
    # context.bot.set_my_commands(commands=commands)
    update.message.reply_photo(
        # photo=open('photos/hi_bot.jpg', 'rb'),
        photo='https://picsum.photos/400/200',
        caption="Hello!!!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

def message_handler(update, context):
    # context.user_data - har bir user uchun maxsus dict o'zgaruvchi
    if context.user_data.get('matn'):
        words = context.user_data['matn']
    else:
        words = []
    words.append(update.message.text)
    context.user_data['matn'] = words
    print(f"{update.message.from_user.username}: {words}")


def inline_messages(update, context):
    query = update.callback_query
    print(query)
    if query.data == 'send_document':
        query.message.reply_document(
            document=open('register_bot.py'),
            caption='1-dars',
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == 'send_photo':
        query.message.reply_photo(
            photo=f'https://picsum.photos/id/{random.randint(1,100)}/400/200',
            caption='Random Photo',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
    elif query.data == 'change_photo':
        query.message.edit_media(media=InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(1,100)}/400/200'))

        query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    elif query.data == 'send_group':
        query.message.reply_media_group(
            media=[
                InputMediaPhoto(media=open('photos/programmist.png','rb')),
                InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(1, 100)}/400/200'),
                InputMediaPhoto(media=f'https://picsum.photos/id/{random.randint(20, 100)}/400/200')
            ]
        )
def photo_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download('photos/user_photo.jpg')
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start_func))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
dispatcher.add_handler(CallbackQueryHandler(inline_messages))
dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))
updater.start_polling()
updater.idle()

