from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.types import InputMediaPhoto

TOKEN = "8434165984:AAEeHEiQT3aOTKeUW-_fEbYaVG-rvrDRg3Y"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add("📚 Anatomiya")
main_menu.add("📝 Test")
main_menu.add("⭐ Qiyin mavzular")

anatomiya_menu = ReplyKeyboardMarkup(resize_keyboard=True)
anatomiya_menu.add("I BO‘LIM — Sistema digestorium")
anatomiya_menu.add("II BO‘LIM — Sistema respiratorium")
anatomiya_menu.add("III BO‘LIM — Sistema urinaria")
anatomiya_menu.add("IV BO‘LIM — Sistema genitalia")
anatomiya_menu.add("V BO‘LIM — Sistema endocrin")
anatomiya_menu.add("VI BO‘LIM — Angiologia")
anatomiya_menu.add("VII BO‘LIM — Sistema phlebs")
anatomiya_menu.add("VIII BO‘LIM — Sistema lymphaticum")
anatomiya_menu.add("IX BO‘LIM — Sistema immunis")
anatomiya_menu.add("⬅️ Orqaga")

thorax_menu = ReplyKeyboardMarkup(resize_keyboard=True)
thorax_menu.add("🦴 Skelet")
thorax_menu.add("❤️ Yurak")
thorax_menu.add("🫁 O‘pka")
thorax_menu.add("⬅️ Orqaga")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("MedStructure botiga xush kelibsiz!", reply_markup=main_menu)

@dp.message_handler()
async def handle(message: types.Message):
    

    if message.text == "📚 Anatomiya":
        await message.answer("Anatomiya bo‘limi:", reply_markup=anatomiya_menu)

    elif message.text == "I BO‘LIM — Sistema digestorium":
        digest_menu = ReplyKeyboardMarkup(resize_keyboard=True)
        digest_menu.add("Og‘iz bo‘shlig‘i")
        digest_menu.add("Tishlar")
        digest_menu.add("Til")
        digest_menu.add("Tanglay")
        digest_menu.add("Halqum")
        digest_menu.add("Qizilo‘ngach")
        digest_menu.add("Oshqozon")
        digest_menu.add("Jigar")
        digest_menu.add("⬅️ Orqaga")
    
        await message.answer("SISTEMA DIGESTORIUM", reply_markup=digest_menu)

    elif message.text == "Og'iz bo‘shlig‘i":
        media = [
        InputMediaPhoto(open("ogiz1.jpg", "rb")),
        InputMediaPhoto(open("ogiz2.jpg", "rb")),
        InputMediaPhoto(open("ogiz3.jpg", "rb")),
        InputMediaPhoto(
            open("ogiz4.jpg", "rb"),
            caption="🦷 OG‘IZ BO‘SHLIG‘I — Cavitas oris\n\n"
                "📌 2 qismga bo‘linadi:\n\n"

                "1️⃣ Og‘iz dahlizi — Vestibulum oris\n"
                "🔹 Oldindan: lablar (labium) va lunj (buccalis)\n"
                "🔹 Orqadan: tishlar (dentes) va milk (gingiva)\n"
                "🔹 Kirish qismi: og‘iz tirqishi (rima oris)\n"
                "📎 Og‘iz dahlizida alohida anatomik tuzilma yo‘q.\n\n"

                "2️⃣ Xususiy og‘iz bo‘shlig‘i — Cavitas oris propria\n"
                "🔹 Oldindan: tishlar\n"
                "🔹 Pastdan: og‘iz diafragmasi (diaphragma oris)\n"
                "🔹 Yuqoridan: qattiq va yumshoq tanglay "
                "(palatum durum et molle)\n"
                "🔹 Orqadan: tomoq teshigi (fauces)\n\n"

                "━━━━━━━━━━━━━━━━━━\n"
                "💋 LAB TUZILISHI:\n\n"

                "1️⃣ Pars cutanea — teri qavati\n"
                "Faqat epidermis qavati mavjud.\n"
                "Ostidaki mushak ko‘rinib, qizg‘ish tus beradi.\n\n"

                "2️⃣ Pars intermedia (pars muscularis)\n"
                "m. orbicularis oris hosil qiladi.\n\n"

                "3️⃣ Pars mucosa — shilliq qavat\n"
                "Lab bezlari (glandula labialis) joylashgan.\n"
                "Shilliq qavatni namlab turadi.\n\n"

                "📎 Lab shilliq qavatida:\n"
                "Frenulum labii superioris\n"
                "Frenulum labii inferioris\n\n"

                "‼ Pastgi yuganchasi yuqorigisiga nisbatan "
                "kattaroq va yaqqolroq ko‘rinadi."
            )
        ]

        await message.answer_media_group(media)
    

    elif message.text == "❤️ Yurak":
        await message.answer("Lotin: Cor\nO‘zbek: Yurak\n\n4 kamerali mushakli organ.")

    elif message.text == "🫁 O‘pka":
        await message.answer("Lotin: Pulmo\nO‘zbek: O‘pka\n\nGaz almashinuvi uchun javobgar organ.")

    elif message.text == "⬅️ Orqaga":
        await message.answer("Asosiy menyu:", reply_markup=main_menu)

    else:
        await message.answer("Menyudan tanlang.")

if __name__ == "__main__":

    executor.start_polling(dp, skip_updates=True)
