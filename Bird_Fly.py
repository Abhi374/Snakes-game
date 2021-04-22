author = "Abhishek Dubey"

import pygame
import random
import os

pygame.mixer.init()

pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pink = (233, 188, 213, 250)


# Creating window

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# background images
bgimg = pygame.image.load('snake1.jpg')
bgimg = pygame.transform.scale(bgimg, [screen_width, screen_height]).convert_alpha()


# Game Title
pygame.display.set_caption("Snack with abhishek")
pygame.display.update()
font = pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()


def Text_Screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x, y))


def plot_snack(gameWindow, color, snk_list, snake_size):
    # print(snk_list)
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((255, 150, 80)) #233, 188, 213, 250 pink color
        Text_Screen("Welcome to Snacks   ", black, 250, 230)
        Text_Screen("Press Space bar to Play ", red, 220, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    pygame.mixer.music.load('back.mp3.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)
# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    init_velocity = 5
    snk_list = []
    snack_lenght = 1
    # check if hiscore file exits or not
    if(not os.path.exists("high_score.txt")):
        with open("high_score.txt", "w") as f:
            f.write("0")

    with open("high_score.txt", "r") as f:
        hiScore = f.read()

    velocity_y = 0
    snake_size = 30
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    fps = 60

    while not exit_game:

        if game_over:
            with open("high_score.txt", "w") as f:
                f.write(str(hiScore))

            gameWindow.fill(pink)
            Text_Screen("Game over : press Enter to Continue", red, 100, 230)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10




            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 8 and abs(snake_y - food_y) < 8:
                score += 10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snack_lenght += 5
                if score>int (hiScore):
                    hiScore = score
            gameWindow.fill((100,73,60))
            gameWindow.blit(bgimg, (0, 0))
            Text_Screen("Score: " + str(score) + "  Hiscore :  "+str(hiScore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snack_lenght:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()

            if snake_x <= 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('game_over.mp3.mp3')
                pygame.mixer.music.play()

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snack(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


Welcome()
