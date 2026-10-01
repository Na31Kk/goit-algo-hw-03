import random

def get_numbers_ticket(min, max, quantity):
    # Функція для генерації унікальних чисел для лотерейного квитка в заданому діапазоні
    # При коректних праметрах функція повертає відсортований список унікальних чисел, 
    # інакше повертає пустий список"""
    winning_numbers = []
    if 0 < min < max and max <= 1000 and 0 < quantity <= (max - min + 1):
        winning_numbers = sorted(random.sample(range(min, max +1), quantity))
    return winning_numbers

print(get_numbers_ticket(1, 49, 6))