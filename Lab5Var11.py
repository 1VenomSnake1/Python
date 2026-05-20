import re


class InvalidEmailError(Exception):
    """Исключение, возникающее при некорректном адресе электронной почты."""

    def __init__(self, email: str, message: str = "Некорректный адрес электронной почты"):
        self.email = email
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.email}"


def is_valid_email(email: str) -> bool:
    """
    Проверяет, является ли строка корректным адресом электронной почты.
    Возвращает True, если адрес валиден, иначе False.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_email(email: str) -> str:
    """
    Проверяет адрес электронной почты.
    Если адрес корректен, возвращает его.
    В противном случае выбрасывает исключение InvalidEmailError.
    """
    if not is_valid_email(email):
        raise InvalidEmailError(email)
    return email


if __name__ == "__main__":
    f = str(input())
    while (f != ""):
        print(f"'{f}' валиден? {is_valid_email(f)}")

        print("\nПроверка с выбросом исключения")
        try:
            validated = validate_email(f)
            print(f"Успешно: {validated}")
        except InvalidEmailError as e:
            print(f"Ошибка: {e}")
        f = str(input())



''''''
'user@example.com'
'invalid-email'
'user@domain'
'user@.com'
'@domain.com'
'user@domain.c'
'user.name+tag@sub.domain.co'
''''''