from classes.classes import Card, Deck
from calculations import hypergeometric, multiv_hypergeometric


# FUNCTIONS TO CALCULATE THE PROBABILITY FOR
##########     SINGLE CARDS     #########

# inputs:
#   deck: full deck of cards
#   card: card for which we are calculating the probability
#   draw_limit: the amount of cards we can draw in a round

# returns output = {
#                   "probability": float indicating probability of finding matching cards,
#                   "valid_cards": array of Card() indicating cards that can be drawn to match
#                   }

# DONE:
# HIGHCARD: DONE
# PAIR: DONE
# TWOPAIR: TODO
# THREE_OF_A_KIND: DONE
# FOUR_OF_A_KIND: DONE
# FLUSH: DONE
# FIVE_OF_A_KIND: DONE

def calculate_high_card_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 1.0
    output["valid_cards"] = card
    return output

def calculate_pair_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.ranks[card.rank]) == 1 or draw_limit < 1:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate hypergeometric PEF for drawing three cards
    probability = hypergeometric(
        N = deck.length, 
        K = len(deck.ranks[card.rank]),
        n = draw_limit,
        k = 2)
    
    output["probability"] = probability
    output["valid_cards"] = [deck.ranks[card.rank]]

    return output


def calculate_two_pair_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    
    output["probability"] = 0.0
    output["valid_cards"] = []
    return output

def calculate_three_of_a_kind_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.ranks[card.rank]) < 2 or draw_limit < 2:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate hypergeometric PEF for drawing three cards
    probability = hypergeometric(
        N = deck.length, 
        K = len(deck.ranks[card.rank]),
        n = draw_limit,
        k = 2)
    
    output["probability"] = probability
    output["valid_cards"] = deck.ranks[card.rank]
    return output


def calculate_four_of_a_kind_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.ranks[card.rank]) < 3 or draw_limit < 3:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate hypergeometric PEF for drawing three cards
    probability = hypergeometric(
        N = deck.length, 
        K = len(deck.ranks[card.rank]),
        n = draw_limit,
        k = 3)
    
    output["probability"] = probability
    output["valid_cards"] = deck.ranks[card.rank]
    return output


def calculate_flush_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.suits[card.suit]) < 4 or draw_limit < 4:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate hypergeometric PEF for drawing three cards
    probability = hypergeometric(
        N = deck.length, 
        K = len(deck.suits[card.suit]),
        n = draw_limit,
        k = 4)
    
    output["probability"] = probability
    output["valid_cards"] = deck.ranks[card.rank]
    return output

def calculate_full_house_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 0
    output["valid_cards"] = []
    return output


def calculate_straight_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 0
    output["valid_cards"] = []
    return output


def calculate_straight_flush_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 0
    output["valid_cards"] = []
    return output


def calculate_five_of_a_kind_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.ranks[card.rank]) < 4 or draw_limit < 4:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate hypergeometric PEF for drawing three cards
    probability = hypergeometric(
        N = deck.length, 
        K = len(deck.ranks[card.rank]),
        n = draw_limit,
        k = 4)
    
    output["probability"] = probability
    output["valid_cards"] = deck.ranks[card.rank]
    return output

def calculate_flush_five_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 0
    output["valid_cards"] = []
    return output


def calculate_flush_house_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}
    output["probability"] = 0
    output["valid_cards"] = []
    return output