import random

def current_total(hand):
    """ Sums the cards in hand.  Aces count as 1 or 11.  Will optimize for 
    highest total without going over 21.
    """
    total, aces = 0, 0
    for card in hand:
        if card.isdigit():
            total += int(card)
        elif card in 'JQK':
            total += 10
        elif card == 'A':
            aces += 1
            total += 11
    for i in range(aces):
        if total > 21:
            total -= 10
    return total


    
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)
player_hand = []
computer_hand = []
for i in range(2):
    player_hand.append(deck.pop())
    computer_hand.append(deck.pop())

# Use the function, current_total, and the variables defined above to
# finish this implementation of one "hand" of blackjack

# 1. continually ask whether or not the player wants to it or stand
# 2. once the player is done drawing cards (or if they go over 21)...
#    continually remove cards from the deck and add them to the computer's
#    hand until the computer's hand total is over 17
# 3. the player that's closest to 21 without going over wins

player_total = current_total(player_hand)
computer_total = current_total(computer_hand)
action = input("(h)it or (s)tand?\n>")

while action == "h":
    print("\n(Player draws another card)")
    player_hand.append(deck.pop())
    player_total = current_total(player_hand)
    print("\nPlayer Hand: ", player_hand, player_total)
    if player_total > 21:
        print("BUST!\n")
        while computer_total <= 17:
            computer_hand.append(deck.pop())
            computer_total = current_total(computer_hand)
        print("Computer Hand: ", computer_hand, computer_total)
        break
    else:
        action = input("\n(h)it or (s)tand?\n>")

if action == "s":
    player_total = current_total(player_hand)
    print("\n(Player stands)")
    print("\nPlayer Hand: ", player_hand, player_total)
    while computer_total <= 17:
        computer_hand.append(deck.pop())
        computer_total = current_total(computer_hand)
    print("\nComputer Hand: ", computer_hand, computer_total)

if (21 - player_total) < (21 - computer_total) and (21 - player_total) >= 0:
    print("\nPlayer wins")
elif (21 - player_total) < (21 - computer_total) and (21 - player_total) < 0 and (21 - computer_total) >= 0:
    print("\nComputer wins")
elif (21 - player_total) > (21 - computer_total) and (21 - computer_total) >= 0:
    print("\nComputer wins")
elif (21 - player_total) > (21 - computer_total) and (21 - computer_total) < 0 and (21 - player_total) >= 0:
    print("\nPlayer wins")
elif (21 - player_total < 0) and (21 - computer_total < 0):
    print("\nTie")
elif player_total == computer_total:
    print("\nTie")
