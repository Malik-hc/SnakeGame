import pygame 
pygame.init()

snake_color = (102, 255, 102)
screen_color = (0,0,0)

x = 300
y = 300
x_movement = 0
y_movement = 0

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("SNAKE")

game_over = False

while not game_over: #Allows for game to stay open
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If quit button is pressed, game is over
            game_over = True
        
        if event.type == pygame.KEYDOWN: #If a key is pressed snake will move int hat direction
            if event.key == pygame.K_UP:
                x_movement = 0
                y_movement = -10
            elif event.key == pygame.K_DOWN:
                x_movement = 0
                y_movement = 10
            elif event.key == pygame.K_LEFT:
                x_movement = -10
                y_movement = 0
            elif event.key == pygame.K_RIGHT:
                x_movement = 10
                y_movement = 0

    x += x_movement #Applying the change made by the event to the snake
    y += y_movement

    screen.fill(screen_color)

    pygame.draw.rect(screen, snake_color, [x,y,10,10]) #Creates one block of the snake, at position of x and y

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()