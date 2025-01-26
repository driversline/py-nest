import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''.join([
        string.ascii_uppercase if use_uppercase else '',
        string.ascii_lowercase if use_lowercase else '',
        string.digits if use_digits else '',
        string.punctuation if use_special else ''
    ])
    
    if not characters:
        raise ValueError("Выберите хотя бы один тип символов.")

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Введите длину пароля: "))
    use_uppercase = input("Использовать заглавные буквы? (y/n): ") == 'y'
    use_lowercase = input("Использовать строчные буквы? (y/n): ") == 'y'
    use_digits = input("Использовать цифры? (y/n): ") == 'y'
    use_special = input("Использовать специальные символы? (y/n): ") == 'y'

    while True:
        try:
            print(f"Сгенерированный пароль: {generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)}")
        except ValueError as e:
            print(e)
            break
        input("Нажмите Enter, чтобы сгенерировать новый пароль...")
