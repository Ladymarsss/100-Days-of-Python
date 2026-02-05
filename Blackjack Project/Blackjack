import art
import random

print(art.logo)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False

def draw_one(player, dealer, dealer_score, player_score):
    draw = input("would you like to draw another card 'y' or 'n': ").lower()
    if draw == "y":
        random.shuffle(deck)
        player += deck[:1]
        player_score = sum(player)
        print(f"Your cards: {player}, current score: {player_score}\nDealer first card: {dealer[0]}")
        if player_score == 21:
            draw_one(player, dealer, dealer_score, player_score)
        if player_score > 21:
            for index, number in enumerate(player):
                if player_score > 21 and number == 11:
                    player[index] = 1
                    player_score = sum(player)
                    break
            if player_score > 21:
                print(f"Your final hand: {player}, final score: {player_score}\nDealer final hand: {dealer}, final score {dealer_score}")
                print("You passed 21, YOU LOSE!")
                new_game()
            else:
                print(f"Your cards: {player}, current score: {player_score}\nDealer first card: {dealer[0]}")
                draw_one(player, dealer, dealer_score, player_score)
        elif player_score < 21:
            draw_one(player, dealer, dealer_score, player_score)
        elif dealer_score < 21:
            random.shuffle(deck)
            dealer += deck[:1]
    if draw == "n":
        if player_score > dealer_score:
            print(f"Your final hand: {player}, final score: {player_score}\nDealer final hand: {dealer}, final score: {dealer_score}\nYOU WIN!!")
            new_game()
        elif dealer_score > player_score:
            print(f"Your final hand: {player}, final score: {player_score}\nDealer final hand: {dealer}, final score: {dealer_score}\nYOU LOSE!!")
            new_game()


def start():
    player = []
    dealer = []
    random.shuffle(deck)
#This shuffles and give cards to dealer and player.
    player += deck[:2]
    random.shuffle(deck)
    dealer += deck[:2]
# print(dealer, player) #This is to check player and dealer values on list
#This gives me the score of the cards summed up
    player_score = sum(player)
    dealer_score = sum(dealer)
    print(f"Your cards: {player}, current score: {player_score}\nDealer first card: {dealer[0]}")
#If player or dealer has a blackjack
    if player[:2] and player_score == 21:
        print(f"Your final hand: {player}, final score: {player_score}\nDealer final hand: {dealer}, final score {dealer_score}")
        print("You got a BLACKJACK! You Win!")
        new_game()
    elif dealer[:2] and dealer_score == 21:
        print(f"Your final hand: {player}, final score: {player_score}\nDealer final hand: {dealer}, final score {dealer_score}")
        print("Dealer have a BLACKJACK! You Lose!")
        new_game()
    else:
        draw_one(player, dealer, dealer_score, player_score)

def new_game():
    new_game = input("Press 'ENTER' to start your game: ")
    if new_game == "":
        print("\n" * 100, art.logo)
        start()

new_game()
