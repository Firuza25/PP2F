import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("ball")
pygame.display.set_icon(pygame.image.load("/Users/firuza/Desktop/PP2/week7/images/pr.png"))
x = 50
y = 350

speed = 20
clock = pygame.time.Clock()
running = True
while running:

    pygame.display.update()
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, 'Red', (x, y), 25)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 30:
        x -= speed
    elif keys[pygame.K_RIGHT] and x < 570:
        x += speed
    elif keys[pygame.K_DOWN] and y < 370:
        y += speed
    elif keys[pygame.K_UP] and y > 30:
        y -= speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(20)

    '''Draw circle - a red ball of size 50 x 50 (radius = 25) on white background.
      When user presses Up, Down, Left, Right arrow keys on keyboard, the ball should 
      move by 20 pixels in the direction of pressed key. The ball should not leave the screen, i.e. 
      user input that leads the ball to leave of the screen should be ignored
    '''