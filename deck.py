import random

def create_order_deck():
    """create a 52 cards deck"""
    suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    order_deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    return order_deck

def create_random_deck():
    """create a 52 cards deck"""
    suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck