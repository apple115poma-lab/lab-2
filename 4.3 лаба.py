import random


def quick_sort(matrix):
    if len(matrix) <= 1:
        return matrix

    pivot = matrix[len(matrix) // 2][0]

    left = []
    middle = []
    right = []

    for row in matrix:

        if row[0] < pivot:
            left.append(row)

        elif row[0] == pivot:
            middle.append(row)

        else:
            right.append(row)

    return quick_sort(left) + middle + quick_sort(right)


matrix = []

for i in range(5):
    row = []

    for j in range(3):
        row.append(random.randint(5, 61))

    matrix.append(row)


print("До сортировки:")
for row in matrix:
    print(row)


matrix = quick_sort(matrix)


print("После сортировки:")
for row in matrix:
    print(row)