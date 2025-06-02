import random
import handtests
from classes import Card, HandType, TypeChecker, HandTypeTranslator
from hand_types import create_hand_types
import sys
import ante_scores
import probability


HAND_TYPES = create_hand_types()
DECK_SIZE = 52
HAND_SIZE = 8
DISCARDS = 3
DISCARD_SIZE = 5
CHECKER = TypeChecker()

random.seed(100)

def main():
    print("BALSTATRO MAIN MENU")
    print("Type 'usage' to see commands")
    command = ""
    while True:
        while not command:
            command = input("Input command: ")

        if command == "usage":
            usage()

        if command == "exit":
            print("Exiting program. Goodbye!")
            sys.exit(0)

        if command == "display_scores":
            # DISPLAY SCORES OF HANDS
            for type, scoring in HAND_TYPES.items():
                print(f"{type} scores {scoring.chips} chips and {scoring.mult} mult with total of {scoring.chips * scoring.mult}")

        if command == "pair_prob":
            #Create random deck and random hand
            deck = populate_random_deck()
            hand = random.sample(deck, HAND_SIZE)
            deck = [card for card in deck if card not in hand]
            # Amount of additional cards you can see from the deck if you hard fish for the pair
            draw_limit = DISCARD_SIZE * DISCARDS

            print("")
            print("Initial hand: ", end = "")
            display_cards(hand)
            print("\n")
            print("Deck size:", len(deck))
            print("\n")

            # TODO: Redo this because this aint it chief
            probabilities = probability.check_pair_probability(hand, deck, draw_limit)
            
            print("PROBABILITY FOR PAIRS:")
            print("")
            for key, value in probabilities.items():
                # Amount of cards that comprise a compatible pair
                compatible_for_pair = len(value)

                # Calculate the probability that the next drawn card will create a compatible pair
                pair_probability = compatible_for_pair / len(deck)

                print("For ", end="")
                display_card(key)
                print(": ", end = " ")
                print(f"{pair_probability * 100}% with: ")
                for card in value:
                    display_card(card)
                
        if command == "play_blind":
            play_blind()
        
        if command == "ante1_blind_scores":
            ante1_blinds = {
                "SMALL_BLIND": 300,
                "BIG_BLIND": 450,
                "BOSS_BLIND": 600
            }
            for name, requirement in ante1_blinds.items():
                print(f"ANTE 1 {name}:")
                ante_scores.calculate_ante_scores(requirement)
                print("")

        print("")
        command = ""
        
def usage():
    print("")
    print("display_scores : display base chips and mult for hands")
    print("exit : terminate program")
    print("pair_prob : display likelihood of drawing a pair for each card")
    print("play_blind : play a simulation of a small blind")
    print("ante1_blind_scores : display chips that cards have to add up to to win the first ante blinds in 1 hand (for each hand type)")
    return True

def play_blind():
    #Create random deck and random hand
    deck = populate_random_deck()
    hand = random.sample(deck, HAND_SIZE)
    deck = [card for card in deck if card not in hand]

    print("Initial hand: ", end = "")
    display_cards(hand)
    print("")
    print("Deck size:", len(deck))

    requirement = 300
    print(f"Required score is {requirement}.")
    while True:
        action = input(f"Select action that you'd like to do (play/draw/discard): ")
        if action == "play":
            return play_hand(hand, requirement)
        elif action == "draw":
            draw_amount = random.randint(1, 3)
            print(f"You have drawn {draw_amount} cards.")
            drawn_cards = random.sample(deck, draw_amount)
            deck = [card for card in deck if card not in hand]
            hand = hand + drawn_cards
            print("Current hand: ", end = "")
            display_cards(hand)
        

def play_hand(hand, requirement = 300):
    # Get the hand type that the user wants to play
    played_type_name = ""
    print("Current hand: ", end = "")
    display_cards(hand)
    while True:
        played_type_name = input("Select the hand type that you'd like to play: ")
        if played_type_name in CHECKER.hand_checkers:
            # Create structure for played type
            played_hand = CHECKER.check(hand, played_type_name)
            if not played_hand["wins"]:
                print(f"You are not holding a {played_type_name}")
            else:
                print(f"You are holding a {played_type_name}")
                break
        else:
            print("Not a valid type. ")

    # Calculate score for played hand
    # Translate basic language to hand type language
    translator = HandTypeTranslator()
    handname = translator.translate(played_type_name)

    if handname in HAND_TYPES:
        hand = HAND_TYPES[handname]
    else:
        raise ValueError("Couldn't translate name of played hand")

    # Get the cards that were played in the hand
    cards = played_hand["cards"]
    
    chips = hand.chips
    for card in cards:
        chips += card.chips
    
    score = chips * hand.mult
    print(f"Hand score: {score}")

    if score > requirement:
        print("Successfully passed the requirement.")
        return True
    else:
        print("Hand did not pass the requirement.")
        return True

def populate_random_deck():
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    full_deck = []

    for suit in suits:
        for rank in ranks:
            card = Card()
            card.suit = suit
            card.rank = rank
            if rank < 11:
                card.chips = rank
            elif rank < 14:
                card.chips = 10
            else:
                card.chips = 11
            full_deck.append(card)
    
    return full_deck

def discard(deck, hand, size):
    """
    Discard cards from the hand and return the new hand and the discarded cards.
    """
    discarded = []
    if size > DISCARD_SIZE:
        size = DISCARD_SIZE
    for _ in range(size):
        card = random.choice(hand)
        hand.remove(card)
        discarded.append(card)
    draw(DISCARDS, deck, hand)
    return hand, discarded


def draw(amount, deck, hand):
    """
    Draw cards from the deck and add them to the hand.
    """
    for _ in range(amount):
        if len(deck) == 0:
            print("Deck is empty!")
            break
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand, deck

def display_cards(cards):
        if not cards:
            print("N/A", end="")
        else:
            for card in cards:
                display_card(card)

def display_card(card):
        if not card:
            print("N/A")
        else:
            print(card.rank, "of", card.suit, end=" ")

if __name__ == "__main__":
    main()