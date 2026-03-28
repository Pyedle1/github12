 #1. Функция валидации email (email_validator.py)
import re

def validate_email(email):
    
    Проверяет корректность формата email-адреса.
    
    Args:
        email (str): Email адрес для проверки
        
    Returns:
        bool: True если email валиден, False в противном случае
   
    
    if not email or not isinstance(email, str):
        return False
    
   
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
   
    if len(email) > 254:
        return False
    
    
    if '@' in email:
        local_part = email.split('@')[0]
        if len(local_part) > 64:
            return False
    
    
    if email.startswith('.') or email.endswith('.'):
        return False
    
    if '..' in email:
        return False
    
    
    return bool(re.match(pattern, email))

