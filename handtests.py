# FUNCTIONS TO CHECK WHETHER A HAND TYPE WAS ACHIEVED
# hand: an amount of cards to be checked by the function
# rtype: {["wins"]: bool, ["cards"]: Card()}
# ["wins"] indicates whether the hand contains the card
# ["cards"] return the cards used to create the hand, and all cards in hand if hand doesn't win

class Card:
    def __init__(self):
        self.suit = ""
        self.rank = 0
        self.chips = 0

def check_high_card(hand):
    highest = Card()
    highest.rank = 0
    for card in hand:
        if card.rank > highest.rank:
            highest = card
    
    output = {}
    output["wins"] = True
    output["cards"] = highest
    return output

# TODO REDO
def check_pair(hand):
    output = {}
    if type(hand) is not list: 
        output["wins"] = False
        output["cards"] = None
        return output
    if len(hand) < 2:
        output["wins"] = False
        output["cards"] = None
        return output
    
    checker = {}
    for card in hand:
        if card.rank not in checker:
            checker[card.rank] = card
        else:
            output["cards"] = [checker[card.rank], card]
            output["wins"] = True
            return output
    
    output["wins"] = False
    output["cards"] = None
    return output

def check_two_pair(hand):
    tmphand = []
    for card in hand:
        tmphand.append(card)

    output = {}
    if type(tmphand) is not list: 
        output["wins"] = False
        output["hand"] = None
        return output
    if len(hand) < 4:
        output["wins"] = False
        output["hand"] = None
        return output

    first_pair = check_pair(tmphand)
    if not first_pair["wins"]:
        output["wins"] = False
        output["cards"] = None
        return output
    firstpaircards = first_pair["cards"]
    for card in firstpaircards:
        tmphand.remove(card)
    
    second_pair = check_pair(tmphand)
    if not second_pair["wins"]:
        output["wins"] = False
        output["cards"] = None
        return output

    if first_pair["cards"][0].rank == second_pair["cards"][0].rank:
        output["wins"] = False
        output["cards"] = None
        return output

    output["wins"] = True
    output["cards"] = first_pair["cards"] + second_pair["cards"]

    return output

def check_three_of_a_kind(hand):
    output = {
        "cards": [],
        "wins": False
    }
    if type(hand) is not list: 
        output["cards"] = None
        output["wins"] = False
        return output
    
    ranks = {}

    for card in hand:
        if card.rank not in ranks:
            ranks[card.rank] = [card]
        else:
            ranks[card.rank].append(card)
    
    max_rank = 0
    foundthree = False
    for key, value in ranks.items():
        if len(value) >= 3 and key > max_rank:
            max_rank = key
            foundthree = True

    if not foundthree:
        output["cards"] = None
        output["wins"] = False
        return output
    
    for card in hand:
        if card.rank == max_rank and len(output["cards"]) < 3:
            output["cards"].append(card)
    
    output["wins"] = True
    return output

def check_four_of_a_kind(hand):
    output = {}
    if type(hand) is not list: 
        output["cards"] = None
        output["wins"] = False
        return output
    
    ranks = {}

    for card in hand:
        if card.rank not in ranks:
            ranks[card.rank] = 1
        else:
            ranks[card.rank] += 1
            

    output["wins"] = False
    output["cards"] = None
    return output

def check_flush(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["wins"] = False
        output["cards"] = None
        return output
    target = hand[0].suit
    for card in hand:
        if card.suit != target:
            output["wins"] = False
            output["cards"] = None
            return output
        
    output["wins"] = True
    return output

def check_full_house(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["cards"] = None
        output["wins"] = False
        return output
    cards = {}
    for card in hand:
        if card.rank not in cards:
            cards[card.rank] = 1
        else:
            cards[card.rank] +=1

    pair = False
    three = False
    for key, value in cards.items():
        if value == 2:
            pair = True
        elif value == 3:
            three = True
    
    output["wins"] = (pair and three)
    if not output["wins"]: output["cards"] = None
    return output

def check_straight(hand):
    output = {}
    output["cards"] = hand

    if type(hand) is not list: 
        output["wins"] = False
        output["cards"] = None
        return output
    
    ranks = set()
    for card in hand:
        ranks.add(card.rank)
    
    if len(ranks) < 5:
        output["wins"] = False
        output["cards"] = None
        return output
    
    ranks = sorted(ranks)
    for i in range(len(ranks) - 1):
        if ranks[i + 1] != ranks[i] + 1:
            output["wins"] = False
            output["cards"] = None
            return output
    
    output["wins"] = True
    # TODO: Change this to return the cards that comprise the straight
    output["cards"] = None
    return output

    # ranks = []
    # for card in hand:
    #     ranks.append(card.rank)
    
    # ranks.sort()
    # for i in range(0, len(ranks) - 1):
    #     if ranks[i] == (ranks[i + 1]):
    #         continue
    #     if ranks[i] != (ranks[i + 1] - 1):
    #         output["wins"] = False
    #         output["cards"] = None
    #         return output
        
    # output["wins"] = True
    # return output

def check_straight_flush(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["wins"] = False
        output["cards"] = None
        return output
    output["wins"] = check_flush(hand)["wins"] and check_straight(hand)["wins"]
    if output["wins"]:
        output["cards"] = hand
    else:
        output["cards"] = None
    return output

def check_five_of_a_kind(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["wins"] = False
        output["cards"] = None
        return output
    
    target_rank = hand[0].rank
    for i in range(1, len(hand)):
        target_rank = target_rank ^ hand[i].rank
    
    output["wins"] = not target_rank
    if target_rank: output["cards"] = None
    return output

def check_flush_five(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["wins"] = False
        return output
    
    output["wins"] = check_flush(hand)["wins"] and check_five_of_a_kind(hand)["wins"]
    if output["wins"]:
        output["cards"] = hand
    else:
        output["cards"] = None
    return output

def check_flush_house(hand):
    output = {}
    output["cards"] = hand
    if type(hand) is not list: 
        output["wins"] = False
        return output
    
    output["wins"] = check_flush(hand)["wins"] and check_full_house(hand)["wins"]
    if output["wins"]:
        output["cards"] = hand
    else:
        output["cards"] = None
    return output


def test():
    card1 = Card()
    card2 = Card()
    card3 = Card()
    card4 = Card()
    card5 = Card()
    card6 = Card()
    card7 = Card()
    card8 = Card()

    card1.suit = "diamonds"
    card1.rank = 2

    card2.suit = "diamonds"
    card2.rank = 2

    card3.suit = "diamonds"
    card3.rank = 3

    card4.suit = "diamonds"
    card4.rank = 5

    card5.suit = "diamonds"
    card5.rank = 2

    card6.suit = "diamonds"
    card6.rank = 4
    
    card7.suit = "diamonds"
    card7.rank = 2

    card8.suit = "diamonds"
    card8.rank = 6

    cards = [
        card1, 
        card2, 
        card3, 
        card4, 
        card5, 
        card6, 
        card7, 
        card8]
    print("Played hand: ", end = "")
    display_cards(cards)
    print("")

    highcard = check_high_card(cards)
    pair = check_pair(cards)
    twopair = check_two_pair(cards)
    threeofakind = check_three_of_a_kind(cards)
    fourofakind = check_four_of_a_kind(cards)
    flush = check_flush(cards)
    straight = check_straight(cards)
    fullhouse = check_full_house(cards)
    straighflush = check_straight_flush(cards)
    fiveofakind = check_five_of_a_kind(cards)
    flushfive = check_flush_five(cards)
    flushhouse = check_flush_house(cards)

    print("Checker:")
    print("High card: " + str(highcard["wins"]) + " with ", end = "")
    display_card(highcard["cards"])
    print("")
    print("Pair: " + str(pair["wins"]) + " with ", end = "")
    display_cards(pair["cards"])
    print("")
    print("Two pair: " + str(twopair["wins"]) + " with ", end = "")
    display_cards(twopair["cards"])
    print("")
    print("Three of a kind: " + str(threeofakind["wins"]) + " with ", end = "")
    display_cards(threeofakind["cards"])
    print("")
    print("Four of a kind: " +  str(fourofakind["wins"]) + " with ", end = "")
    display_cards(fourofakind["cards"])
    print("")
    print("Flush: " +  str(flush["wins"]) + " with ", end = "")
    display_cards(flush["cards"])
    print("")
    print("Straight: " +  str(straight["wins"]) + " with ", end = "")
    display_cards(straight["cards"])
    print("")
    print("Full House: " +  str(fullhouse["wins"]) + " with ", end = "")
    display_cards(fullhouse["cards"])
    print("")
    print("Straight Flush: " +  str(straighflush["wins"]) + " with ", end = "")
    display_cards(straighflush["cards"])
    print("")
    print("Five of a Kind: " +  str(fiveofakind["wins"]) + " with ", end = "")
    display_cards(fiveofakind["cards"])
    print("")
    print("Flush Five: " +  str(flushfive["wins"]) + " with ", end = "")
    display_cards(flushfive["cards"])
    print("")
    print("Flush House: " +  str(flushhouse["wins"]) + " with ", end = "")
    display_cards(flushhouse["cards"])
    print("")


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
    test()