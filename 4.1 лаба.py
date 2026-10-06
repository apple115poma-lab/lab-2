import random


def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    left = []
    middle = []
    right = []

    for number in numbers:
        if number < pivot:
            left.append(number)
        elif number == pivot:
            middle.append(number)
        else:
            right.append(number)

    return quick_sort(left) + middle + quick_sort(right)


numbers = []

for i in range(1000):
    numbers.append(random.randint(1, 1000))

print("До сортировки:")
print(numbers)

numbers = quick_sort(numbers)

print("После сортировки:")
print(numbers)