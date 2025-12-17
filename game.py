import random, Cards, PieceRed, PieceBlue
#import board setup
turn = 1 
piece = 0

def shuffle(card_list):
    #recreate card_list based on card info
    random.shuffle(card_list)

def draw_card(card_list, piece):
    if card_list != []:
        #adapt based on card info
        card = random.choice(card_list)
        #adapt based on card info
        card.effect()
        #adapt based on card info
        card_list.remove(card)
        turn += 1
    else:
        shuffle()
        draw_card()

# may not need if card effect works in draw_card
#def act_card(card):
#    #adapt based on card info
#    card.effect

def player_turn():
    if turn % 2 != 0:
        #red player turn
        draw_card(card_list, red)
    else:
        #blue player turn
        draw_card(card_list, blue)
    draw_card()
    #act_card()


def game():
    pass

game()