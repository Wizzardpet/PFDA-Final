# Have game open
# Present title card and instructions
# Start game loop
# End game loop when player wins, loses, or quits
# Display win/lose message 
# Exit game
import pygame
import sys

pygame.init()
#Making screen

Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Side Scroller")

title_font = pygame.font.SysFont("Arial", 64)
menu_font = pygame.font.SysFont("Arial", 32)

class TitleScreen:
    def __init__(self):
        self.title_text = title_font.render("Brains and Brownies", True, (255,255,255))
        self.prompt_text = menu_font.render("Press any key to start", True, (200,200,200))
        self.finished = False
