from classes.classes import Card, Deck
from calculations import univ_hypergeometric, multiv_hypergeometric


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
    
    # Calculate univariate hypergeometric PEF for drawing a card of the same rank
    probability = univ_hypergeometric(
        N = deck.length, 
        K = len(deck.ranks[card.rank]),
        n = draw_limit,
        k = 2)
    
    output["probability"] = probability
    output["valid_cards"] = [deck.ranks[card.rank]]

    return output


def calculate_two_pair_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    # Establish the rank of the card
    r1 = card.rank

    # Check if we can even draw a pair (if there's at least one card remaining)
    if r1 not in deck.ranks:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    pair_compliment = len(deck.ranks[r1])
    if pair_compliment < 1:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output

    total_prob = 0.0
    highest_complimenting_rank = 0

    # Iterate over all ranks EXCEPT r1 (in order to get two pairs and avoid a four of a kind)
    for r2, r2_cards in deck.ranks.items():
        if r2 == r1:
            # It's the same rank, skippity scrappity don't give me that crappity
            continue

        # Check whether we can draw a whole new pair to our hand
        new_pair_candidate = len(r2_cards)
        if new_pair_candidate < 2:
            # Bro can't even comprise a pair 💀
            continue

        successes = [pair_compliment, new_pair_candidate]   # We want to get a card of the same rank, and the cards of the currently analysed rank
        success_amounts = [1, 2]                            # We want 1 of the first one, 2 of the second one

        # Calculate multivariate hypergeometric PEF for drawing cards that satisfy these criteria
        p = multiv_hypergeometric(
            N=deck.length, 
            K_x=successes, 
            n=draw_limit, 
            k_x=success_amounts)
        
        total_prob += p

        # Select this rank as the highest complimenting rank if it is bigger than what we've seen, and we are still in the loop
        if r2 > highest_complimenting_rank:
            highest_complimenting_rank = r2


    output["probability"] = total_prob
    output["valid_cards"] = deck.ranks[highest_complimenting_rank]
    return output

def calculate_three_of_a_kind_probability(deck: Deck, card: Card, draw_limit: int):
    output = {}

    if card.rank not in deck.ranks or len(deck.ranks[card.rank]) < 2 or draw_limit < 2:
        output["probability"] = 0.0
        output["valid_cards"] = []
        return output
    
    # Calculate univariate hypergeometric PEF for drawing two cards of the same rank
    probability = univ_hypergeometric(
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
    
    # Calculate univariate hypergeometric PEF for drawing three cards of the same rank
    probability = univ_hypergeometric(
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
    
    # Calculate univariate hypergeometric PEF for drawing four cards of the same suit
    probability = univ_hypergeometric(
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
    
    # Calculate hypergeometric PEF for drawing four cards of the same rank
    probability = univ_hypergeometric(
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