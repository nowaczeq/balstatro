import handtests

def check_pair_probability(hand, deck):
    probabilities = {}
    for held_card in hand:
        compatible_cards = []
        # For each card in the deck, pretend the card is in the hand and calculate whether it creates a pair
        for deck_card in deck:
            if handtests.check_pair([held_card, deck_card]):
                compatible_cards.append(deck_card)
        probabilities[held_card] = compatible_cards
    
    return probabilities
