from datetime import datetime


def get_days_from_today(date):
    # Функція для обчислення кількості днів між вказаною датою і сьогодіншьою
    # Функція повертає кількість днів між датами, якщо дані введено коректно
    try:
        user_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        days_diffference = (today - user_date).days
        return days_diffference
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

print(get_days_from_today("2023-01-01")) 