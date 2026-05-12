# Have game open
# Present title card and instructions
# Start game loop
# End game loop when player wins, loses, or quits
# Display win/lose message 
# Exit game
import pygame
import sys
from background import Background
from player import Player
from zombies import Zombie
import random

pygame.init()
#Making screen

Width, Height = 800, 600
screen = pygame.display.set_mode((Width, Height))
title_bg = pygame.image.load('docs/assets/pfda_titlecard.png').convert()
win_bg = pygame.image.load('docs/assets/pfda_titlecard.png').convert()
lose_bg = pygame.image.load('docs/assets/pfda_titlecard.png').convert()
pygame.display.set_caption("Side Scroller")

title_font = pygame.font.Font('docs/PixelDraft-Regular.ttf', 64)
menu_font = pygame.font.SysFont("Arial", 32)

zombies = []

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

class Winscreen:
    def __init__(self):
        self.text = title_font.render("You Win!", True, (255,255,255))
        self.prompt = menu_font.render("Press R to restart", True, (200,200,200))

    def draw(self, screen):
        
        screen.blit(self.text, (Width//2 -150, Height//3))
        screen.blit(self.prompt, (Width//2 -150, Height//2))

class GameOverScreen:
    def __init__(self):
        self.text = title_font.render("You Died", True, (255,255,255))
        self.prompt = menu_font.render("Press R to restart", True, (200,200,200))

    def draw(self, screen):
        
        screen.blit(self.text, (Width//2 -130, Height//3))
        screen.blit(self.prompt, (Width//2 -130, Height//2))

def spawn_wave():
    count = random.randint(1, 3)

    for i in range(count):
        x = 800 + i * 100
        y = 400
        zombies.append(Zombie(x,y))

def main():
    clock = pygame.time.Clock()
    title_screen = TitleScreen()

    player = Player()
    game_bg = Background('docs/assets/background.png', Width, Height)

    win_screen = Winscreen()
    game_over_screen = GameOverScreen()

    
    zombies_killed = 0
    required_kills = 10

    spawn_timer = 0
    spawn_delay = 180

    
    flash_timer = 0
    flash_duration = 10


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
            keys = pygame.key.get_pressed()

            if player.health <= 0:
                game_state = "game_over"

            elif zombies_killed >= required_kills and player.health > 0:
                game_state = "win"

            else:
                
                player.move(keys)
                player.attack(keys)

                spawn_timer += 1
                if spawn_timer >= spawn_delay:
                    spawn_wave()
                    spawn_timer = 0

                new_zombies = []

                for zombie in zombies:
                    zombie.move()
                    zombie.attack_player(player)

                    if player.attacking and zombie.rect.colliderect(player.rect):
                        zombie.take_damage(8)

                    if zombie.alive and zombie.x > -200:
                        new_zombies.append(zombie)
                    else:
                        zombies_killed += 1

                zombies[:] = new_zombies

                # --- DRAW (ONLY ONCE EACH) ---
                game_bg.draw(screen)

                for zombie in zombies:
                    zombie.draw(screen)

                player.draw(screen)

        elif game_state == "win":
            screen.blit(win_bg, (0, 0))
            win_screen.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_state = "title"
                zombies.clear()
                zombies_killed = 0
                player = Player()
                spawn_timer = 0
                title_screen.finished = False

        elif game_state == "game_over":
            screen.blit(lose_bg, (0, 0))
            game_over_screen.draw(screen)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game_state = "title"
                zombies.clear()
                zombies_killed = 0
                player = Player()
                spawn_timer = 0
                title_screen.finished = False

        pygame.display.flip()
        clock.tick(60)

main()
