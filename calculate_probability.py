from classes import Card, Deck

def calculate_pair_probability(deck: Deck, card: Card):
    output = {}
    # See how many two-card combinations there are for each card in hand (all cards in deck)
    all_observations = deck.length
    valid_observations = len(deck.ranks[card.rank])
    valid_cards = deck.ranks[card.rank]
    output["probability"] = valid_observations / all_observations
    output["valid_cards"] = valid_cards
    return output