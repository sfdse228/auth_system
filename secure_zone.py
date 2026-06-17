"""
secure_zone.py - Защищённая зона (доступна только после входа)
"""

import datetime
import platform
import os
import sys


class SecureZone:
    """Класс для работы с защищённой зоной"""
    
    def __init__(self, username):
        """
        Инициализация защищённой зоны
        
        Args:
            username: имя авторизованного пользователя
        """
        self.username = username
    
    def show_menu(self):
        """
        Задание 4: Меню защищённой зоны
        """
        while True:
            print("\n" + "=" * 40)
            print(f"🔒 ЗАЩИЩЁННАЯ ЗОНА")
            print(f"👤 Пользователь: {self.username}")
            print("=" * 40)
            print("1. 📊 Посмотреть статус системы")
            print("2. 🚪 Выйти из защищённой зоны")
            print("=" * 40)
            
            choice = input("Выберите действие (1-2): ").strip()
            
            if choice == "1":
                self._show_system_status()
            elif choice == "2":
                print("👋 Выход из защищённой зоны...")
                break
            else:
                print("❌ Неверный выбор. Попробуйте снова.")
    
    def _show_system_status(self):
        """
        Показывает статус системы (информация о системе)
        """
        print("\n" + "=" * 40)
        print("📊 СТАТУС СИСТЕМЫ")
        print("=" * 40)
        
        # Информация о системе
        print(f"🖥️ Операционная система: {platform.system()} {platform.release()}")
        print(f"💻 Имя компьютера: {platform.node()}")
        print(f"🐍 Версия Python: {platform.python_version()}")
        print(f"📁 Текущая директория: {os.getcwd()}")
        
        # Время
        now = datetime.datetime.now()
        print(f"🕐 Текущее время: {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📅 День недели: {now.strftime('%A')}")
        
        # Информация о пользователе
        print(f"\n👤 Авторизован как: {self.username}")
        print(f"🔐 Статус: Активен")
        
        print("=" * 40)
        input("\nНажмите Enter для продолжения...")