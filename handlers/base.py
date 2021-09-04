import markups
from aiogram import types
from loader import dp
@dp.message_handler(commands=["start"])
async def Start(message : types.Message):
	await message.answer(text = markups.main_handler, reply_markup= markups.main_menu)

@dp.callback_query_handler(text="FAQ")
async def FAQ(call: types.CallbackQuery):
	await call.message.edit_text("Часо задаваемые вопросы", reply_markup = markups.FAQ)

@dp.callback_query_handler(text="start")
async def Back(call: types.CallbackQuery):
	await call.message.edit_text(text = markups.main_handler, reply_markup = markups.main_menu)

