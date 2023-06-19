from aiogram import Router
from aiogram.types import CallbackQuery, Message

router: Router = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')

@router.callback_query()
async def send_echo(callback: CallbackQuery):
    print(callback)
    print(callback.data)