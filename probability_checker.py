from itertools import combinations
from handtests import check_pair
from calculate_probability import calculate_pair_probability
from classes import Deck
import time

# Check how many cards in the deck would make a pair
def check_hands_pair_probability(hand, deck: Deck, draw_limit: int):
    probabilities = {}
    counter = 1
    start_time = time.perf_counter()

    for hand_card in hand:
        # Check if a pair already exists in the hand for the card
        for candidate_card in hand:
            if hand_card != candidate_card and candidate_card.rank == hand_card.rank:
                probabilities[hand_card] = {}
                probabilities[hand_card]["probability"] = 1
                probabilities[hand_card]["valid_cards"] = candidate_card
                continue

        print(f"Initiating analysis for {hand_card.rank} of {hand_card.suit} ")
        data = calculate_pair_probability(deck, hand_card, draw_limit)
        probabilities[hand_card] = data
        local_time = time.perf_counter()
        print(f"Analysis for {hand_card.rank} of {hand_card.suit} took {local_time - start_time}.")
    
    print(f"Analysis finished. Time elapsed: {time.perf_counter() - start_time}")
    return probabilities


def test():
    return

if __name__ == "__main__":
    test()