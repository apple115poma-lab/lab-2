def deliteli(n, d=2):
    if n == 1:
        return

    if n % d == 0:
        print(d)
        deliteli(n // d, d)
    else:
        deliteli(n, d + 1)


n = int(input())
deliteli(n)
