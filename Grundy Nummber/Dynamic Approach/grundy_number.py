def calculateMex(l):
    mex = 0
    while True:
        if mex in l:
            mex += 1
        else:
            return mex

def calculateGrundy(n,grundy):
    if n == 0:
        return 0
    if grundy[n] != -1:
        return grundy[n]
    l = []
    for i in range(n):
        l.append(calculateGrundy(i,grundy))
    grundy[n] = calculateMex(l)
    return grundy[n]


def main():
    pass

if __name__ == '__main__':
    print("Enter Number: ")
    n = int(input())
    grundy = [-1]*(n+1)
    print(calculateGrundy(n,grundy))
    main()
