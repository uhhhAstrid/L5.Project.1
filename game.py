import random
#import card info
#import board setup

def shuffle():
    #recreate card_list based on card info
    random.shuffle(card_list)

def draw_card():
    if card_list != []:
        #adapt based on card info
        card = random.choice(card_list)
        #adapt based on card info
        card_list.remove(card)
    else:
        shuffle()
        draw_card()

def act_card():
    #adapt based on card info
    card.effect

def player_turn():
    draw_card()
    act_card()


def game():
    

game()