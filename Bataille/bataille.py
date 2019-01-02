#!/usr/bin/env python3

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cards_p1 = []
cards_p2 = []
defausse_p1 = []
defausse_p2 = []
nb_turn = 0
nb_turn_display = 0

def read_input():
    n = int(input())  # the number of cards for player 1
    for i in range(n):
        cardp_1 = input()  # the n cards of player 1
        cards_p1.append(cardp_1)
    m = int(input())  # the number of cards for player 2
    for i in range(m):
        cardp_2 = input()  # the m cards of player 2
        cards_p2.append(cardp_2)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

def display():
    if (nb_turn == nb_turn_display) or (nb_turn == nb_turn_display + 1):
        print(cards_p1)
        print(cards_p2)
    if len(defausse_p1) > 0:
        print("Defausse p1", defausse_p1)
    if len(defausse_p2) > 0:
        print("Defausse p2", defausse_p2)

def get_value(card):
    if len(card) == 3:
        return 10
    if card[0].isdigit():
        return int(card[0])
    if card[0] == "1" and card[1] == "0":
        return 10
    elif card[0] == "J":
        return 11
    elif card[0] == "Q":
        return 12
    elif card[0] == "K":
        return 13
    elif card[0] == "A":
        return 14
    else:
        print("Syntax Error")

def one_run():
    global defausse_p1
    global defausse_p2
    global cards_p1
    global cards_p2
    global nb_turn
    global nb_turn_display

    card_p1 = cards_p1[0]
    card_p2 = cards_p2[0]

    card_p1_value = get_value(card_p1)
    card_p2_value = get_value(card_p2)

    if card_p1_value > card_p2_value:
        cards_p1.pop(0)
        cards_p2.pop(0)
        for card in defausse_p1:
            cards_p1.append(card)
        defausse_p1 = []
        cards_p1.append(card_p1)
        for card in defausse_p2:
            cards_p1.append(card)
        defausse_p2 = []
        cards_p1.append(card_p2)

    elif card_p1_value < card_p2_value:
        cards_p1.pop(0)
        cards_p2.pop(0)
        for card in defausse_p1:
            cards_p2.append(card)
        defausse_p1 = []
        cards_p2.append(card_p1)

        for card in defausse_p2:
            cards_p2.append(card)
        defausse_p2 = []
        cards_p2.append(card_p2)
    else:
        if len(cards_p1) < 5:
            print("PAT")
            sys.exit()
        if len(cards_p2) < 5:
            print("PAT")
            sys.exit()
        else:
            for i in range(0, 4):
                defausse_p1.append(cards_p1[0])
                defausse_p2.append(cards_p2[0])
                cards_p1.pop(0)
                cards_p2.pop(0)
            print("Before calling nested one_run")
            display()
            one_run()

def main():
    finished = False

    read_input()

    while finished != True:
        nb_turn += 1
        print(nb_turn, file=sys.stderr)
        one_run()

        if len(cards_p1) == 0:
            print("2", nb_turn)
            finished = True

        if len(cards_p2) == 0:
            print("1", nb_turn)
            finished = True

if __name__ == '__main__':
    main()