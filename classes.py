import handtests

class Card:
    def __init__(self):
        self.suit = ""
        self.rank = 0
        self.chips = 0

class HandType:
    def __init__(self):
        self.cards = 1
        self.chips = 0
        self.mult = 0

class Deck:
    def __init__(self):
        self.ranks = {}
        self.suits = {}
        self.length = 0
    
    def add_card(self, val: Card) -> bool:
        if val.rank not in self.ranks:
            self.ranks[val.rank] = [val]
        else:
            self.ranks[val.rank].append(val)
        
        if val.suit not in self.suits:
            self.suits[val.suit] = [val]
        else:
            self.suits[val.suit].append(val)
        
        self.length += 1
        return True
    
    def remove_card(self, val: Card) -> bool:
        if not self.ranks.get(val.rank) or not self.suits.get(val.suit):
            return False
        
        self.ranks[val.rank].remove(val)
        self.suits[val.suit].remove(val)
        self.length -= 1
        return True
        

class TypeChecker:
    def __init__(self):
        self.hand_checkers = {
            "high card": handtests.check_high_card,
            "pair": handtests.check_pair,
            "two pair": handtests.check_two_pair,
            "three of a kind": handtests.check_three_of_a_kind,
            "four of a kind": handtests.check_four_of_a_kind,
            "flush": handtests.check_flush,
            "full house": handtests.check_full_house,
            "straight": handtests.check_straight,
            "straight flush": handtests.check_straight_flush,
            "five of a kind": handtests.check_five_of_a_kind,
            "flush five": handtests.check_flush_five,
            "flush house": handtests.check_flush_house
        }
    
    def check(self, hand, hand_type):
        checker = self.hand_checkers.get(hand_type.lower())
        if checker:
            return checker(hand)
        else:
            raise ValueError(f"Unknown hand type: {hand_type}")

class HandTypeTranslator:
    def __init__(self):
        # Add keys for additional translations
        self.hand_dict = {
            "high card": "HIGH_CARD",
            "high_card": "HIGH_CARD",
            "pair": "PAIR",
            "two pair": "TWO_PAIR",
            "three of a kind": "THREE_OF_A_KIND",
            "four of a kind": "FOUR_OF_A_KIND",
            "flush": "FLUSH",
            "full house": "FULL_HOUSE",
            "straight": "STRAIGHT",
            "straight flush": "STRAIGHT_FLUSH",
            "five of a kind": "FIVE_OF_A_KIND",
            "flush five": "FLUSH_FIVE",
            "flush house": "FLUSH_HOUSE"
        }
    
    def translate(self, name):
        if name in self.hand_dict:
            return self.hand_dict[name]
        else:
            return False