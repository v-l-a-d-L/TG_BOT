from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
import markups
from states.test import Test

@dp.callback_query_handler(text = "push_documents")
async def ChooseCity(call: types.CallbackQuery()):
	await call.message.edit_text("Выберите город", reply_markup = markups.cyties_list)
	await Test.city.set()

@dp.callback_query_handler(state = Test.city)
async def UserCity(call: types.CallbackQuery(), state: FSMContext):
	await state.update_data(city=call.data)
	await Test.next()
	await call.message.edit_text("Напишите своё ФИО одним сообщением \n Например: Иванов Иван Иванович")

@dp.message_handler(state=Test.Name)
async def UserName(message: types.Message, state: FSMContext):
	await state.update_data(name=message.text)
	await Test.next()
	await message.answer("Напишите свой адрес")

@dp.message_handler(state=Test.Addres)
async def UserAddress(message: types.Message, state: FSMContext):
	data = await state.get_data()
	await message.answer("Ваши данные успешно отправлены")
	await message.answer(data.get('city'), data.get('name'), message.text)

