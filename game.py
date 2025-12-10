# this will be the main file for the game
import random
import pygame

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
    

    class Player_1:
        endzone = ["SafetyZoneP1", "HomeP1"]
    class Player_2:
        endzone = ["SafetyZoneP2", "HomeP2"]

game()





