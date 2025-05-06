# Helper function to calculate required scores for subsequent antes
from hand_types import create_hand_types
HAND_TYPES = create_hand_types()


def calculate_ante_scores(requirement = 0):
    for name in HAND_TYPES:
        score = HAND_TYPES[name]
        card_chips_required = (requirement // score.mult) - score.chips
        # Establish maximum score accomodating for rank limitations of some cards
        if name == "TWO_PAIR":
            # Maximum: two aces and two face cards/tens
            maximum_score = (11 * 2) + (10 * 2)
        elif name == "FULL_HOUSE":
            # Maximum: three aces and two face cards/tens
            maximum_score = (11 * 3) + (10 * 2)
        elif name == "STRAIGHT" or name == "STRAIGHT_FLUSH":
            # Maximum: royal straight (11 + 10 * 4)
            maximum_score = 51
        else:
            # Maximum: all aces
            maximum_score = score.cards * 11
        if card_chips_required > maximum_score:
            print(f"A {name} cannot score, as the maximum possible score is {maximum_score}")
        # Checking if the hand will score on its own (uses score.cards instead of 0 assuming each card 
        # will be worth at least 1 chip)
        elif card_chips_required > score.cards:
            print(f"A {name} would require a card chip total of {card_chips_required}")
        else:
            print(f"{name} scores required chips on its own with {score.chips * score.mult}")