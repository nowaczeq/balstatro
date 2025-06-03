from classes import Card, Deck

def calculate_pair_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    # Return if there is no match in the deck
    if card.rank not in deck.ranks:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output

    # See how many two-card combinations there are for each card in hand (all cards in deck)
    all_observations = deck.length
    valid_observations = len(deck.ranks[card.rank])

    if valid_observations == 0 or draw_limit == 0 or all_observations == 0:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Establish the minimum amount of cards we can draw for the card
    draws = min(draw_limit, all_observations)
    prob_no_match = 1.0

    # Calculate the probability that we DON'T draw a pair
    for i in range(draws):
        if all_observations - i <= 0:
            break
            
        prob_no_match *= (all_observations - valid_observations - i) / (all_observations - i)
    
    output["probability"] = 1 - prob_no_match

    valid_cards = deck.ranks[card.rank].copy()
    output["valid_cards"] = valid_cards
    return output

def calculate_two_pair_probability(deck: Deck, card: Card):
    return