from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
main_handler = "Чем я могу вам помочь?"

main_menu = InlineKeyboardMarkup(row_width = 1)
but_FAQ = InlineKeyboardButton("Часто задаваенмые вопросы",callback_data="FAQ")
but_send_doc = InlineKeyboardButton("Направить документы",callback_data = "push_documents")
but_check_list = InlineKeyboardButton("Узнать очередь",callback_data="check_list")
but_instruction = InlineKeyboardButton("Порядок оформления",callback_data="instruction")
but_back = InlineKeyboardButton('Назад \n \U00002b05', callback_data = "start")
main_menu.add(but_FAQ,but_send_doc,but_check_list,but_instruction)

FAQ = InlineKeyboardMarkup(row_width = 1)
FAQ.add(but_back)


cyties_list = InlineKeyboardMarkup(row_width = 1)
Saratov = InlineKeyboardButton("Саратов", callback_data = "Saratov")
Mokrous = InlineKeyboardButton("Мокроус", callback_data = "Mokrous")
Balashov = InlineKeyboardButton("Балашов", callback_data = "Balashov")
cyties_list.add(Saratov,Mokrous,Balashov)