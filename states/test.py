from aiogram.dispatcher.filters.state import StatesGroup,State

class Test(StatesGroup):
	city = State()
	Name = State()
	Number = State()
	Addres = State()