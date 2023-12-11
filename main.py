import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cards = random.choice(cards)
    return cards


user_cards = []
Computers_card = []


def first_cards():
    for _ in range(2):
        user_cards.append(deal_card())
        Computers_card.append(deal_card())


def play_game():
    print("Your card", user_cards)
    print("Computers first card", Computers_card[0])
    while True:
        if sum(user_cards) > 21:
            print("You loss")
            print("Computer Win")
            print("player", user_cards, "total", sum(user_cards), "/n Computers card", sum(Computers_card))
            return True
        elif sum(Computers_card) > 21:
            print("Computer loss")
            print("you Win")
            print("player", user_cards, "total", sum(user_cards), "/n Computers card", sum(Computers_card))
            return True

        inputs = input("type y to got another card , type n for pass")

        if inputs.lower() == "y":
            new_card = deal_card()
            user_cards.append(new_card)
            print("Your card", user_cards)
            print("Computers first card", Computers_card[0])

        else:
            you_score = (sum(user_cards) - 21)
            coumputers_score = (sum(Computers_card) - 21)

            if you_score < coumputers_score:
                print("you win")
            elif you_score > coumputers_score:
                print("You loss")
            else:
                print("drowe")
            return True





while True:
    player_input = input("You want to Play y for yes and n for no: ")
    if player_input.lower() == "y":
        first_cards()
        play_game()
    else:
        break
