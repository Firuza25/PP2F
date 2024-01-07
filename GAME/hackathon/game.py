import pygame
import button
import time,random
from text import InputBox
from player import *
from map import world
pygame.init()   

clock = pygame.time.Clock()
#game screen and menu screen indicators
SCENE_GAME = 0
SCENE_MENU = 1

W, H = 800, 800
# pixels per block in map
cell = 40

nums = []
while len(nums)!=5:
    i = random.randint(0,9)
    if i not in nums:
        nums.append(i)


#files for design
water = pygame.transform.scale(
    pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/water.png'), (40, 120))
glass = pygame.transform.scale(
    pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/glass.png'), (320, 320))
bg = pygame.transform.scale(pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/b.jpg'), (800, 800))
blocks = pygame.transform.scale(
    pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/metal.png'), (40, 40))


points = [] #contains right answers length = num of right answers
pipes = [] #images of water pipes
def pipe():
    for i in range(1, 8):
        pip = pygame.transform.scale(pygame.image.load(
            f'/Users/firuza/Desktop/PP2/GAME/hackathon/resources/pipe{i}.png'), (120, 120))
        pipes.append(pip)
    return pipes

# question files
i1 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image1.png'), (800, 500))
i2 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image2.png'), (800, 500))
i3 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image3.png'), (800, 500))
i4 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image4.png'), (800, 500))
i5 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image5.png'), (800, 500))
i6 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image6.png'), (800, 500))
i7 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image7.png'), (800, 500))
i8 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image8.png'), (800, 500))
i9 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image9.jpg'), (800, 500))
i10 = pygame.transform.scale(pygame.image.load(
    '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/image10.jpg'), (800, 500))
#boxes for input text
input_box1 = InputBox(200, 600, 200, 80)
input_box2 = InputBox(200, 600, 200, 80)
input_box3 = InputBox(200, 600, 200, 80)
input_box4 = InputBox(200, 600, 200, 80)
input_box5 = InputBox(200, 600, 200, 80)
input_box6 = InputBox(200, 600, 200, 80)
input_box7 = InputBox(200, 600, 200, 80)
input_box8 = InputBox(200, 600, 200, 80)
input_box9 = InputBox(200, 600, 200, 80)
input_box10 = InputBox(200, 600, 200, 80)
in_boxes = [input_box1, input_box2, input_box3, input_box4, input_box5,input_box6,input_box7,
            input_box8,input_box9,input_box10] #list of input boxes
answers = ['CONTRADICTION', 'MATPLOTLIB','CRYPTOGRAPHY', 'GAME OF THRONES', 'COPERNICUS',
           'UNICODE','TRIGONOMETRY','MARATHON','DEVELOPER','PYGAME'] #answers for chiphers
images = [i1, i2, i3, i4, i5,i6,i7,i8,i9,i10] 
#texts and fonts for game
FONT2 = pygame.font.SysFont('Consolas', 30)
FONT = pygame.font.SysFont('Consolas', 40)#timer font
font = pygame.font.SysFont('Consolas', 60)#ponts font

timer_text = FONT.render("00:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(700, 30))

game_over = font.render("GAME OVER", True, 'black')
win = font.render("MISSION COMPLETED", True, 'black')
caution = FONT2.render("Write with CAPS", True, 'grey3')
def menu(window):
    music = pygame.mixer.music.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/music2.mp3')

# установка громкости музыки
    pygame.mixer.music.set_volume(0.5)

# проигрывание музыки
    pygame.mixer.music.play(-1)

# game variables
    game_paused = False
    menu_state = "main"

# define fonts
    font = pygame.font.SysFont("arialblack", 70)

# define colours
    TEXT_COL = (255, 0, 0)

# load button images
    play_img = pygame.image.load("/Users/firuza/Desktop/PP2/GAME/hackathon/resources/play.png").convert_alpha()
    rules_img = pygame.image.load("/Users/firuza/Desktop/PP2/GAME/hackathon/resources/game_rules.png").convert_alpha()
    quit_img = pygame.image.load("/Users/firuza/Desktop/PP2/GAME/hackathon/resources/quit.png").convert_alpha()
    back_img = pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/back.png').convert_alpha()
    rule_list_img = pygame.image.load("/Users/firuza/Desktop/PP2/GAME/hackathon/resources/ere.png").convert_alpha()

# create button instances
    resume_button = button.Button(270, 125, play_img, 1)
    rules_button = button.Button(265, 250, rules_img, 1.03)
    quit_button = button.Button(270, 375, quit_img, 1)
    rule_button = button.Button(50, 5, rule_list_img, 1)
    back_button = button.Button(535, 350, back_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        window.blit(img, (x, y))
# game loop
    run = True

    while run:
        background_image = pygame.transform.scale(pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/bg.jpg'),(800,800))
        window.blit(background_image, (0, 0))

  # check if game is paused
        if game_paused == True:
        # check menu state
            if menu_state == "main":
          # draw pause window buttons
                if resume_button.draw(window):
                    menu_state = "play"
                if rules_button.draw(window):
                    menu_state = "rules"
                if quit_button.draw(window):
                    quit()

    # check if the options menu is open
            if menu_state == "rules":

          # draw the different options buttons
                if rule_button.draw(window):  

                    print("любое слово")
                back = pygame.transform.scale(pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/bg.jpg'),(800,800))
                rule = pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/ere.png')
                window.blit(back, (0, 0))
                window.blit(rule, (30, 100))

                if back_button.draw(window):
                    menu_state = "main"
 
            if menu_state == "play":
                if resume_button.draw(window):
                    print("play start")

                    return SCENE_GAME

        else:
            draw_text("DEADPOOL", font, TEXT_COL, 200, 350)

  # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
                 
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()


def q1(window, i, current_seconds): #function which opens the i-th question, 
                                    #checks the i-th answer in i-th text box in a new screen 
    play = True
    FPS = 60
    clock = pygame.time.Clock()
    while play:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.USEREVENT: # timer 
                current_seconds -= 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# press esc to go again to the main game-screen
                    play = False
                    game(window,current_seconds)
                    
              
            in_boxes[i].handle_event(event, answers[i], points)  #properties of a function are written in module "text.py"
            in_boxes[i].update()
            surf = font.render(str(len(points)), True, pygame.Color('white')) # points visualizer
            window.blit(surf, (740, 0)) #properties of a function are written in module "text.py"
            
            window.fill((255, 255, 255)) 
            
            window.blit(images[i], (0, 0)) #adding question images to the q1 screen
            
            in_boxes[i].draw(window) #properties of a function are written in module "text.py"
            window.blit(caution, (200,550))
        if current_seconds >= 0: #checks the time and shows it on the q1 screen
            display_seconds = current_seconds % 60
            display_minutes = int(current_seconds / 60) % 60
        timer_text = FONT.render(
            f"{display_minutes:02}:{display_seconds:02}", True, "white")
        window.blit(timer_text, timer_text_rect)
            
        if current_seconds == 0: #checks if the time is out and returns GAMEOVER-SCREEN
            window.fill('red')
            window.blit(game_over, (235, 320))
            play =False
            game(window,current_seconds)
            
            
        if len(points) ==5 and current_seconds!=0: #checks if gamer solved all questions and have extra time 
                window.fill('paleturquoise1')      #and returns WIN-SCREEN
                window.blit(win, (60, 320))
                play =False
                game(window,current_seconds)
                
        
        pygame.display.flip()



#timer setting 
pygame.time.set_timer(pygame.USEREVENT, 1000)
POMODORO_LENGTH = 120  # 
current_seconds = POMODORO_LENGTH


def game(window, current_seconds): #main game screen
    FPS = 60
    clock = pygame.time.Clock()
    player = Object(600, 450, '/Users/firuza/Desktop/PP2/GAME/hackathon/resources/1.png')
    play = True
    
    
    while play:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.USEREVENT: #timer 
                    current_seconds -= 1
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  #replay/go to the menu
                        play = False                    #impossible to stop the game because it will let gamers to cheat
                        return SCENE_MENU

            # bg
            window.blit(bg, (0,0))
            
            # player
            player.update()
            window.blit(player.image, player.rect)
            waterlevel = 320
            # pool
            window.blit(water, (445,640))
            window.blit(water,(283,40))
            window.blit(pygame.transform.rotate(water,90),(40,245))
            window.blit(pygame.transform.rotate(water,90),(40,485))
            s = pygame.Surface((320, waterlevel))
            s.set_alpha(50)
            s.fill(pygame.Color('blue'))
            window.blit(s, (240, 240))
            window.blit(glass, (240,240))

            # pipes
            pipes = pipe()
            pipe3 = window.blit(pipes[3], (420,640))
            pipe0 = window.blit(pipes[0], (460,40))
            pipe4 = window.blit(pipes[4], (350,40))
            pipe1 = window.blit(pipes[1], (40,460))
            pipe2 = window.blit(pipes[2], (40,220))
            pipe7 = window.blit(pygame.transform.rotate(pipes[1], 90),(260,40))
            pipe5 = window.blit(pipes[5],(640,420))
            pipe6 = window.blit(pipes[6],(640,300))

            # questions
            pos = pygame.mouse.get_pos()
            
            if len(points) !=5 and current_seconds!=0: # allows functions only when some questions still unsolved 
                if pipe0.collidepoint(pos) or pipe4.collidepoint(pos):  #if the first pipe clicked switches to the q1 screen
                    if pygame.mouse.get_pressed()[0]:
                        q1(window, nums[0],current_seconds)
                elif pipe7.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0]:
                        q1(window, nums[1],current_seconds)
                elif pipe2.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0]:
                        q1(window, nums[2],current_seconds)
                elif pipe1.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0]:
                        q1(window, nums[3],current_seconds)
                elif pipe3.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0]:
                        q1(window, nums[4],current_seconds)

            # map
            for i in range(len(world)):
                for j in range(len(world[i])):
                    x, y = j*cell,i*cell

                    if world[i][j] == 'B':        #replaces "B" string with blocks(map is in module "map.py")
                        window.blit(blocks, (x, y))

            #points streaming
            surf = font.render(str(len(points)), True, pygame.Color('white'))
            window.blit(surf, (0,0))


            if current_seconds >= 0: #checks the time and shows it on the q1 screen
                display_seconds = current_seconds % 60
                display_minutes = int(current_seconds / 60) % 60
            timer_text = FONT.render(
                f"{display_minutes:02}:{display_seconds:02}", True, "white")
            window.blit(timer_text, timer_text_rect)
                
            if current_seconds == 0: #checks if the time is out and returns GAMEOVER-SCREEN
                window.fill('red')
                window.blit(game_over, (235, 320))
                
                play = False
            elif len(points) == 5 and current_seconds!=0: #checks if gamer solved all questions and have extra time
                
                window.fill('paleturquoise1')               #and returns WIN-SCREEN
                window.blit(win, (100, 320))
                
                play = False
            pygame.display.update()
    time.sleep(3)
    quit()    
  


def main():    #controls the switch of two screens 
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("DEADPOOL")
    
    pygame.display.set_icon(pygame.image.load('/Users/firuza/Desktop/PP2/GAME/hackathon/resources/icon.jpg'))
    play = True
    scene = SCENE_MENU

    while play:

        if scene == SCENE_GAME:
            scene = game(window, current_seconds)
        
        elif scene == SCENE_MENU:
            scene = menu(window)

main()