from aiogram import types 


async def cmd_start(msg: types.Message) -> None:
    await msg.answer('Hello World!')
    
    
def register_user_handlers(dp) -> None:
    dp.register_message_handler(cmd_start, commands=['start', 'help'])
