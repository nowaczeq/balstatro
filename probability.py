from itertools import combinations
from handtests import check_pair
import time

def check_pair_probability(hand, deck, draw_limit):
    probabilities = {}
    counter = 0
    start_time = time.perf_counter()

    for hand_card in hand:
        print(f"Initiating analysis for {hand_card.rank} of {hand_card.suit} ")
        valid_draws = 0
        all_draws = 0

        for draw in combinations(deck, draw_limit):
            drawn_hand = [hand_card] + list(draw)
            checker = check_pair(drawn_hand)
            if checker["wins"] and checker["cards"][0].rank == hand_card.rank:
                print("Found valid pair combination")
                valid_draws += 1
            else:
                print("Invalid pair combination")
            all_draws += 1
        
        prob = valid_draws / all_draws if all_draws > 0 else 0
        local_time = time.perf_counter()
        print(f"Analysis for {hand_card.rank} of {hand_card.suit} took {local_time - start_time}.")
        probabilities[hand_card] = prob
    
    print(f"Analysis finished. Time elapsed: {time.perf_counter() - start_time}")
    return probabilities


def test():
    return

if __name__ == "__main__":
    test()