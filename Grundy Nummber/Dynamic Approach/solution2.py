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
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    if grundy[n] != -1:
        return grundy[n]
    l = []
    for i in range(1,4):
        l.append(calculateGrundy(n-i,grundy))
    grundy[n] = calculateMex(l)
    return grundy[n]


def main():
    print("Enter Number: ")
    n = int(input())
    grundy = [-1]*(n+1)
    print(calculateGrundy(n,grundy))

if __name__ == '__main__':
    main()
