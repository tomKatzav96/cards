import time
from collections import Counter

def take_twenty_one(deck):
    twenty_one_cerds_deck = deck[:21]
    return twenty_one_cerds_deck

def liar_detact(card, piles):
    print(piles)
    counts = Counter(piles)
    if counts[card] == 3:
        return True
    else:
        return False

def magic_action(deck, i):
    pile_a = deck[::3]
    pile_b = deck[1::3]
    pile_c = deck[2::3]
    print("Pile A" , pile_a)
    print("Pile B" , pile_b)
    print("Pile C" , pile_c)

    if i == 0:
        choice = input(
            "Coose a card.\n"
            "Which pile is your card in?\n"
            "A\n"
            "B\n"
            "C\n"
            "Enter your choice: "
        )
    else:
        choice = input(
            "Which pile is your card in?\n"
            "A\n"
            "B\n"
            "C\n"
            "Enter your choice: "
        )
    match choice:
        case "A":
            first_pile = pile_b
            midlle_pile = pile_a
            finel_pile = pile_c
        case "B":
            first_pile = pile_a
            midlle_pile = pile_b
            finel_pile = pile_c
        case "C":
            first_pile = pile_a
            midlle_pile = pile_c
            finel_pile = pile_b
        case _:
            print("You ruined the magic.")
    new_list = first_pile + midlle_pile + finel_pile
    return new_list , midlle_pile

def twenty_one_magic(deck):
    print("For this magick we need only 21 cards")
    twenty_one_cerds_deck = take_twenty_one(deck)
    user_piles = []

    for i in range(3):
        twenty_one_cerds_deck, chosen_pile = magic_action(twenty_one_cerds_deck, i )
        user_piles.extend(chosen_pile)
    if liar_detact(twenty_one_cerds_deck[10], user_piles):
        print("Your card is...")
        time.sleep(3) 
        print(twenty_one_cerds_deck[10])
    else:
        print("You are liar")