import pygame, sys
from pygame.locals import* 
import random, time


pygame.init()

FPS=60
clock=pygame.time.Clock()


BLUE=(0,0,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLACK=(0,0,0)
WHITE=(255,255,255)


S_WIDTH=565
S_HEIGHT=650
SPEED=5
SCORE=0
COINS=0


font=pygame.font.SysFont(None,60)
font_small=pygame.font.SysFont(None,60)
game_over = font.render("GAME OVER", True, BLACK)
scoring = font.render("Score",True,BLACK)

background=pygame.image.load("/Users/firuza/Desktop/PP2/week8/racer/back.jpg")

DISPLAYSURF = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/firuza/Desktop/PP2/week8/racer/b.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,S_WIDTH-10),0)
    

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if(self.rect.top>S_HEIGHT):
            SCORE+=1
            self.rect.top=0
            self.rect.center=(random.randint(40,S_WIDTH-10),0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/firuza/Desktop/PP2/week8/racer/r.png")
        self.rect=self.image.get_rect()
        self.rect.center=(160,520)
    
    def move(self):
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("/Users/firuza/Desktop/PP2/week8/racer/Копия-Coin_1.png")
        self.rect=self.image.get_rect()
        self.rect.center=(random.randint(40,360),random.randint(-100,0))
        self.weight=1
        self.mask=pygame.mask.from_surface(self.image)

    def move(self):
        global COINS
        if self.rect.top>S_HEIGHT:
            self.rect.top=0
            self.rect.center=(random.randint(40,450),0)
        elif pygame.sprite.spritecollide(self,player,False,pygame.sprite.collide_mask):
            COINS+=self.weight
            self.rect.top=0
            self.rect.center=(random.randint(40,450),0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,450), 0)

        self.rect.move_ip(0,SPEED)
p1=Player()
e1=Enemy()

player=pygame.sprite.Group()
player.add(p1)
coins_group=pygame.sprite.Group()
enemies=pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

inc_speed=pygame.USEREVENT+1
pygame.time.set_timer(inc_speed,1000)

for i in range(3):
    c1=Coin()
    coins_group.add(c1)
    all_sprites.add(c1)


while True:
    for event in pygame.event.get():
        if event.type==inc_speed:
            SPEED += 0.5
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    DISPLAYSURF.blit(background,(0,0))
    SCORES=font_small.render(str(SCORE),True,BLACK)
    coins_view=font_small.render(str(COINS),True,BLACK)
    DISPLAYSURF.blit(SCORES,(10,10))
    DISPLAYSURF.blit(coins_view,(535,10))


    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p1, enemies):
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (100,250))
           
        pygame.display.update()
        for entity in all_sprites:
                entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
    pygame.display.update()
    
    clock.tick(FPS)


    



    






                






















