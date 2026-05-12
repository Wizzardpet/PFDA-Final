#define characters and their attributes (health, attack power, etc.)

import pygame

class Player:
    def __init__(self):
        #position
        self.x = 100
        self.y = 400

        #movement
        self.speed = 5

        #health
        self.health = 70

        #attack settings
        self.attacking = False
        self.attack_cooldown = 0
        self.hit_cooldown = 0

        #Load sprite
        self.image = pygame.image.load('docs/assets/player.png').convert_alpha()

        #rectangle for collision
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

        self.rect.midbottom = (self.x, self.y)

        if keys[pygame.K_d]:
            self.x +=self.speed

        #update collision rectangle
        self.rect.midbottom = (self.x, self.y)

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

    def attack(self,keys):

        if keys[pygame.K_SPACE] and self.attack_cooldown == 0:
            self.attacking = True
            self.attack_cooldown = 30 #cooldown frames

        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

        if self.attacking and self.attack_cooldown <= 15: #attack active for 15 frames
            self.attacking = False

    def take_damage(self, amount):
        if self.hit_cooldown == 0:
            self.health -= amount
            self.hit_cooldown = 60

    def draw(self, screen):
        screen.blit(self.image, self.rect)