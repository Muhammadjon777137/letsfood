from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def til_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="English 🇺🇸"), KeyboardButton(text="Russia 🇷🇺"), KeyboardButton(text="Uzbekistan 🇺🇿"))
    return rkm

def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="Order 🛍"), KeyboardButton(text="Info ℹ️"))
    rkm.add(KeyboardButton(text="Settings⚙️"), KeyboardButton(text="Feedback  📩"))
    return rkm


def Settings_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="Change name ✏️"), KeyboardButton(text="Change phone 📱"))
    rkm.add(KeyboardButton(text="Change language 🇺🇿"), KeyboardButton(text="Back ⬅️"))
    return rkm

def change_phone():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.add(KeyboardButton(text="Share your contact", request_contact=True))
    rkm.add(KeyboardButton(text="Back ⬅️"))
    return rkm