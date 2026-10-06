def namba(a, b):
    print(a)
    if a == b:
        return
    if a < b:
        return namba(a + 1, b)
    if a > b:
        return namba(a - 1, b)

a = int(input())
b = int(input())
namba(a, b)