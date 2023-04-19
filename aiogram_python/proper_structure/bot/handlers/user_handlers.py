from aiogram import types, Dispatcher


async def cmd_start(msg: types.Message) -> None:
    """Processes CMD START
    """
    
    await msg.answer(
        text='Hello World!'
    )


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start', 'help'])

