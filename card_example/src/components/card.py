import pygame
from buttons.image_button import ImageButton

class CardComponent:
    def __init__(self, screen, x, y, suit, value):
            self.flipped = False
            self.value = value
            self.suit = suit
            
            card_image = f"assets/{value}_{suit}.png"
            
            self.card = ImageButton(screen, x, y, card_image, 0.5)            
            self.back = ImageButton(screen, x, y, "assets/back_red.png", 0.5)
            
    def draw(self):
        if self.flipped == True:
            self.back.draw()
        else:
            self.card.draw()

    def flip(self):
        self.flipped = not self.flipped
    
    def getFlipped(self):
        return self.flipped
        