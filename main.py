import aiogram 
import os

import aiogram.filters 
import dotenv
import asyncio
import yt_dlp

dotenv.load_dotenv()

bot = aiogram.Bot(os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher()

@dp.message(aiogram.filters.Command("start"))
def start_handler(message: aiogram.types.Message):
    url = "https://youtube.com/shorts/5bjOrfkdNo8?si=7zDc2FvdUAlO3Wje"
    opts = {"format": "best", "outtmpl": "video.%(ext)s"}

    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.download([url])
        print(info)

def on_start():
    print("bot has been started...")

async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)



asyncio.run(main())