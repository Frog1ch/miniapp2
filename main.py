from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

def start(update, context):
    # Ссылка на ваше мини-приложение
    url = "https://github.com/Frog1ch/miniapp2.git"
    button = InlineKeyboardButton(text="Open Mini App", url=url)
    keyboard = InlineKeyboardMarkup([[button]])
    update.message.reply_text("Click to open the mini app:", reply_markup=keyboard)

def main():
    # Токен вашего бота
    updater = Updater("7847413695:AAFKSXeqHvnc051Nqnq8nkwvqFCeKaWTzTI")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
