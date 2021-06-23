if __name__ == "__main__":
    n = int(input())
    x = set(map(int,input().split(' ')))
    y = set()
    z = set()
    for i in range(1, n+1):
        y.add(i)
        z = y.difference_update(x)
    print(*y)
