"""
auth.py - Бизнес-логика авторизации (попытки, блокировка)
"""

import time
from src.user_manager import UserManager
from src.logger_setup import logger


class AuthSystem:
    """Система авторизации с лимитом попыток"""
    
    MAX_ATTEMPTS = 3
    BLOCK_TIME = 5  # секунд
    
    def __init__(self):
        """Инициализация системы авторизации"""
        self.user_manager = UserManager()
        self.current_user = None
        self.is_authenticated = False
        self.failed_attempts = 0
        self.blocked_until = 0
    
    def register(self, login, password):
        """
        Задание 2: Регистрация нового пользователя
        """
        success, message = self.user_manager.register_user(login, password)
        
        if success:
            logger.info(f"Регистрация: {login} - УСПЕШНО")
        else:
            logger.warning(f"Регистрация: {login} - {message}")
        
        return success, message
    
    def login(self, login, password):
        """
        Задание 3: Авторизация с лимитом попыток
        """
        # Проверка блокировки
        if self._is_blocked():
            remaining = int(self.blocked_until - time.time()) + 1
            logger.warning(f"Попытка входа в заблокированном состоянии: {login}")
            return False, f"Система заблокирована. Подождите {remaining} секунд"
        
        # Проверка пользователя
        success, message = self.user_manager.verify_user(login, password)
        
        if success:
            # Успешный вход
            self.current_user = login
            self.is_authenticated = True
            self.failed_attempts = 0  # Сбрасываем попытки
            logger.info(f"Вход: {login} - УСПЕШНО")
            return True, "Добро пожаловать в систему!"
        
        else:
            # Неуспешный вход
            self.failed_attempts += 1
            remaining_attempts = self.MAX_ATTEMPTS - self.failed_attempts
            
            logger.warning(f"Вход: {login} - НЕУДАЧНО (попытка {self.failed_attempts}/{self.MAX_ATTEMPTS})")
            
            if self.failed_attempts >= self.MAX_ATTEMPTS:
                # Превышение лимита - блокировка
                self._block_system()
                logger.error(f"ПРЕВЫШЕНИЕ ЛИМИТА ПОПЫТОК: {login} - система заблокирована на {self.BLOCK_TIME}с")
                return False, f"Превышен лимит попыток! Система заблокирована на {self.BLOCK_TIME} секунд"
            
            return False, f"Неверный логин или пароль. Осталось попыток: {remaining_attempts}"
    
    def logout(self):
        """Выход из системы"""
        if self.is_authenticated:
            logger.info(f"Выход: {self.current_user}")
            self.current_user = None
            self.is_authenticated = False
            return True, "Вы вышли из системы"
        return False, "Вы не авторизованы"
    
    def _is_blocked(self):
        """Проверяет, заблокирована ли система"""
        if self.blocked_until == 0:
            return False
        return time.time() < self.blocked_until
    
    def _block_system(self):
        """Блокирует систему на BLOCK_TIME секунд"""
        self.blocked_until = time.time() + self.BLOCK_TIME
        self.failed_attempts = 0
    
    def is_authenticated(self):
        """Возвращает статус авторизации"""
        return self.is_authenticated
    
    def get_current_user(self):
        """Возвращает текущего пользователя"""
        return self.current_user
