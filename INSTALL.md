# 📦 Установка и запуск OZON Status Bot

### � Проверка pip
```bash
pip --version
# или
pip3 --version

# Должно показать: pip 21.x.x или выше
```

## ⚡ Быстрая проверка системы
Запустите скрипт проверки:
```bash
python check_system.py
```

Он покажет:
- ✅ Версию Python
- ✅ Доступность pip
- ✅ Информацию о системе

## 📋 Установка зависимостей проектавания
- Python 3.8+
- pip (обычно идет в комплекте с Python)

## 🐍 Установка Python

### Windows:
1. Скачайте Python с [python.org](https://www.python.org/downloads/)
2. Запустите установщик
3. ✅ **ВАЖНО**: Поставьте галочку "Add Python to PATH"
4. Нажмите "Install Now"

### macOS:
```bash
# Через Homebrew (рекомендуется)
brew install python

# Или скачайте с python.org
```

### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Linux (CentOS/RHEL):
```bash
sudo yum install python3 python3-pip
```

## 🔍 Проверка установки Python
```bash
python --version
# или
python3 --version

# Должно показать: Python 3.8.x или выше
```

## � Проверка pip
```bash
pip --version
# или
pip3 --version

# Должно показать: pip 21.x.x или выше
```

## �📋 Установка зависимостей проекта

### Способ 1: Установка из requirements.txt
```bash
pip install -r requirements.txt
```

### Способ 2: Установка по отдельности
```bash
pip install aiogram==3.13.1
pip install requests==2.31.0
pip install python-dotenv==1.0.0
```

## ⚙️ Настройка

1. **Создайте .env файл** в корне проекта:
```bash
cp .env.example .env
```
2. **Получите токен бота** от @BotFather в Telegram

3. **Получите OZON API ключи** в личном кабинете OZON Seller

4. **Заполните .env файл** своими данными:
```env
BOT_TOKEN=your_telegram_bot_token_here
OZON_CLIENT_ID=your_ozon_client_id
OZON_API_KEY=your_ozon_api_key
```



## 🚀 Запуск

### Windows:
```cmd
python ozon_bot.py
```

### macOS/Linux:
```bash
python3 ozon_bot.py
```

### Если возникают проблемы:
```bash
# Попробуйте указать полный путь к Python
/usr/bin/python3 ozon_bot.py

# Или через модуль
python -m ozon_bot
```

## 📋 Зависимости

| Пакет | Версия | Назначение |
|-------|--------|------------|
| aiogram | 3.13.1 | Telegram Bot API библиотека |
| requests | 2.31.0 | HTTP запросы к OZON API |
| python-dotenv | 1.0.0 | Загрузка переменных окружения |

## ✅ Проверка установки

Запустите тест:
```bash
python test_simple_version.py
```

Если все работает - увидите:
```
✅ Упрощенный бот работает!
```
