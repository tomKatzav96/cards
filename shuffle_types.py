import random
from collections import deque

def riffle(deck):
    """
    This shuffle splits the deck near the middle and then interleaves the two halves.
    It randomly chooses which half goes first, then alternates taking 1-3 cards from each half 
    until all cards are in the new shuffled deck.
    """
    middle = len(deck) // 2
    cut_index = random.randint(middle - 3, middle + 3)
    left_half = deck[:cut_index]
    right_half = deck[cut_index:]
    shuffled_deck = []
    start_half = random.choice(['L', 'R'])
    while left_half or right_half:
        if start_half == 'L':
            num_of_cards = random.randint(1, 3)
            shuffled_deck += left_half[:num_of_cards]
            left_half = left_half[num_of_cards:]  
        num_of_cards = random.randint(1, 3)
        shuffled_deck += right_half[:num_of_cards]
        right_half = right_half[num_of_cards:]
        start_half = 'L'
    return shuffled_deck

def overhand(deck):
    '''
    this shuffle cards like regular?
    '''
    pass


def mongean(deck):
    '''
    This shuffle take 2-6 cards from the top and move to new deck.
    one time put the cards to top, second time on bottom and so.
    '''
    shuffled_deck = []
    add_to_start = False
    while deck:
        num_of_cards = random.randint(2, 6)
        chunk = deck[:num_of_cards]
        deck = deck[num_of_cards:]
        if add_to_start:
            shuffled_deck = chunk + shuffled_deck
        else:
            shuffled_deck = shuffled_deck + chunk
        add_to_start = not add_to_start
    return shuffled_deck

def mexican_spiral(deck):
    """
    Take the top card and place it on the table.
    Then move the next top card to the bottom of the deck.
    Repeat until no cards remain.
    """
    deck = deque(deck)
    table_deck = deque()
    while deck:
        table_deck.appendleft(deck.popleft())
        if deck:
            deck.append(deck.popleft())
    return list(table_deck)

def cut_deck(deck):
    """
    Cut the deck at a random position and move the top portion to the bottom.
    """
    deck = deque(deck)
    cut_index = random.randint(1, len(deck) - 1)
    deck.rotate(-cut_index)
    return list(deck)

