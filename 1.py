from telegram import Update
from telegram.ext import*
import requests
Token= "8575945448:AAEwbWd2DwzmE4R0Gt_zJDTPwmfy6e9U-4E"
API_KEY= "37d35c50"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Введите название фильма:")
async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE): 

    name= update.message.text
    url = (
        f"https://www.omdbapi.com/"
        f"?apikey={API_KEY}"
        f"&t={name}"
    )
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        title = data["Title"]
        year = data["Year"]
        genre = data["Genre"]
        director = data["Director"]
        plot= data["Plot"]
        Actors= data["Actors"]

        await update.message.reply_text(
            f"Название: {title}\n"
            f"Год: {year}\n"
            f"Жанр: {genre}\n"
            f"Режиссер: {director}\n"
            f"Сюжет: {plot}"
            f"Актеры: {Actors}"
        )
    else:
        await update.message.reply_text(
            f"Ошибка: {data['Error']}"
        )
    return ConversationHandler.END

app= ApplicationBuilder().token(Token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, movie))

app.run_polling()