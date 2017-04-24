import math

def eulerTotient(n):
    res = n
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            while n%i  == 0:
                n /= i
            res = res*(1 - 1/i)
    if n > 1:
        res = res*(1 - 1/n)
    return res

def main():
    n = int(input())
    res = eulerTotient(n)
    print(int(res))

if __name__ == '__main__':
    main()
