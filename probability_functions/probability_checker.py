from probability_functions.calculate_probability import calculate_pair_probability
from classes.classes import Deck
import time


# FUNCTIONS TO CALCULATE THE PROBABILITY FOR
##########     HANDS [arrays of Cards]     #########

# Check how many cards in the deck would make a pair
def check_hands_pair_probability(hand, deck: Deck, draw_limit: int):
    probabilities = {}
    start_time = time.perf_counter()

    for hand_card in hand:
        # TODO: Rework this hackish solution cause what the hell is that man
        pair_in_hand = False
        # Check if a pair already exists in the hand for the card
        for candidate_card in hand:
            if hand_card != candidate_card and candidate_card.rank == hand_card.rank:
                pair_in_hand = True
                probabilities[hand_card] = {}
                probabilities[hand_card]["probability"] = 1
                probabilities[hand_card]["valid_cards"] = [candidate_card]
                break
        
        if not pair_in_hand:
            print(f"Initiating analysis for {hand_card.rank} of {hand_card.suit} ")
            data = calculate_pair_probability(deck, hand_card, draw_limit)
            probabilities[hand_card] = data
            local_time = time.perf_counter()
            print(f"Analysis for {hand_card.rank} of {hand_card.suit} took {local_time - start_time}.")
    
    print(f"Analysis finished. Time elapsed: {time.perf_counter() - start_time}")
    return probabilities
