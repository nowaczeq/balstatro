from classes import Card

# FUNCTIONS TO CHECK WHETHER A HAND TYPE WAS ACHIEVED
# hand: an amount of cards to be checked by the function
# rtype: {["wins"]: bool, ["cards"]: Card()}
# ["wins"] indicates whether the hand contains the card
# ["cards"] return the cards used to create the hand, and all cards in hand if hand doesn't win

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

    foundthree = False
    candidates = []
    for key, value in ranks.items():
        if value == 3:
            for card in hand:
                if card.rank == key:
                    candidates.append(card)
            output["cards"] = candidates
            foundthree = True
            break
    
    if not foundthree: output["cards"] = None
    output["wins"] = foundthree
    return output

def check_four_of_a_kind(hand):
    output = {}
    if type(hand) is not list: 
        output["cards"] = None
        output["wins"] = False
        return output
    
    ranks = {}
    candidates = []

    for card in hand:
        if card.rank not in ranks:
            ranks[card.rank] = 1
            candidates.append(card)
        elif ranks[card.rank] == 3:
            output["wins"] = True
            candidates.append(card)
            output["cards"] = candidates
            return output
        else:
            ranks[card.rank] += 1
            candidates.append(card)

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
    
    ranks = []
    for card in hand:
        ranks.append(card.rank)
    
    ranks.sort()
    for i in range(0, len(ranks) - 1):
        if ranks[i] != (ranks[i + 1] - 1):
            output["wins"] = False
            output["cards"] = None
            return output
        
    output["wins"] = True
    return output

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
    card1.suit = "hearts"
    card1.rank = 2
    card2 = Card()
    card2.suit = "clubs"
    card2.rank = 2
    card3 = Card()
    card3.suit = "hearts"
    card3.rank = 3
    card4 = Card()
    card4.suit = "hearts"
    card4.rank = 5
    card5 = Card()
    card5.suit = "diamonds"
    card5.rank = 2
    cards = [card1, card2, card3, card4, card5]
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