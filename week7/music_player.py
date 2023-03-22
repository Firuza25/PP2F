import pygame
import os

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("music_player")
icon = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/IMAGE 2023-03-22 23_12_16.png')

music_folder = "/Users/firuza/Desktop/PP2/week7/music"
music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith('.mp3')]
queue = []
for i in music_files:
    queue.append(i)

song = 0
pygame.mixer.music.load(music_files[song])
pygame.mixer.music.play()

play_button = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/play_button.png')
pause_button = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/pause.png')
next_button = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/next.png')
previous_button = pygame.image.load('/Users/firuza/Desktop/PP2/week7/images/previous.png')

clock = pygame.time.Clock()

playing_mode = True
flPause = False
temp = pause_button

running = True
while running:

    screen.blit(background, (0, 0))

    screen.blit(previous_button, (200, 300))
    screen.blit(pause_button, (275, 300))
    screen.blit(next_button, (350, 300))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                    pause_button = play_button
                else:
                    pygame.mixer.music.unpause()
                    pause_button = temp
            elif event.key == pygame.K_a:
                pygame.mixer.music.stop()
                song += 1
                pygame.mixer.music.load(music_files[song])
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                song -= 1
                pygame.mixer.music.load(music_files[song])
                pygame.mixer.music.play()

        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(60)




