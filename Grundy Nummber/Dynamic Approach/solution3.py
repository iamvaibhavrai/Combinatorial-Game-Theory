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
    l.append(calculateGrundy(n//2,grundy))
    l.append(calculateGrundy(n//3,grundy))
    l.append(calculateGrundy(n//6,grundy))
    grundy[n] = calculateMex(l)
    return grundy[n]


def main():
    print("Enter Number: ")
    n = int(input())
    grundy = [-1]*(n+1)
    print(calculateGrundy(n,grundy))

if __name__ == '__main__':
    main()
