from classes import Card, Deck

def calculate_pair_probability(deck: Deck, card: Card) -> float:
    # See how many two-card combinations there are for each card in hand (all cards in deck)
    all_observations = deck.length
    valid_observations = len(deck.ranks[card.rank])
    return valid_observations / all_observations

