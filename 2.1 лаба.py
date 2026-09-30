import random

numbers = []

# Создаём список из 10 случайных чисел
for i in range(10):
    number = random.randint(2, 103)
    numbers.append(number)

print("До сортировки:", numbers)

# Перебираем места в списке слева направо
for i in range(len(numbers)):
    min_index = i

    # Ищем самое маленькое число в оставшейся части списка
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Ставим найденное число на место i
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("После сортировки:", numbers)