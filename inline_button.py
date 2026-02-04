from telegram import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = "*********************************************"

buttons_data = {
    "python_info": "Python — eng yaxshi dasturlash tillaridan biri.",
    "python_library": "Numpy, Django, Aiogram",
    "java_info": "Java — Android va yirik tizimlar uchun ishlatiladi.",
    "java_library": "Spring, Hibernate, Apache Commons",
    "cpp_info": "C++ — tizim darajasidagi dasturlash uchun ideal.",
    "cpp_library": "STL, Boost, Qt",
    "csharp_info": "C# — .NET asosidagi Windows ilovalari uchun.",
    "csharp_library": "Entity Framework, ASP.NET",
    "php_info": "PHP — veb saytlar yaratishda keng qo‘llaniladi.",
    "php_library": "Laravel, Symfony, CodeIgniter",
    "javs_info": "JavaScript — frontend va Node.js orqali backendda ishlatiladi.",
    "javs_library": "React, Vue, jQuery, Node.js"
}


def start(update, context):
    commands = [BotCommand(command='start', description="Botga start berish")]
    context.bot.set_my_commands(commands=commands)
    #/start buyrug‘i kelganda, foydalanuvchi uchun /start komandasi qo‘lda ko‘rsatib qo‘yiladi.

    button = [
        [InlineKeyboardButton("Programming Language", callback_data="program_lan")]
    ]
    reply_markup = InlineKeyboardMarkup(button)
    update.message.reply_text("Assalomu alaykum! Tilni tanlang:", reply_markup=reply_markup)


def inline_messages(update, context):
    query = update.callback_query
    data = query.data
    # Foydalanuvchi biror inline tugma bosganida, bu funksiya ishlaydi. data — tugma bosilganda kelgan callback_data

    if data == "program_lan":
        langs = [
            [InlineKeyboardButton("Python", callback_data="select_python")],
            [InlineKeyboardButton("Java", callback_data="select_java")],
            [InlineKeyboardButton("C++", callback_data="select_cpp")],
            [InlineKeyboardButton("C#", callback_data="select_csharp")],
            [InlineKeyboardButton("PHP", callback_data="select_php")],
            [InlineKeyboardButton("JavaScript", callback_data="select_javs")]
        ]
        query.message.reply_text("Quyidagi tillardan birini tanlang:", reply_markup=InlineKeyboardMarkup(langs))

    elif data.startswith("select_"):    #Bu satr callback_data ning boshi "select_" bilan boshlanadimi, deb tekshiradi.
                                        #Masalan, "select_python", "select_java" kabi qiymatlar uchun true bo‘ladi.
                                        #Bu degani — foydalanuvchi dasturlash tilini tanladi.

        lang = data.split("_")[1]   #Bu yerda "select_python" ni "_" bo‘yicha bo‘lib, ikkinchi bo‘lagini oladi, ya’ni:

        buttons = [
            [InlineKeyboardButton("Info", callback_data=f"{lang}_info")],
            [InlineKeyboardButton("Libraries", callback_data=f"{lang}_library")]
        ]    #Endi foydalanuvchiga "Info" va "Libraries" degan ikkita tugma chiqariladi.
            # Ularning callback_datasi avtomatik quyidagicha bo‘ladi:
                                        # "python_info"
                                        # "python_library"
                                        # Agar til java bo‘lsa:
                                        # "java_info"
                                        # "java_library"



        query.message.reply_text(f"{lang.capitalize()} haqida ma’lumot turini tanlang:", reply_markup=InlineKeyboardMarkup(buttons))

    elif data in buttons_data:
        query.message.reply_text(buttons_data[data])


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(inline_messages))

updater.start_polling()
updater.idle()
