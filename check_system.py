#!/usr/bin/env python3
"""
Проверка системы перед установкой OZON Status Bot на Python 3.8+ и систему Linux
"""
import sys
import subprocess
import platform

def check_python_version():
    """Проверка версии Python"""
    version = sys.version_info
    print(f"🐍 Python версия: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python версия подходящая (3.8+)")
        return True
    else:
        print("❌ Нужен Python 3.8 или выше")
        return False

def check_pip():
    """Проверка pip"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ pip доступен: {result.stdout.strip()}")
            return True
        else:
            print("❌ pip не найден")
            return False
    except Exception as e:
        print(f"❌ Ошибка проверки pip: {e}")
        return False

def check_system():
    """Проверка операционной системы"""
    os_name = platform.system()
    print(f"💻 Операционная система: {os_name}")
    return True

def main():
    print("=" * 50)
    print("🔍 ПРОВЕРКА СИСТЕМЫ ДЛЯ OZON STATUS BOT")
    print("=" * 50)
    
    checks = [
        ("Python версия", check_python_version),
        ("pip установлен", check_pip),
        ("Система", check_system),
    ]
    
    all_passed = True
    
    for name, check_func in checks:
        print(f"\n📋 Проверка: {name}")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ!")
        print("✅ Можно устанавливать зависимости:")
        print("   pip install -r requirements.txt")
    else:
        print("❌ ЕСТЬ ПРОБЛЕМЫ!")
        print("🔧 Установите Python 3.8+ и pip перед продолжением")
    print("=" * 50)

if __name__ == "__main__":
    main()
