import pygame
import random

def game():
    
    pygame.init()
    
    
    monitor = pygame.display.set_mode((400,500))
    pygame.display.set_caption("Snake")
    pygame.display.set_icon(pygame.image.load("/Users/firuza/Desktop/SNAKE.PNG"))

    #colors
    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)

    #black line to divided monitor
    head_line_start = (0,100)
    head_line_end = (400,100)

   
    apple = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
    apple_spawn = True
    score = 0
    speed = 1
    level = ['easy','normal','hard','very hard', 'impossible', 'impossible x2', 'death']
    score_font = pygame.font.SysFont('lunchtime Double So',32)

    #direction of snake
    change = 'left'
    direction = 'left'

    #start
    player = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]]

    #FPS
    clock = pygame.time.Clock()

    check = True

    while check:
        for action in pygame.event.get():
        
            if action.type == pygame.QUIT:
                check = False
                pygame.quit()
            
            #Keyboard
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_UP:
                    change = 'up'
                if action.key == pygame.K_DOWN:
                    change = 'down'
                if action.key == pygame.K_LEFT:
                    change = 'left'
                if action.key == pygame.K_RIGHT:
                    change = 'right'
            
        
        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'
        
        #Speed of snake (0 - x, 1 - y cordinates)
        if direction == 'up':
            player[1] -= 10
        if direction == 'down':
            player[1] += 10 
        if direction == 'left':
            player[0] -= 10 
        if direction == 'right':
            player[0] += 10  
        
        
        #Apple spawn (random) if apple generated in otherside, so this apple delete
        while apple_spawn:
            apple = (random.randint(1,monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
            if apple not in snake:
                apple_spawn = False
                
        snake.insert(0, list(player))
              
        #Когда кординаты пикселей совпадают, то это засчитывается за съедение яблока. При поедании каждого 4 яблока скорость будет увеличиваться  
        if player[0] == apple[0] and player[1] == apple[1]:
            score += 1
            apple_spawn = True
            speed = score // 4 + 1
        else:
            snake.pop()
        
        #Обновления монитора, без этой команды змея будет увеличиваться если не будет направления, а при изменения направления размер змеи возвращается на исходный размер
        monitor.fill(white) 
        
        #line
        pygame.draw.line(monitor, black, head_line_start, head_line_end, 1)
        
        #Границы(Если змея пони)
        if ((player[0] < -5 or player[0] > monitor.get_width() - 5) or (player[1] < 100 or player[1] > monitor.get_height() - 5)):
            break
        
       
        print(snake[1:])
        print(player)
        
     
        if player in snake[1:]:
            break
        

        for pos in snake:
            pygame.draw.rect(monitor, black, pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(monitor, red, pygame.Rect(apple[0],apple[1],10,10))
        
        
        monitor.blit(score_font.render(f'Score: {score}' , True, black) , (20,38))
        #Текущий уровень игры
        if speed <= 7:
            monitor.blit(score_font.render(f'Speed: {level [speed - 1]}', True, black), (20,58))
        else:
            monitor.blit(score_font.render(f'Speed: death', True, black), (20,58))
        
        pygame.display.update()
        
        clock.tick(10 + speed * 2)
    
    #После проигрыша игра не закрывается, а предлагает повторить попытку, либо просто выйти
    while check:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                check = False
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_r:
                    game()
                if action.key == pygame.K_q:
                    check = False
        monitor.fill(white)
        
        monitor.blit(score_font.render('Press R for restart or Q for quit' , True, black), (35,200))

        pygame.display.update()
game()
pygame.quit()












