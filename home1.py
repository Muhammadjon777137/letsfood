from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from logging import basicConfig, getLogger, INFO
from key import til_menu, Settings_menu,main_menu, change_phone
user_data = {}
basicConfig(level=INFO)
log = getLogger()
text = """Welcome to "Let's Food" - food service and delivery bot! Our bot is ready to offer you different dishes every day according to the menu. We work from 11:00 to 20:00 so that your lunch is tasty and timely.
Details about our menu can be found by following us on Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , for instruction on how to use the bot press /instruction 
We are ready to satisfy every taste and make your dinner unforgettable!

Also, we are pleased to announce that when ordering more than 5 servings, delivery is free! There are two types of portions in our menu: "Set" and "Half-set".
Serving cost:

"Set" is 40,000 sum

"Partial Set" - 35,000 sum

We guarantee that each meal will be fresh, tasty and prepared with love. We are waiting for your order!

Eat delicious every day
@letfood_bot """

BOT_TOKEN = "7180499633:AAHyFkeQjaW-s7J5BTR-u92jo_WbMzgVF6I"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_bot(message: types.Message):
    await message.answer("Tilni tanlang",reply_markup=til_menu())


@dp.message_handler(Text(equals="English 🇺🇸"))
async def start_bot(message: types.Message):
    with open("letsfood.jpg", "rb") as photo:
        await message.answer_photo(photo=photo, caption="""Welcome to "Let's Food" - food service and delivery bot! Our bot is ready to offer you different dishes every day according to the menu. We work from 11:00 to 20:00 so that your lunch is tasty and timely.
Details about our menu can be found by following us on Instagram   @letsfood_tashkent (https://www.instagram.com/letsfood_tashkent) , for instruction on how to use the bot press /instruction 
We are ready to satisfy every taste and make your dinner unforgettable!

Also, we are pleased to announce that when ordering more than 5 servings, delivery is free! There are two types of portions in our menu: "Set" and "Half-set".
Serving cost:

"Set" is 40,000 sum

"Partial Set" - 35,000 sum

We guarantee that each meal will be fresh, tasty and prepared with love. We are waiting for your order!

Eat delicious every day
@letfood_bot """,)
    await message.answer("Language changed to 🇺🇸", reply_markup=main_menu())

@dp.message_handler(Text(equals="Order 🛍"))
async def start_bot(message: types.Message):
    await message.answer("""Sorry for inconvenience, but we are run out of orders
Try new tastes tomorrow!
@letsfood_bot""")

@dp.message_handler(Text(equals="Info ℹ️"))
async def start_bot(message: types.Message):
    await message.answer("""📌 Here you can find information about our restaurant    
📞 Phone number: +998(90) 177-73-37
🕐 Working time: 10:00 - 20:00
⚡️Contact: @letsfood_bot_admin""")


@dp.message_handler(Text(equals="Settings⚙️"))
async def start_bot(message: types.Message):
    await message.answer("Change settings", reply_markup=Settings_menu())

@dp.message_handler(Text(equals="Change name ✏️"))
async def start_bot(message: types.Message):
    await message.answer("Enter your name:")

@dp.message_handler(Text(equals="Dilshod"))
async def set_name(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = message.text  # Save the user's name
    await message.reply("Your name has been changed!", reply_markup=Settings_menu())

@dp.message_handler(Text(equals="Feedback  📩"))
async def start_bot(message: types.Message):
    await message.answer("Send your feedback")

@dp.message_handler(Text(equals="Yaxshi joy ekan"))
async def set_name(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = message.text  # Save the user's name
    await message.reply("Feedback sent", reply_markup=main_menu())



@dp.message_handler(Text(equals="Change phone 📱"))
async def start_bot(message: types.Message):
    await message.answer("""Enter your phone number or share your contact:
Example: 90 123 45 67
Your current phone""", reply_markup=change_phone())

@dp.message_handler(content_types=["contact"])
async def start_bot(message: types.Message):
    await message.answer("Your phone number has been changed!",
                         reply_markup=main_menu())




@dp.message_handler(Text(equals="Change language 🇺🇿"))
async def start_bot(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=til_menu())

@dp.message_handler(Text(equals="Back ⬅️"))
async def start_bot(message: types.Message):
    await message.answer("Back", reply_markup=main_menu())



if __name__ == '__main__':
    executor.start_polling(dp)