import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "RenamerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command
@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        "👋 Hi! I can rename your files & change thumbnails.\n\nSend me a file to start.",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("Developer", url="https://t.me/YourUsername")]]
        )
    )

# Handle documents/videos
@bot.on_message(filters.document | filters.video)
async def rename_file(client, message):
    file = message.document or message.video
    filename = file.file_name

    new_name = filename.replace(" ", "_")  # simple rename example
    await message.download(file_name=new_name)
    await message.reply_document(new_name, caption="✅ Renamed Successfully!")

bot.run()
