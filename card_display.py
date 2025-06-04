from classes.classes import Card

def display_cards(cards):
        if not cards:
            print("N/A", end="")
        elif isinstance(cards, Card):
            display_card(cards)
        else:
            for card in cards:
                display_card(card)

def display_card(card):
        if not card:
            print("N/A")
        else:
            print(card.rank, "of", card.suit, end=" ")
