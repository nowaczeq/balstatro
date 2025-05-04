from classes import HandType

def create_hand_types():

    hand_types = {}

    hand_highcard = HandType()
    hand_highcard.chips = 5
    hand_highcard.mult = 1
    hand_types["HIGH_CARD"] = hand_highcard

    hand_pair = HandType()
    hand_pair.chips = 10
    hand_pair.mult = 2
    hand_types["PAIR"] = hand_pair

    hand_two_pair = HandType()
    hand_two_pair.chips = 20
    hand_two_pair.mult = 2
    hand_types["TWO_PAIR"] = hand_two_pair  

    hand_three_of_a_kind = HandType()
    hand_three_of_a_kind.chips = 30
    hand_three_of_a_kind.mult = 3
    hand_types["THREE_OF_A_KIND"] = hand_three_of_a_kind
  
    hand_four_of_a_kind = HandType()
    hand_four_of_a_kind.chips = 60
    hand_four_of_a_kind.mult = 7
    hand_types["FOUR_OF_A_KIND"] = hand_four_of_a_kind
      
    hand_flush = HandType()
    hand_flush.chips = 35
    hand_flush.mult = 4
    hand_types["FLUSH"] = hand_flush
      
    hand_straight = HandType()
    hand_straight.chips = 30
    hand_straight.mult = 4
    hand_types["STRAIGHT"] = hand_straight
      
    hand_full_house = HandType()
    hand_full_house.chips = 40
    hand_full_house.mult = 4
    hand_types["FULL_HOUSE"] = hand_full_house
      
    hand_straight_flush = HandType()
    hand_straight_flush.chips = 100
    hand_straight_flush.mult = 8
    hand_types["STRAIGHT_FLUSH"] = hand_straight_flush
      
    hand_five_of_a_kind = HandType()
    hand_five_of_a_kind.chips = 120
    hand_five_of_a_kind.mult = 12
    hand_types["FIVE_OF_A_KIND"] = hand_five_of_a_kind
      
    hand_flush_house = HandType()
    hand_flush_house.chips = 140
    hand_flush_house.mult = 14
    hand_types["FLUSH_HOUSE"] = hand_flush_house
      
    hand_flush_five = HandType()
    hand_flush_five.chips = 160
    hand_flush_five.mult = 16
    hand_types["FLUSH_FIVE"] = hand_flush_five
    
    return hand_types
