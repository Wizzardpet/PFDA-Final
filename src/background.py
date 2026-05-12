import pygame

class Background:
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))