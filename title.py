import pygame
x = pygame.init()

# Creating Window
gameWindow = pygame.display.set_mode((1200, 500))
pygame.display.set_caption("My First Game")

# Spacific Variables
exit_game = False
game_over = False

# Creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have passed Right arrow key")


pygame.quit()
quit()


