# this file will store all of the classes for the game
# of course, this will also include all class functions and variables
from shutil import move


class Card():
    def __init__(self, number, effect):
        self.number = number
        self.effect = effect


    def effects(self, move):
        if self.number == 1:
            move(1)
        if self.number == 2:
            move(-2)
        if self.number == 3:
            move(-3)
        if self.number == 4:
            move(4)
        if self.number == 5:
            move(5)
        if self.number == 6:
            move(6)
        if self.number == 7:
            #calling button for asking split between pieces or move 7
            pass
        if self.number == 8:
            move(8)
        if self.number == 9:
            move(9)
        if self.number == 10:
            #call button for split between peices or move 7
            pass
        if self.number == 11:
            move(11)
        if self.number == 12:
            move(12)
            skipaturn()


class Piece():
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.finished = False

    def getColor(self):
        return self.color

    def setColor(self, newColor):
        self.color = newColor

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition