# this file will store all of the classes for the game
# of course, this will also include all class functions and variables
class Card():
    def __init__(self, number, effect):
        self.number = number
        self.effect = effect

    def card1classfunction(self):
        self.number = 1
        self.effect = move1space
    
    def card2classfunction(self):
        self.number = 2
        self.effect = move2spaces

    def card3classfunction(self):
        self.number = 3
        self.effect = move3spaceback
    
    def card4classfunction(self):
        self.number = 4
        self.effect = move4spaces  

    def card5classfunction(self):
        self.number = 5
        self.effect = move5spaces 

    def card7classfunction(self):
        self.number = 7
        self.effect = move7spaces or splitbetweenpieces
    
    def card8classfunction(self):
        self.number = 8
        self.effect = move8spaces
    
    def card10classfunction(self):
        self.number = 10
        self.effect = move10spaces and movedifcard1spaceback
    
    def card11classfunction(self):  
        self.number = 11
        self.effect = move11spaces or swapanypieces
    
    def card12classfunction(self):
        self.number = 12
        self.effect = move12spaces and skipaturn or move7spaces


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