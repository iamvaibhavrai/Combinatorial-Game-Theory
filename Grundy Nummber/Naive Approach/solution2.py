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
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3

    l = []
    for i in range(1,4):
        l.append(calculateGrundy(n-i))
    return calculateMex(l)

def main():
    print(calculateGrundy(10))

if __name__ == '__main__':
    main()
