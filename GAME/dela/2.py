import pygame

pygame.init()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Моя игра с бассейном")


screen.fill((255,255,255))
pygame.draw.rect(screen,(0,0,0),(25,25,950,650),6)
pygame.draw.rect(screen,(0,0,255),(125,95,750,500),6)
pygame.draw.rect(screen,(0,0,255),(30,200,100,75),6)
pygame.draw.rect(screen,(0,0,255),(30,400,100,75),6)
pygame.draw.rect(screen,(0,0,255),(869,200,100,75),6)
pygame.draw.rect(screen,(0,0,255),(870,400,100,75),6)
pygame.draw.rect(screen,(0,0,255),(300,590,100,75),6)
pygame.draw.rect(screen,(0,0,255),(600,590,100,75),6)
background_image = pygame.image.load('/Users/firuza/Desktop/ww.png')
screen.blit(background_image, (127, 100))
screen.blit(background_image, (127, 150))
screen.blit(background_image, (127, 200))
screen.blit(background_image, (127, 250))
screen.blit(background_image, (127, 300))
screen.blit(background_image, (127, 350))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

  
    pygame.display.flip()
