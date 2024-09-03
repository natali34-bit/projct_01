import random

def computer_guesses_number():
    # Компьютер загадывает число от 1 до 100
    secret_number = random.randint(1, 100)
    print("Компьютер загадал число от 1 до 100.")
    
    # Начальные границы для бинарного поиска
    low = 1
    high = 100
    attempts = 0

    while attempts < 20:  # Ограничиваем количество попыток до 20
        # Программа делает предположение
        guess = (low + high) // 2
        attempts += 1
        print(f"Попытка {attempts}: Программа предполагает, что это число {guess}.")

        # Проверяем, больше, меньше или равно загаданное число
        if guess < secret_number:
            print("Загаданное число больше.")
            low = guess + 1  # Увеличиваем нижнюю границу
        elif guess > secret_number:
            print("Загаданное число меньше.")
            high = guess - 1  # Уменьшаем верхнюю границу
        else:
            print(f"Программа угадала число {secret_number} за {attempts} попыток!")
            return  # Завершаем функцию, если число угадано

    print("Программа не смогла угадать число за 20 попыток.")

# Запускаем игру
computer_guesses_number()
