
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
FORM_LINK = os.getenv("FORM_LINK")

EVENTS_INFO = """
📚 Вдячність поміж рядків

Дата: 15 травня
Місце: Київ

Опис:
Збір україномовних книг для військових у медичні та реабілітаційні заклади.
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я помічник заходів 🤖\n\n"
        "Можу розповісти про заходи та дати посилання на реєстрацію.\n\n"
        "Напиши:\n"
        "• заходи\n"
        "• реєстрація\n"
        "• контакти"
    )

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "захід" in text or "заходи" in text or "подія" in text:
        await update.message.reply_text(EVENTS_INFO)

    elif "реєстрац" in text or "зареєстру" in text or "форма" in text:
        await update.message.reply_text(
            f"Ось посилання на реєстрацію:\n{FORM_LINK}"
        )

    elif "контакт" in text or "організатор" in text:
        await update.message.reply_text(
            "З питань щодо заходу зверніться до організатора.\n\n"
            "Можеш тут написати свій контакт або питання у формі реєстрації."
        )

    elif "привіт" in text or "добрий" in text:
        await update.message.reply_text(
            "Привіт! 😊 Напиши “заходи”, щоб побачити доступні події."
        )

    else:
        await update.message.reply_text(
            "Я можу допомогти з інформацією про заходи та реєстрацію.\n\n"
            "Напиши “заходи” або “реєстрація”."
        )

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer))

print("Bot without AI is running...")
app.run_polling()
