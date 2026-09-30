import shuffle_methods as shuffle
import magic_21
import deck

def main():
    print("Welcome to Card Shuffle App")

    # שלב 1 - יצירת חפיסה
    order_deck = deck.create_random_deck()
    print(order_deck)

    #  שלב 2 - בחירת שיטת ערבוב
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
            shuffled_deck = shuffle.riffle(order_deck)
        case "2":
            shuffled_deck = shuffle.mongean(order_deck)
        case "3":
            shuffled_deck = shuffle.mexican_spiral(order_deck)
        case "4":
            shuffled_deck = shuffle.cut_deck(order_deck)
        case _:
            print("Invalid choice!")
            print("The deck remained as it was.")
            shuffled_deck = order_deck

    # שלב 3 - הצגת התוצאה
    print(shuffled_deck)

    # magic_21.twenty_one_magic(new_deck)

if __name__ =="__main__":
    main()