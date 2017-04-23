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
    for i in range(n):
        l.append(calculateGrundy(i))
    return calculateMex(l)

def main():
    print(calculateGrundy(10))

if __name__ == '__main__':
    main()
