import random
import handtests
from classes import Card
from hand_types import create_hand_types
import sys
import ante_scores
import probability


HAND_TYPES = create_hand_types()
DECK_SIZE = 52
HAND_SIZE = 8
DISCARDS = 3
DISCARD_SIZE = 5

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
            sys.exit(0)

        if command == "display_scores":
            # DISPLAY SCORES OF HANDS
            for type, scoring in HAND_TYPES.items():
                print(f"{type} scores {scoring.chips} chips and {scoring.mult} mult with total of {scoring.chips * scoring.mult}")
        
        
        if command == "create_deck":
            #Create random deck and random hand
            deck = populate_random_deck()
            hand = random.sample(deck, HAND_SIZE)
            deck = [card for card in deck if card not in hand]

            print("Initial hand: ", end = "")
            display_cards(hand)
            print("")
            print("Deck size:", len(deck))

        if command == "pair_prob":
            #Create random deck and random hand
            deck = populate_random_deck()
            hand = random.sample(deck, HAND_SIZE)
            deck = [card for card in deck if card not in hand]

            print("")
            print("Initial hand: ", end = "")
            display_cards(hand)
            print("\n")
            print("Deck size:", len(deck))
            print("\n")

            # TODO: Redo this because this aint it chief
            probabilities = probability.check_pair_probability(hand, deck)
            
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
                
                

        if command == "pair_win":
            check_score()
        
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
    print("create_deck : create a random deck and hand")
    print("exit : terminate program")
    print("pair_prob : display likelihood of drawing a pair for each card")
    print("pair_win : display score of a pair for each card in your hand")
    print("ante1_blind_scores : display chips that cards have to add up to to win the first ante blinds in 1 hand (for each hand type)")
    return True

def check_score():
    #Create random deck and random hand
    deck = populate_random_deck()
    hand = random.sample(deck, HAND_SIZE)
    deck = [card for card in deck if card not in hand]

    print("Initial hand: ", end = "")
    display_cards(hand)
    print("")
    print("Deck size:", len(deck))

    requirement = 300

    # Check whether a pair exists in hand
    played_hand = None
    candidates = [hand[0]]
    for i in range(1, len(hand) - 1):
        for candidate in candidates:
            if hand[i].rank == candidate.rank:
                played_hand = [hand[i], candidate]
                break
        candidates.append(hand[i])
    
    # Exit if there is no pair in hand
    if not played_hand:
        print("You do not have a pair.")
        return False
    
    print("Played hand: ", end = "")
    display_cards(played_hand)
    print("")
    
    wins = calculate_scores(HAND_TYPES["PAIR"], played_hand, requirement)
    display_cards(played_hand)
    if played_hand[0].rank != played_hand[1].rank:
        print("This is not a pair.")
    elif wins["wins"]:
        print(f"satisfies requirement of {requirement} with {wins["score"]} points.")
    else:
        print(f"does not satisfy requirement of {requirement} with {wins["score"]} points.")
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


def check_pair_probability(hand, deck):
    probabilities = {}
    for held_card in hand:
        compatible_cards = []
        for deck_card in deck:
            if handtests.check_pair([held_card, deck_card]):
                compatible_cards.append(deck_card)
        probabilities[held_card] = compatible_cards
    
    return probabilities


def calculate_scores(base_score, cards, requirement):
    output = {}

    # Handle passing in a single card
    if type(cards) is not list:
        # Check if the hand type is high card
        ishighcard = (base_score.chips == 5 and base_score.mult == 1)
        # Calculate if hand is high card, else return False, since one card cannot fulfill anything else
        if ishighcard:
            output["score"] = (cards.chips + base_score.chips) * base_score.mult
            output["wins"] = (output["score"] >= requirement)
            return output
        else:
            return {0, False}
    
    chips = base_score.chips
    for card in cards:
        chips += card.chips
    output["score"] = chips * base_score.mult
    output["wins"] = output["score"] >= requirement
    return output
    

def calculate_pair_score(base_score, card, requirement):
    output = {}
    chips = (card.chips * 2) + base_score.chips
    mult = base_score.mult
    score = chips * mult
    output["score"] = score
    output["wins"] = (score >= requirement)
    return output


if __name__ == "__main__":
    main()