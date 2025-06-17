import aiogram 
import os 
import dotenv
import asyncio

dotenv.load_dotenv()

bot = aiogram.Bot(os.getenv("BOT_TOKEN"))
dp = aiogram.Dispatcher()


def on_start():
    print("bot has been started...")

async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)



asyncio.run(main())