from random import randint

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

symbols = ['♣', '♦', '♥', '♠']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

while 1:
    deck = [i for i in range(52)]
    players = [[],[],[],[]]
    
    for i in range(13):
        for j in range(4):
            index = randint(0, len(deck) - 1)
            card = deck[index]
            players[j].append(card)
            deck.pop(index)
    # ----- Add some code to sort -----
    # example:
    #    ♣ 2 < ♠ 5 < ♣ 10 < ♥ 10 < ♦ 11
    
    # ---------------------------------
    for index, p in enumerate(players):
        players[index] = bubbleSort(p)

    for i in range(13):
        for j in range(4):
            card = players[j][i]
            print('%s %s\t' % (symbols[card // 13], num[card % 13]), end = '')
        print('')
    input()
