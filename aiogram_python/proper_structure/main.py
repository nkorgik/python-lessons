import asyncio
import os

from aiogram import types, Bot, Dispatcher
from dotenv import load_dotenv

from bot.handlers.user_handlers import register_user_handlers


def register_handlers(dp) -> None:
    register_user_handlers(dp)


async def main():
    load_dotenv('.env')
    token = os.getenv('TOKEN_API')
    
    bot = Bot(token)
    dp = Dispatcher(bot)
    
    register_handlers(dp)
    
    try:
        await dp.start_polling()
    except Exception as _ex:
        print(f'Exception - {_ex}')


if __name__ == "__main__":
    asyncio.run(main())
