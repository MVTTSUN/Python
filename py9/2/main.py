from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Приветствую, {update.effective_user.first_name}!')


app = ApplicationBuilder().token("5952090498:AAElZWZ-h4I-RCuQfPmZU2JYnSZwt0y193c").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()