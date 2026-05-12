import pygame

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = 4
        self.health = 30
        self.damage = 2
        self.attack_cooldown = 0

        self.image = pygame.image.load('docs/assets/zombie.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

        self.alive = True

    def move(self):
        self.x -= self.speed
        self.rect.midbottom = (self.x, self.y)

    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.alive = False

    def attack_player(self, player):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
            return

        if self.rect.colliderect(player.rect):
            player.health -= self.damage
            self.attack_cooldown = 60

    def draw(self, screen):
        screen.blit(self.image, self.rect)


        