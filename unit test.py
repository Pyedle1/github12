#2. Unit-тесты (test_email_validator.py)

import unittest
from email_validator import validate_email

class TestEmailValidator(unittest.TestCase):
    
    def test_valid_emails(self):
        """Тестирование валидных email адресов"""
        valid_emails = [
            "user@example.com",
            "user.name@example.com",
            "user-name@example.com",
            "user_name@example.com",
            "username@example.co.uk",
            "user+tag@example.com",
            "user123@example.com",
            "user@subdomain.example.com",
            "user@example.io",
            "user@example.technology",
            "a@b.c",  # Минимальный валидный email
            "user@example-domain.com",
            "user@example.museum",
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email), f"Email '{email}' должен быть валидным")
    
    def test_invalid_emails(self):
        """Тестирование невалидных email адресов"""
        invalid_emails = [
            "",  # Пустая строка
            None,  # None значение
            "user",  # Нет @ и домена
            "user@",  # Нет домена
            "@example.com",  # Нет локальной части
            "user@.com",  # Домен начинается с точки
            "user@example.",  # Домен заканчивается точкой
            "user@example..com",  # Две точки подряд
            "user@example.c",  # Доменная зона слишком короткая
            "user@example.c0m",  # Цифры в доменной зоне
            "user name@example.com",  # Пробел в локальной части
            "user@example.com.",  # Заканчивается точкой
            ".user@example.com",  # Начинается с точки
            "user..name@example.com",  # Две точки подряд в локальной части
            "user@-example.com",  # Домен начинается с дефиса
            "user@example-.com",  # Домен заканчивается дефисом
            "a" * 65 + "@example.com",  # Локальная часть длиннее 64 символов
            "user@" + "a" * 64 + ".com",  # Длинная локальная часть
            "user@example." + "a" * 64,  # Длинная доменная зона
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email), f"Email '{email}' должен быть невалидным")
    
    def test_edge_cases(self):
        """Тестирование граничных случаев"""
        # Максимальная длина локальной части (64 символа)
        local_part_64 = "a" * 64
        email_64 = f"{local_part_64}@example.com"
        self.assertTrue(validate_email(email_64))
        
        # Локальная часть 65 символов
        local_part


65 = "a" * 65
        email_65 = f"{local_part_65}@example.com"
        self.assertFalse(validate_email(email_65))
        
        # Допустимые символы в локальной части
        special_chars_email = "user.+_-%@example.com"
        self.assertTrue(validate_email(special_chars_email))
        
        # Много поддоменов
        many_subdomains = "user@sub1.sub2.sub3.sub4.example.com"
        self.assertTrue(validate_email(many_subdomains))
        
        # Цифры в домене
        domain_with_numbers = "user@example123.com"
        self.assertTrue(validate_email(domain_with_numbers))
    
    def test_type_validation(self):
        """Тестирование проверки типов данных"""
        self.assertFalse(validate_email(123))  # Число
        self.assertFalse(validate_email(["user@example.com"]))  # Список
        self.assertFalse(validate_email({"email": "user@example.com"}))  # Словарь
        self.assertFalse(validate_email(True))  # Boolean

if __name__ == '__main__':
    # Создание тестового набора
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmailValidator)
    
    # Запуск тестов с детальным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Вывод статистики
    print("\n" + "="*50)
    print(f"Результаты тестирования:")
    print(f"Запущено тестов: {result.testsRun}")
    print(f"Успешно: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Ошибок: {len(result.errors)}")
    print(f"Неудач: {len(result.failures)}")
    print("="*50)
