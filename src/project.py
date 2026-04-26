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
title_bg = pygame.image.load('docs/assets/pfda_titlecard.png').convert()
pygame.display.set_caption("Side Scroller")

title_font = pygame.font.Font('docs/PixelDraft-Regular.ttf', 64)
menu_font = pygame.font.SysFont("Arial", 32)

class TitleScreen:
    def __init__(self):
        self.title_text = title_font.render("Brains and Brownies", True, (255,255,255))
        self.prompt_text = menu_font.render("Press any key to start", True, (200,200,200))
        self.finished = False

    def handle_events(self,events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.finished = True

    def update(self): #to add animations
        pass

    def draw(self, screen):
        screen.blit(title_bg, (0,0)) #background color

        title_rect = self.title_text.get_rect(center=(Width//2, Height//3))
        prompt_rect = self.prompt_text.get_rect(center=(Width//2, Height//2))

        screen.blit(self.title_text, title_rect)
        screen.blit(self.prompt_text, prompt_rect)

def main():
    clock = pygame.time.Clock()
    title_screen = TitleScreen()

    game_state = "title"

    while True:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "title":
            title_screen.handle_events(events)
            title_screen.update()
            title_screen.draw(screen)

            if title_screen.finished:
                game_state = "game"

        elif game_state == "game":
            screen.fill((50,50,100))

        pygame.display.flip()
        clock.tick(60)

main()
