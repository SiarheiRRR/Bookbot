from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()

class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback, str) and callback.endswith('del') and callback[:-3].isdigit()