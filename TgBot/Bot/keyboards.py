from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Запись'
            ), 
        KeyboardButton(
            text='Информация'
            )
    ]
    
],
resize_keyboard=True, input_field_placeholder='Выберите нужную кнопку...')

get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]], resize_keyboard=True)