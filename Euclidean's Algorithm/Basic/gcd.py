def findGCD(a,b):
    if a == 0:
        return b
    return findGCD(b%a,b)

def main():
    print("Enter two number seperated by space.")
    a,b = map(int,input().split(" "))
    gcd = findGCD(a,b)
    print(gcd)

if __name__ == '__main__':
    main()
