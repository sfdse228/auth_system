#!/usr/bin/env python3
"""
main.py - Точка входа в приложение (CLI)
"""

import sys
import os

# Добавляем путь к модулям
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.auth import AuthSystem
from src.secure_zone import SecureZone
from src.logger_setup import logger


def show_main_menu():
    """Показывает главное меню"""
    print("\n" + "=" * 40)
    print("🔐 СИСТЕМА АВТОРИЗАЦИИ")
    print("=" * 40)
    print("1. 🔑 Войти")
    print("2. 📝 Зарегистрироваться")
    print("3. 🚪 Выйти")
    print("=" * 40)


def main():
    """Главная функция"""
    auth = AuthSystem()
    
    print("\n" + "=" * 40)
    print("🔐 ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ")
    print("=" * 40)
    
    while True:
        show_main_menu()
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == "1":
            # Задание 3: Вход
            print("\n🔑 ВХОД В СИСТЕМУ")
            login = input("Логин: ").strip()
            password = input("Пароль: ").strip()
            
            success, message = auth.login(login, password)
            print(f"\n{message}")
            
            if success:
                # Задание 4: Переход в защищённую зону
                secure_zone = SecureZone(auth.current_user)
                secure_zone.show_menu()
                
                # Выход из защищённой зоны
                auth.logout()
                print("\n👋 Вы вышли из системы")
        
        elif choice == "2":
            # Задание 2: Регистрация
            print("\n📝 РЕГИСТРАЦИЯ")
            login = input("Придумайте логин: ").strip()
            password = input("Придумайте пароль: ").strip()
            confirm = input("Подтвердите пароль: ").strip()
            
            if password != confirm:
                print("❌ Пароли не совпадают!")
                continue
            
            success, message = auth.register(login, password)
            print(f"\n{message}")
        
        elif choice == "3":
            print("\n👋 До свидания!")
            logger.info("Завершение работы программы")
            break
        
        else:
            print("❌ Неверный выбор. Попробуйте снова.")
            continue
        
        # Пауза перед показом меню
        input("\nНажмите Enter для продолжения...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Принудительное завершение...")
        logger.info("Принудительное завершение программы")
        sys.exit(0)