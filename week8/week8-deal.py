import os
import random

symbols = ['♠', '♦', '♥', '♣']
num = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

while 1:
    deck = [i for i in range(52)]
    player = [[], [], [], []]
    for i in range(52):
        seq = random.randint(0, len(deck) - 1)
        player[i % 4].append(deck[seq])
        deck.pop(seq)

    for i in range(13):
        for j in range(4):
            card = player[j][i]
            print('%s%s\t' % (symbols[card // 13], num[card % 13]), end = '')
        print('')
    print('------------------')
    input()
