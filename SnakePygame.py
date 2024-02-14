import pygame 
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("SNAKE")

snake_color = (102, 255, 102)
game_over = False

while not game_over: #Allows for game to stay open
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(screen, snake_color,[200,150,10,10])
    pygame.display.update()

pygame.quit()
quit()