if __name__ == "__main__":
    n = int(input())
    x =sum([int(x) for x in input().split(' ')])
    y = n*(n+1) // 2
    result = y-x
    print(result)
