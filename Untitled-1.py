import pygame
import sys
import random

# initialize pygame
pygame.init()

# set window size
window_size = (400, 400)

# create the window
screen = pygame.display.set_mode(window_size)

# set title
pygame.display.set_caption("Snake Game")

# clock to control game speed
clock = pygame.time.Clock()

# set block size
block_size = 10

# set font for displaying score
font = pygame.font.Font(None, 25)

# set initial position of the snake
snake_position = [100, 100]

# set initial snake body
snake_body = [    [100, 100],
    [90, 100],
    [80, 100]
]

# initialize food position
food_position = [random.randrange(1, (window_size[0] // block_size)) * block_size,
                 random.randrange(1, (window_size[1] // block_size)) * block_size]
food_spawn = True

# initialize direction
direction = 'RIGHT'
change_to = direction

# initialize score
score = 0

# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 30)
    game_over_surface = my_font.render('Your Score is: ' + str(score), True, (255, 255, 255))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_size[0] / 2, window_size[1] / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # update snake position
    if direction == 'UP':
        snake_position[1] -= block_size
    if direction == 'DOWN':
        snake_position[1] += block_size
    if direction == 'LEFT':
        snake_position[0] -= block_size
    if direction == 'RIGHT':
        snake_position[0] += block_size

    # snake body mechanics
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawn = False
        score += 10
    else:
        snake_body.pop()
        
    if not food_spawn:
        food_position = [random.randrange(1, (window_size[0] // block_size)) * block_size,
                         random.randrange(1, (window_size[1] // block_size)) * block_size]
        food_spawn = True

    # background color
    screen.fill((0, 0, 0))
    
    # draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], block_size, block_size))
        
    # draw food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], block_size, block_size))
    
    # check if hit the boundaries
    if snake_position[0] < 0 or snake_position[0] > window_size[0] - block_size:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_size[1] - block_size:
        game_over()
    
    # check for collision with the body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    
    # display score
    score_surface = font.render('Score: ' + str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect.topleft = (window_size[0] - 120, 10)
    screen.blit(score_surface, score_rect)
    
    # refresh screen
    pygame.display.update()
    
    # set clock speed
    clock.tick(20)