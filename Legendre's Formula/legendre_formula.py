def computePower(n,p):
    x = 0
    while n:
        n //= p
        x += n
    return x

def main():
    n,p = map(int,input().split(" "))
    ans = computePower(n,p)
    print(ans)

if __name__ == '__main__':
    main()
