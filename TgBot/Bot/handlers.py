from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Database.database import Database
from Bot.keyboards import keyboard, get_number
from Bot.status import Clients
from aiogram.fsm.context import FSMContext

db = Database()
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствую!",reply_markup=keyboard)
    
@router.message(F.text == 'Запись')
async def get_help(message: Message, state: FSMContext):
    await state.set_state(Clients.name)
    await message.answer(f'Введите ваше - Имя')

@router.message(Clients.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Clients.NumberPhone)
    await message.answer("Введите ваш номер", reply_markup=get_number)

@router.message(Clients.NumberPhone)
async def register_numberPhone(message: Message, state: FSMContext):
    if message.text != None:
        await state.update_data(numberPhone=message.text)
    else:
        await state.update_data(numberPhone=message.contact.phone_number)
    await state.set_state(Clients.Address)
    await message.answer("Введите ваш адресс")


@router.message(Clients.Address)
async def register_Address(message: Message, state: FSMContext):
    await state.update_data(Address=message.text)
    data = await state.get_data()
    await message.answer(f'Ваше имя: {data["name"]}\nВаш номер: {data["numberPhone"]}\nВаш адрес: {data["Address"]}')
    await message.answer("Вы успешно зарегестрировались!", reply_markup=keyboard)
    db.set_query(data["name"], data["numberPhone"], data["Address"])
    await state.clear()