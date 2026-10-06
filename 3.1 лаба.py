def namba(n):
    if n == 0:
        return
    namba(n-1)
    print(n)

n = int(input())
namba(n)