import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Dice")

# Load background image
background = pygame.image.load("background.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load dice face images (for display & selection)
raw_faces = {
    "rock": pygame.image.load("rock.png"),
    "paper": pygame.image.load("paper.png"),
    "scissors": pygame.image.load("scissors.png")
}

# Resize
dice_faces = {}
for key in raw_faces:
    dice_faces[key] = pygame.transform.scale(raw_faces[key], (100, 100))

# Load sound
roll_sound = pygame.mixer.Sound("dice_roll.wav")
roll_sound.set_volume(1.0)  # Range is 0.0 (mute) to 1.0 (max)

# Fonts
font = pygame.font.SysFont("Arial", 28)

# Moves
moves = ["rock", "paper", "scissors"]

# Image positions (clickable)
selector_rects = {}
start_x = 50
spacing = 150
y_pos = 450

for i, move in enumerate(moves):
    rect = pygame.Rect(start_x + i * spacing, y_pos, 100, 100)
    selector_rects[move] = rect

# Function to draw text
def draw_text(text, y, color=(255, 255, 255), size=28):
    label = pygame.font.SysFont("Arial", size).render(text, True, color)
    rect = label.get_rect(center=(WIDTH // 2, y))
    screen.blit(label, rect)

# Result logic
def show_result(user, computer):
    if user == computer:
        return "🤝 It's a Tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "🎉 You Win!"
    else:
        return "😢 You Lose."

# Game loop
running = True
clock = pygame.time.Clock()
user_choice = None
computer_choice = None
rolling = False
roll_start_time = 0
ROLL_DURATION = 3
result_text = ""

while running:
    screen.blit(background, (0, 0))

    draw_text("Choose your move!", 50)

    # Draw clickable images
    for move in moves:
        screen.blit(dice_faces[move], selector_rects[move].topleft)
        label = font.render(move.capitalize(), True, (255, 255, 255))
        label_rect = label.get_rect(center=(selector_rects[move].centerx, selector_rects[move].bottom + 15))
        screen.blit(label, label_rect)

    # Dice rolling animation
    if rolling:
        if time.time() - roll_start_time < ROLL_DURATION:
            temp_face = random.choice(moves)
            temp_image = pygame.transform.scale(raw_faces[temp_face], (200, 200))
            screen.blit(temp_image, (150, 150))
        else:
            rolling = False
            final_image = pygame.transform.scale(raw_faces[computer_choice], (200, 200))
            screen.blit(final_image, (150, 150))
            draw_text(f"You: {user_choice} vs Computer: {computer_choice}", 360)
            draw_text(result_text, 410, (0, 255, 0) if "Win" in result_text else (255, 100, 100))

    elif computer_choice:
        final_image = pygame.transform.scale(raw_faces[computer_choice], (200, 200))
        screen.blit(final_image, (150, 150))
        draw_text(f"You: {user_choice} vs Computer: {computer_choice}", 360)
        draw_text(result_text, 410, (0, 255, 0) if "Win" in result_text else (255, 100, 100))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect image clicks
        if event.type == pygame.MOUSEBUTTONDOWN and not rolling:
            for move, rect in selector_rects.items():
                if rect.collidepoint(event.pos):
                    user_choice = move
                    computer_choice = random.choice(moves)
                    result_text = show_result(user_choice, computer_choice)
                    roll_sound.play()
                    rolling = True
                    roll_start_time = time.time()

    clock.tick(60)

pygame.quit()
