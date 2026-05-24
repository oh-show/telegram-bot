from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from groq import Groq

# Telegram токен
TELEGRAM_TOKEN = "8397009892:AAG5JOo6KhP5MwuUM9R7kOQy4koRrv1oBxg"

# Groq API
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
Ты загадочный персонаж.
Ты создаешь ощущение тайны.
Никогда не говори, что ты ИИ.
Отвечай коротко и атмосферно.
""",
            },
            {"role": "user", "content": user_message},
        ],
    )

    reply = response.choices[0].message.content

    await update.message.reply_text(reply)


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")

app.run_polling()
