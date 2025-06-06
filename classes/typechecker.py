from classes.classes import Card, Deck
import probability_functions.calculate_probability as cp
import score_functions.handtests as ht

# Class to allow for checking the score of a hand and the probability of drawing to a hand type from deck

class TypeChecker:
    def __init__(self):
        self.score_checkers = {
            "high_card": ht.check_high_card,
            "pair": ht.check_pair,
            "two_pair": ht.check_two_pair,
            "three_of_a_kind": ht.check_three_of_a_kind,
            "four_of_a_kind": ht.check_four_of_a_kind,
            "flush": ht.check_flush,
            "full_house": ht.check_full_house,
            "straight": ht.check_straight,
            "straight_flush": ht.check_straight_flush,
            "five_of_a_kind": ht.check_five_of_a_kind,
            "flush_five": ht.check_flush_five,
            "flush_house": ht.check_flush_house
        }

        self.probability_checkers = {
            "high_card": cp.calculate_high_card_probability,
            "pair": cp.calculate_pair_probability,
            "two_pair": cp.calculate_two_pair_probability,
            "three_of_a_kind": cp.calculate_three_of_a_kind_probability,
            "four_of_a_kind": cp.calculate_four_of_a_kind_probability,
            "flush": cp.calculate_flush_probability,
            "full_house": cp.calculate_full_house_probability,
            "straight": cp.calculate_straight_probability,
            "straight_flush": cp.calculate_straight_flush_probability,
            "five_of_a_kind": cp.calculate_five_of_a_kind_probability,
            "flush_five": cp.calculate_flush_five_probability,
            "flush_house": cp.calculate_flush_house_probability
        }
    
    def check_score(self, hand, hand_type):
        checker = self.score_checkers.get(hand_type.lower())
        if checker:
            return checker(hand)
        else:
            raise ValueError(f"Unknown hand type: {hand_type}")
        
    def check_probability(self, deck: Deck, card: Card, draw_limit: int, hand_type: str):
        checker = self.probability_checkers.get(hand_type.lower())
        if checker:
            return checker(deck, card, draw_limit)
        else:
            raise ValueError(f"Unknown hand type: {hand_type}")
