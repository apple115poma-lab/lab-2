phones = ["23-45-67", "12-34-56", "98-76-54", "45-12-30", "11-22-33"]

print("До сортировки:", phones)

for i in range(len(phones)):
    min_index = i

    for j in range(i + 1, len(phones)):
        if phones[j] < phones[min_index]:
            min_index = j

    phones[i], phones[min_index] = phones[min_index], phones[i]

print("После сортировки:", phones)