import pygame

class zombie:
    def __init__(self):
        self.x = x
        self.y = y

        self.speed = 1
        self.health = 30
        self.damage = 2

        self.image = pygame.image.load('docs/assets/zombie.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

        self.alive = True

    def move(self):
        self.x -= self.speed
        self.rect.topleft = (self.x, self.y)

    def take_damage(self, amount):
        self.health -= amount
        
        if self.health <= 0:
            self.alive = False

    def attack_player(self,player):
        if self.rect.colliderect(player.rect):
            player.health -= self.damage

    def draw(self, screen):
        if self.alive:
            screen.blit(self.image, (self.x, self.y))


        