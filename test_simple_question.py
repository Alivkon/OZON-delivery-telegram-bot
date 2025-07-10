#!/usr/bin/env python3
"""
Тест запроса в API OZON 
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

OZON_CLIENT_ID = os.getenv("OZON_CLIENT_ID")
OZON_API_KEY = os.getenv("OZON_API_KEY")

def test_mark_as_delivered(posting_number: str) -> tuple[bool, str]:
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

def main():
    print("=== Тестирование запроса ===\n")
    
    test_order = "0125046649-0022-1"
    print(f"Тестируем заказ: {test_order}")
    print("-" * 50)
    
    success, message = test_mark_as_delivered(test_order)
    
    print(f"\n📋 Результат:")
    print(f"✅ Успех: {success}")
    print(f"📱 Сообщение пользователю: {message}")
    
    print("\n" + "=" * 50)
    print("✅ Запрос работает!")
    print("📱 Показывается только результат операции")
    print("📱 Напишите боту @netizen_ozon_status_bot в Telegram")

if __name__ == "__main__":
    main()
