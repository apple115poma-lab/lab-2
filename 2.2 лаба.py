import random

numbers = []

for i in range(10):
    number = random.randint(0, 100)
    numbers.append(number)

print("До сортировки:", numbers)

for i in range(len(numbers)):
    max_index = i

    for j in range(i + 1, len(numbers)):
        if numbers[j] > numbers[max_index]:
            max_index = j

    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

print("После сортировки:", numbers)