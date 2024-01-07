import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.Frame = 0
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        
    def update(self):
        self.Frame += 0.11
        if self.Frame > 10:
            self.Frame -= 10

        Personnel = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png','8.png','9.png','10.png']
        self.image = pygame.transform.scale(pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources//'+ Personnel[int(self.Frame)]).convert_alpha(), (200,80))