x,y = 0,0
def findGcdAndFactors(a,b,m,n,arr):
    global x,y
    if a == 0:
        m = 0
        n = 1
        arr.append(m)
        arr.append(n)
        arr.append(b)
        return arr
    m,n,b = arr[0],arr[1],arr[2]
    arr = []
    gcd = findGcdAndFactors(b%a,b,m,n,arr)
    x = gcd[1] - (gcd[2]//a)*gcd[0]
    y = gcd[0]
    return gcd

def main():
    global x,y
    print("Enter two number seperated by space.")
    a,b = map(int,input().split(" "))
    gcd = [x,y,b]
    gcd = findGcdAndFactors(a,b,x,y,gcd)
    print(gcd[2],gcd[0],gcd[1])

if __name__ == '__main__':
    main()
