from turtle import speed
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1295,745 
GROUND_HEIGHT = HEIGHT - 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (250, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Game")
clock = pygame.time.Clock()
# Load background image
background_img = pygame.image.load("background02.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT)) 
 # Resize to fit screen


# Load player image
player_img = pygame.image.load("player.png")  

# Make sure the image is in the same directory
player_size = 200
player_img = pygame.transform.scale(player_img, (player_size, player_size))  

# Resize image
player_x = 50
player_y = GROUND_HEIGHT - player_size
player_velocity = 30
gravity = 1.90
jump_strength = -25
is_jumping = False

# Obstacle settings
obstacle_img = pygame.image.load("obstacle.png")
obstacle_width = 100
obstacle_hight = 90 

# Make sure the image is in the same directory
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_hight))  
obstacle_x = WIDTH
obstacle_y = GROUND_HEIGHT - obstacle_hight
obstacle_speed = 20
obstacle_speed +=20

# Score
score = 0
font = pygame.font.Font(None, 100)

# Game loop
running = True
while running:
    screen.blit(background_img,(0,0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                player_velocity = jump_strength
                is_jumping = True

    # Player movement
    player_velocity += gravity
    player_y += player_velocity

    if player_y >= GROUND_HEIGHT - player_size:
        player_y = GROUND_HEIGHT - player_size
        is_jumping = False

    # Obstacle movement
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        score += 10

    # Collision detection
    if (
        player_x < obstacle_x + obstacle_width
        and player_x + player_size > obstacle_x
        and player_y + player_size > obstacle_y
    ):
        print("Game Over! Final Score:", score)
        running = False

    # Draw elements
    screen.blit(player_img, (player_x, player_y)) 
     # Draw player image
    screen.blit(obstacle_img,( obstacle_x, obstacle_y)) 
     # Draw obstacle image
    
    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (500, 50))

    # Update screen
    pygame.display.update()
    clock.tick(30)

pygame.quit()