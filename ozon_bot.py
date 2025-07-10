import logging
import requests
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OZON_CLIENT_ID = os.getenv("OZON_CLIENT_ID")
OZON_API_KEY = os.getenv("OZON_API_KEY")

if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN environment variable is not set")

if OZON_CLIENT_ID is None:
    raise ValueError("OZON_CLIENT_ID environment variable is not set")
    
if OZON_API_KEY is None:
    raise ValueError("OZON_API_KEY environment variable is not set")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_order_input: dict[int, str] = {}

def mark_as_delivered(posting_number: str) -> tuple[bool, str]:
    url = "https://api-seller.ozon.ru/v2/fbs/posting/delivered"
    headers = {
        "Client-Id": OZON_CLIENT_ID,
        "Api-Key": OZON_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "posting_number": [posting_number]
    }

    response = requests.post(url, headers=headers, json=payload)
    print(f"Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        try:
            result = response.json()
            if result.get("result") and len(result["result"]) > 0:
                order_result = result["result"][0]
                if order_result.get("result") is True:
                    return True, "✅ Статус успешно изменён на 'Доставлено'"
                else:
                    error_msg = order_result.get("error", "Неизвестная ошибка")
                    if error_msg == "TRANSITION_IS_NOT_POSSIBLE":
                        return False, "❌ Невозможно изменить статус этого заказа на ДОСТАВЛЕНО"
                    else:
                        return False, f"❌ Не удалось изменить статус: {error_msg}"
            else:
                return False, "❌ Пустой ответ от API"
        except Exception as e:
            return False, f"❌ Ошибка обработки ответа: {e}"
    else:
        try:
            error = response.json()
        except:
            error = response.text
        return False, f"❌ Ошибка API ({response.status_code}): {error}"


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Введите номер заказа (posting_number):")


@dp.message()
async def handle_order_input(message: types.Message):
    if message.from_user is None or message.text is None:
        await message.answer("Ошибка: не удалось определить пользователя или текст сообщения.")
        return
    user_id = message.from_user.id
    user_order_input[user_id] = message.text.strip()

    kb = InlineKeyboardBuilder()
    kb.row(InlineKeyboardButton(text="✅ Доставлено", callback_data="mark_delivered"))
    await message.answer(
        f"Номер заказа: {user_order_input[user_id]}\nПодтвердите статус",
        reply_markup=kb.as_markup()
    )


@dp.callback_query()
async def handle_button(callback: types.CallbackQuery):
    if callback.from_user is None:
        return
        
    user_id = callback.from_user.id

    if callback.data == "mark_delivered":
        posting_number = user_order_input.get(user_id)
        
        if not posting_number:
            await callback.answer("Номер заказа не найден.", show_alert=True)
            return

        try:
            success, msg = mark_as_delivered(posting_number)
            
            # Отправляем результат пользователю
            await bot.send_message(user_id, msg)
            await callback.answer()
            
        except Exception as e:
            await callback.answer(f"Ошибка: {e}", show_alert=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    dp.run_polling(bot)
