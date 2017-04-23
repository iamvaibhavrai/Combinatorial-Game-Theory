def findWinner(a,player):
    xor = a[0]
    for i in range(1,len(a)):
        xor ^= a[i]
    if xor == 0:
        if player == 1:
            return 2
        else:
            return 1
    else:
        if player == 1:
            return 1
        else:
            return 2

def main():
    while True:
        print("")
        print("1 - Play")
        print("0 - End")
        option = int(input())
        if option == 1:
            print("Enter number of tiles on each pile:")
            a = list(map(int,input().split(" ")))
            print("Who starts first?")
            print("1-Player 1")
            print("2-Player 2")
            player = int(input())
            winner = findWinner(a,player)
            print("Player %s wins" %(winner))
        else:
            return True

if __name__ == '__main__':
    main()
