import re


def check_form(email, password):
    # Регулярные выражения для проверки
    pattern_for_email = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$')
    pattern_for_password = re.compile(
        r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$')

    # Проверка email
    email_valid = pattern_for_email.match(email) is not None
    # Проверка пароля
    password_valid = pattern_for_password.match(password) is not None

    # Формируем результаты
    results = []
    if email_valid:
        results.append("Email введен правильно.")
    else:
        results.append("Некорректный email.")

    if password_valid:
        results.append("Пароль введен правильно.")
    else:
        results.append("Некорректный пароль.")

    return "\n".join(results)


# Запрос данных у пользователя
email = input("Введите email: ")
password = input(
    "Введите пароль (минимум 8 символов, одна заглавная буква, одна цифра): ")

# Проверка введенных данных
print(check_form(email, password))
