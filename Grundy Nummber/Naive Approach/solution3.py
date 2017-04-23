def calculateMex(l):
    mex = 0
    while True:
        if mex in l:
            mex += 1
        else:
            return mex

def calculateGrundy(n):
    if n == 0:
        return 0

    l = []
    l.append(calculateGrundy(n//2))
    l.append(calculateGrundy(n//3))
    l.append(calculateGrundy(n//6))
    return calculateMex(l)

def main():
    print(calculateGrundy(7))

if __name__ == '__main__':
    main()
