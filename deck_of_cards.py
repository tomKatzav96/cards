import shuffle_types as shuffle
import magic_21

def create_Deck():
    """create a 52 cards deck"""
    suits = ["\u2663", "\u2666", "\u2665", "\u2660"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    order_deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    return order_deck

order_deck = create_Deck()
print(order_deck)

choice = input(
    "Choose shuffle type:\n"
    "1 - Riffle\n"
    "2 - Mongean\n"
    "3 - Mexican Spiral\n"
    "4 - Cut the deck\n"
    "Enter your choice: "
)

match choice:
    case "1":
        new_deck = shuffle.riffle(order_deck)
    case "2":
        new_deck = shuffle.mongean(order_deck)
    case "3":
        new_deck = shuffle.mexican_spiral(order_deck)
    case "4":
        new_deck = shuffle.cut_deck(order_deck)
    case _:
        print("Invalid choice!")
        print("The deck remained as it was.")
        new_deck = order_deck

magic_21.twenty_one_magic(new_deck)

