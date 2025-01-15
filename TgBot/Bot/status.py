from aiogram.fsm.state import State, StatesGroup

class Clients(StatesGroup):
    name = State()
    NumberPhone = State()
    Address = State()
    