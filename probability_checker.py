from itertools import combinations
from handtests import check_pair
from calculate_probability import calculate_pair_probability
from classes import Deck
import time

# Check how many cards in the deck would make a pair
def check_pair_probability(hand, deck: Deck):
    probabilities = {}
    counter = 1
    start_time = time.perf_counter()

    for hand_card in hand:
        print(f"Initiating analysis for {hand_card.rank} of {hand_card.suit} ")
        data = calculate_pair_probability(deck, hand_card)
        probabilities[hand_card] = data
        local_time = time.perf_counter()
        print(f"Analysis for {hand_card.rank} of {hand_card.suit} took {local_time - start_time}.")
    
    print(f"Analysis finished. Time elapsed: {time.perf_counter() - start_time}")
    return probabilities


def test():
    return

if __name__ == "__main__":
    test()