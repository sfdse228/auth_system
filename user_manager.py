"""
user_manager.py - Управление пользователями (регистрация, хранение)
"""

import os
import json


class UserManager:
    """Класс для управления пользователями"""
    
    def __init__(self, users_file="data/users.json"):
        """
        Инициализация менеджера пользователей
        
        Args:
            users_file: путь к файлу с пользователями
        """
        self.users_file = users_file
        self.users = {}
        self._ensure_data_dir()
        self._load_users()
    
    def _ensure_data_dir(self):
        """Создаёт папку для данных если её нет"""
        data_dir = os.path.dirname(self.users_file)
        if data_dir and not os.path.exists(data_dir):
            os.makedirs(data_dir)
    
    def _load_users(self):
        """Загружает пользователей из JSON-файла"""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r', encoding='utf-8') as f:
                    self.users = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.users = {}
        else:
            self.users = {}
            self._save_users()
    
    def _save_users(self):
        """Сохраняет пользователей в JSON-файл"""
        with open(self.users_file, 'w', encoding='utf-8') as f:
            json.dump(self.users, f, ensure_ascii=False, indent=2)
    
    def user_exists(self, login):
        """Проверяет, существует ли пользователь"""
        return login in self.users
    
    def register_user(self, login, password):
        """
        Регистрирует нового пользователя
        
        Returns:
            (success: bool, message: str)
        """
        # Проверка на пустой логин
        if not login or not login.strip():
            return False, "Логин не может быть пустым"
        
        # Проверка на пустой пароль
        if not password or not password.strip():
            return False, "Пароль не может быть пустым"
        
        # Проверка на занятость логина
        if self.user_exists(login):
            return False, f"Пользователь '{login}' уже существует"
        
        # Регистрируем пользователя
        self.users[login] = password
        self._save_users()
        return True, f"Пользователь '{login}' успешно зарегистрирован"
    
    def verify_user(self, login, password):
        """
        Проверяет логин и пароль
        
        Returns:
            (success: bool, message: str)
        """
        if not self.user_exists(login):
            return False, f"Пользователь '{login}' не найден"
        
        if self.users[login] != password:
            return False, "Неверный пароль"
        
        return True, "Успешный вход"