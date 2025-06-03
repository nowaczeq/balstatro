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
        

class HandTypeTranslator:
    def __init__(self):
        # Add keys for additional translations (keep lowercase)
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
        if name.lower() in self.hand_dict:
            return self.hand_dict[name]
        else:
            return False