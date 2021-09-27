import random

# deck of cards where face cards are denoted by 10 and ace is denoted by 11
cards = [2,3,4,5,6,7,8,9,10,10,10,10,10,11]

# function for picking two random cards for user and one for computer
def start_game():
    pick1 = random.choice(cards)
    pick2 = random.choice(cards)
    #random card selection for computer
    com_pick1 = random.choice(cards)

    #create and push cards in a list
    user_card = [pick1, pick2]
    dealer_card = [com_pick1]

    #return the list of user card and computer card
    return user_card , dealer_card


#function for adding the user cards number
def add_user_card(user_card):
    user_sum = 0
    for i in user_card:
        user_sum += i

    return user_sum

# function for a black jack condition
def blackjack(name="com"):
    if name == "com":
        print(f" blackjack , {name} wins")
    else:
        print(f" blackjack , {name} wins")

#function for bust condition , this condition will apply when user or computer have cards whose sum is more than 21
def bust(name = "com"):
    if name == "com":
        print(f"value greater than 21 ,  {name}puter loose")
    else:
        print(f"value greater than 21 , {name} loose")

# function for adding computer cards
def add_com_card(dealer_card):
    com_sum = 0
    while com_sum<16:
        com_sum = 0
        com_pick = random.choice(cards)
        dealer_card.append(com_pick)
        print(dealer_card)
        for i in dealer_card:
            com_sum += i
        print(com_sum)

    return com_sum



# function for revaling the computer card and campraing the computer card with user card
def stand(name,user_card , dealer_card):

    com_sum = add_com_card(dealer_card)
    user_sum = add_user_card(user_card)

    if user_sum== 21:
        blackjack(name)

    elif user_sum > 21 :
        bust(name)
    else:
        if com_sum == 21:
            blackjack()

        elif com_sum >21:
            bust()
        else :
            if user_sum>com_sum:
                print(f"you win {name}")
            elif user_sum == com_sum:
                print("draw")
            else:
                print("computer wins")

#function for choosing a new card for user from a deck
def hit(user_card):
    pick = random.choice(cards)
    user_card.append(pick)
    print(f"user card are {user_card}")
    return user_card

# function for user choice to take either hit or stand
def user_option():
    # asking for user to choose either hit or stand the game
    print("what you want to choose? type h for hit or s for stand")
    user_choice = input(f"{user_name} type your choice = ").lower()

    # conditions depending upon user choice
    if user_choice == "s":
        stand(name=user_name, user_card=user_card, dealer_card=dealer_card)

    elif user_choice == "h":
        hit(user_card=user_card)
        user_option()

    else:
        print("choice")


# use flag play_jack to track the user activity , should he want to continue or quit
play_blackjack = True

user_name = input("enter your name = ")
# game is on until user type quit
while play_blackjack:
    # calling the function start to assign the number to user card and com card
    user_card , dealer_card = start_game()
    print(f"your card is {user_card} and dealer card is {dealer_card}")

    print("\n")
    #calling function for user option
    user_option()

    # take user decision to continue or not
    user_decision = input("wish to quit the game press q for quit = ").lower()
    if user_decision == "q":
        play_blackjack = False
    print("\n\n")