import pygame
import random

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 480

# Set the font
FONT = pygame.font.Font(None, 32)

# Set the game clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = "right"

    def move(self):
        if self.direction == "right":
            new_head = (self.body[0][0] + 20, self.body[0][1])
        elif self.direction == "left":
            new_head = (self.body[0][0] - 20, self.body[0][1])
        elif self.direction == "up":
            new_head = (self.body[0][0], self.body[0][1] - 20)
        elif self.direction == "down":
            new_head = (self.body[0][0], self.body[0][1] + 20)

        self.body.insert(0, new_head)
        self.body.pop()

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, GREEN, (x, y, 20, 20))

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"

# Define the Food class
class Food:
    def __init__(self):
        self.x = random.randrange(0, SCREEN_WIDTH - 20, 20)
        self.y = random.randrange(0, SCREEN_HEIGHT - 20, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.x, self.y, 20, 20))

    def respawn(self):
        self.x = random.randrange(0, SCREEN_WIDTH - 20, 20)
        self.y = random.randrange(0, SCREEN_HEIGHT - 20, 20)

# Define the main menu function
def main_menu(screen):
    # Set the background color
    screen.fill(WHITE)

    # Draw the title
    title_text = FONT.render("Snake", True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(title_text, title_rect)

    # Draw the name input box
    name_input_text = FONT.render("Enter your name:", True, BLACK)
    name_input_rect = name_input_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(name_input_text, name_input_rect)

    # Create a text input box for the name
    name = ""
    name_input_box = pygame.Rect(SCREEN_WIDTH/2 - 75, SCREEN_HEIGHT/2 + 10, 150, 30)
    name_input_active = False

    # Start the game loop
