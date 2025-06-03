from classes.classes import Card, Deck
import probability_functions.calculate_probability as cp
import score_functions.handtests as ht


class TypeChecker:
    def __init__(self):
        self.score_checkers = {
            "high card": ht.check_high_card,
            "pair": ht.check_pair,
            "two pair": ht.check_two_pair,
            "three of a kind": ht.check_three_of_a_kind,
            "four of a kind": ht.check_four_of_a_kind,
            "flush": ht.check_flush,
            "full house": ht.check_full_house,
            "straight": ht.check_straight,
            "straight flush": ht.check_straight_flush,
            "five of a kind": ht.check_five_of_a_kind,
            "flush five": ht.check_flush_five,
            "flush house": ht.check_flush_house
        }

        self.probability_checkers = {
            "high card": cp.calculate_high_card_probability,
            "pair": cp.calculate_pair_probability,
            "two pair": cp.calculate_two_pair_probability,
            "three of a kind": cp.calculate_three_of_a_kind_probability,
            "four of a kind": cp.calculate_four_of_a_kind_probability,
            "flush": cp.calculate_flush_probability,
            "full house": cp.calculate_full_house_probability,
            "straight": cp.calculate_straight_probability,
            "straight flush": cp.calculate_straight_flush_probability,
            "five of a kind": cp.calculate_five_of_a_kind_probability,
            "flush five": cp.calculate_flush_five_probability,
            "flush house": cp.calculate_flush_house_probability
        }
    
    def check_score(self, hand, hand_type):
        checker = self.score_checkers.get(hand_type.lower())
        if checker:
            return checker(hand)
        else:
            raise ValueError(f"Unknown hand type: {hand_type}")
        
    def check_probability(self, card: Card, hand_type: str, deck: Deck, draw_limit: int):
        checker = self.probability_checkers.get(hand_type.lower())
        if checker:
            return checker(deck, card, draw_limit)
        else:
            raise ValueError(f"Unknown hand type: {hand_type}")
