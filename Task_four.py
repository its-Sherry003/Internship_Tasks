#Task 4: Snake Game

import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
DARK_GREEN = (0, 100, 0)

# Snake settings
snake_block = 20
snake_speed_initial = 10

# Clock to control game speed
clock = pygame.time.Clock()

# Fonts
font_small = pygame.font.SysFont("Arial", 25)
font_medium = pygame.font.SysFont("Arial", 35)
font_large = pygame.font.SysFont("Arial", 50)

# Functions to draw game elements
def draw_snake(snake_list):
    for i, segment in enumerate(snake_list):
        # Drawing head with a different color
        if i == 0:
            pygame.draw.rect(screen, DARK_GREEN, [segment[0], segment[1], snake_block, snake_block])
        else:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])
            
        # Adding eyes to the head
        if i == 0:
            # Determining direction for eye placement
            if len(snake_list) > 1:
                prev_segment = snake_list[1]
                if segment[0] < prev_segment[0]:  # Moving right
                    pygame.draw.circle(screen, WHITE, (segment[0] + snake_block - 5, segment[1] + 5), 3)
                    pygame.draw.circle(screen, WHITE, (segment[0] + snake_block - 5, segment[1] + snake_block - 5), 3)
                elif segment[0] > prev_segment[0]:  # Moving left
                    pygame.draw.circle(screen, WHITE, (segment[0] + 5, segment[1] + 5), 3)
                    pygame.draw.circle(screen, WHITE, (segment[0] + 5, segment[1] + snake_block - 5), 3)
                elif segment[1] < prev_segment[1]:  # Moving down
                    pygame.draw.circle(screen, WHITE, (segment[0] + 5, segment[1] + snake_block - 5), 3)
                    pygame.draw.circle(screen, WHITE, (segment[0] + snake_block - 5, segment[1] + snake_block - 5), 3)
                elif segment[1] > prev_segment[1]:  # Moving up
                    pygame.draw.circle(screen, WHITE, (segment[0] + 5, segment[1] + 5), 3)
                    pygame.draw.circle(screen, WHITE, (segment[0] + snake_block - 5, segment[1] + 5), 3)

def draw_food(food_position):
    pygame.draw.rect(screen, RED, [food_position[0], food_position[1], snake_block, snake_block])
    # Adding a highlight to make food more appealing
    pygame.draw.rect(screen, WHITE, [food_position[0] + snake_block//4, food_position[1] + snake_block//4, 
                                     snake_block//2, snake_block//2])

def draw_score(score, high_score):
    value = font_small.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])
    high_score_text = font_small.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(high_score_text, [10, 40])

def place_food(snake_list):
    """It will place food at a random position not occupied by the snake"""
    while True:
        food_x = round(random.randrange(0, WIDTH - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, HEIGHT - snake_block) / snake_block) * snake_block
        food_position = (food_x, food_y)
        
        # Checking if food position overlaps with snake
        if food_position not in snake_list:
            return food_position

def move_snake(snake_list, direction):
    head_x, head_y = snake_list[0]
    if direction == "UP":
        head_y -= snake_block
    elif direction == "DOWN":
        head_y += snake_block
    elif direction == "LEFT":
        head_x -= snake_block
    elif direction == "RIGHT":
        head_x += snake_block
        
    # Adding new head position
    new_head = (head_x, head_y)
    snake_list.insert(0, new_head)
    
    return snake_list

def check_collision(snake_list):
    head_x, head_y = snake_list[0]
    
    # Checking wall collision
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True
        
    # Checking self collision
    if snake_list[0] in snake_list[1:]:
        return True
        
    return False

def show_menu(high_score):
    menu_running = True
    selected = 0  # 0: Easy, 1: Medium, 2: Hard
    options = [
        {"text": "Easy", "speed": 8},
        {"text": "Medium", "speed": 12},
        {"text": "Hard", "speed": 15}
    ]
    
    while menu_running:
        screen.fill(BLACK)
        
        # Drawing the title
        title = font_large.render("Snake Game", True, WHITE)
        screen.blit(title, [WIDTH//2 - title.get_width()//2, HEIGHT//4])
        
        # Drawing high score
        if high_score > 0:
            high_score_text = font_medium.render(f"High Score: {high_score}", True, WHITE)
            screen.blit(high_score_text, [WIDTH//2 - high_score_text.get_width()//2, HEIGHT//4 + 60])
        
        # Drawing options
        for i, option in enumerate(options):
            color = BLUE if i == selected else WHITE
            option_text = font_medium.render(f"{i+1}. {option['text']}", True, color)
            screen.blit(option_text, [WIDTH//2 - option_text.get_width()//2, HEIGHT//2 + i * 50])
        
        # Drawing instructions
        instructions = font_small.render("Use arrow keys to navigate and ENTER to select", True, WHITE)
        screen.blit(instructions, [WIDTH//2 - instructions.get_width()//2, HEIGHT - 100])
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]["speed"]
                elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    return options[int(event.key) - pygame.K_1]["speed"]
    
    return options[0]["speed"]  # Default return

def show_game_over(score, high_score):
    screen.fill(BLACK)
    
    game_over_text = font_large.render("Game Over!", True, RED)
    screen.blit(game_over_text, [WIDTH//2 - game_over_text.get_width()//2, HEIGHT//3])
    
    score_text = font_medium.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [WIDTH//2 - score_text.get_width()//2, HEIGHT//2])
    
    if score == high_score and score > 0:
        new_high_text = font_medium.render("New High Score!", True, GREEN)
        screen.blit(new_high_text, [WIDTH//2 - new_high_text.get_width()//2, HEIGHT//2 + 40])
    
    restart_text = font_small.render("Press P to play again or Q to quit", True, WHITE)
    screen.blit(restart_text, [WIDTH//2 - restart_text.get_width()//2, HEIGHT - 100])
    
    pygame.display.update()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return False
                if event.key == pygame.K_p:
                    return True

# Main game loop
def game_loop():
    high_score = 0
    
    while True:
        snake_speed = show_menu(high_score)
        
        # Initializing game state
        snake = [(100, 100), (80, 100), (60, 100)]
        snake_direction = "RIGHT"
        food_position = place_food(snake)
        score = 0
        game_over = False
        snake_growth = False
        
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                        snake_direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                        snake_direction = "RIGHT"
                    elif event.key == pygame.K_UP and snake_direction != "DOWN":
                        snake_direction = "UP"
                    elif event.key == pygame.K_DOWN and snake_direction != "UP":
                        snake_direction = "DOWN"
                    elif event.key == pygame.K_ESCAPE:
                        game_over = True
            
            snake = move_snake(snake, snake_direction)
            
            # Checking if snake ate food
            if snake[0] == food_position:
                food_position = place_food(snake)
                score += 1
                snake_growth = True
                
                # Updating high score
                if score > high_score:
                    high_score = score
                
                # Increasing speed every 5 pieces
                if score % 5 == 0:
                    snake_speed += 1
            
            # Removing tail if not growing
            if not snake_growth:
                snake.pop()
            else:
                snake_growth = False
            
            # Checking for collisions
            if check_collision(snake):
                game_over = True
            
            # Drawing everything
            screen.fill(BLACK)
            draw_snake(snake)
            draw_food(food_position)
            draw_score(score, high_score)
            
            pygame.display.update()
            clock.tick(snake_speed)
        
        # Game over
        if not show_game_over(score, high_score):
            break

# Run game
game_loop()
pygame.quit()
quit()

