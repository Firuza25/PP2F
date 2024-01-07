import pygame

pygame.init()

# Set up the window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Define the quiz questions and answers
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest country in the world?", "answer": "Russia"},
    {"question": "What is the tallest mammal?", "answer": "Giraffe"}
]

# Define some variables for tracking the current question and user input
current_question_index = 0
user_input = ""

# Define a function for checking the user's answer and advancing to the next question
def check_answer():
    global current_question_index, user_input

    # Get the current question and answer
    current_question = quiz_questions[current_question_index]
    correct_answer = current_question["answer"]

    # Check the user's answer and display the result
    if user_input == correct_answer:
        result_text = "Correct!"
    else:
        result_text = "Incorrect. The correct answer was " + correct_answer
    result_rendered = font.render(result_text, True, (0, 0, 0))
    screen.blit(result_rendered, (50, 150))

    # Advance to the next question
    current_question_index += 1
    if current_question_index < len(quiz_questions):
        pygame.display.flip()
        pygame.time.delay(1000)
        user_input = ""
    else:
        pygame.display.flip()
        pygame.time.delay(3000)
        pygame.quit()
        quit()

# Main game loop
while True:
    # Clear the screen and display the current question
    screen.fill((255, 255, 255))
    current_question = quiz_questions[current_question_index]
    question_rendered = font.render(current_question["question"], True, (0, 0, 0))
    screen.blit(question_rendered, (50, 50))

    # Display the user's input
    user_input_rendered = font.render(user_input, True, (0, 0, 0))
    screen.blit(user_input_rendered, (50, 100))

    # Update the display
    pygame.display.flip()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            elif event.key == pygame.K_RETURN:
                check_answer()
            else:
                user_input += event.unicode

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
