import random
import os

#Defining the card deck as an array:
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4
#Deal function ( and converting numbers to face cards)
def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 1:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y" or again == 'Y':
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        clear()
        game()
    else:
        print ("See ya.")
        exit()

#calculating the total, and converting face cards back to numbers:
def total(hand):
    total = 0
    for card in hand:
        if card == "J":
            total += 10
        elif card == "Q":
            total += 11
        elif card == "K":
            total += 12
        elif card == "A":
            total += 1
        else:
            total += card
    return total

def hit(hand):
    card = deck.pop()
    facevalue = {"J":11, "Q":12, "K":13, "A":1}
    if card == 11:
        card = facevalue["J"]
    if card == 12:
        card = facevalue["Q"]
    if card == 13:
        card = facevalue["K"]
    if card == 1:
        card = facevalue["A"]
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()
    print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
    print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Congratulations! You got a Blackjack!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print ("Dealer busts. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Sorry. Your score isn't higher than the dealer. You lose.")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print ("Congratulations! Your score is higher than the dealer. You win!")

def game():
    choice = 0
    clear()
    print ("Welcome to Blackjack! (Made by Aadi Anjaria)\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print ("The dealer is showing a " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)

        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print ("Bye!")
            exit()

if __name__ == "__main__":
   game()

#code cleanup still needs to be done
