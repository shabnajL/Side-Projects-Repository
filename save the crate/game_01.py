import pygame
import random
import sys
import time
pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

pygame.init()

WIDTH = 800
HEIGHT = 600
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
NAVY = (0, 0, 128)
BACKGROUND = (0, 0, 0)


enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

player_size = 50
player_pos = [WIDTH / 2, HEIGHT - 2 * player_size]
enemy_list = [enemy_pos]

SPEED = 10
score = 0
#to read the high score
with open("high_score.txt", "r") as f:
    high_score = f.read()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bck_img = pygame.image.load("box2.png")

game_over = False

clock = pygame.time.Clock()

pygame.display.set_caption('Save The Crate')

MyFont = pygame.font.SysFont("monospace", 35)
MyFont1 = pygame.font.SysFont("Helvetica", 50, 1) #for_making_text_bold:1

#for_playing_background_music
pygame.mixer.music.load("Jeremy_Zucker_comethru.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

def level(score, SPEED):
    if score < 20:
        SPEED = 6
    elif score < 50:
        SPEED = 10
    elif score < 80:
        SPEED = 15
    elif score < 100:
        SPEED = 17
    else:
        SPEED = 20
    return SPEED


def drop_box(enemy_list):
    delay = random.random()
    # 10 blocks dropping at the same time
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_box(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, PURPLE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_position(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        # checks whether the box is on screen
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            # checks whether the box fall off screen
            score += 1
            enemy_list.pop(idx)

    return score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_enemy(player_pos, enemy_pos):
            return True
    return False


def detect_enemy(player_pos, enemy_pos):
    p_X = player_pos[0]
    p_Y = player_pos[1]

    e_X = enemy_pos[0]
    e_Y = enemy_pos[1]

    if (e_X >= p_X and e_X < (p_X + player_size)) or (p_X >= e_X and p_X < (e_X + enemy_size)):
        if (e_Y >= p_Y and e_Y < (p_Y + player_size)) or (p_Y >= e_Y and p_Y < (e_Y + enemy_size)):
            return True

    return False

while not game_over:
    for event in pygame.event.get():

        # this line allows to come out game by using cross button
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:

            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size


            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]

    # as the box moves,the previous block bcmes black

    screen.fill(BACKGROUND)

    drop_box(enemy_list)

    score = update_position(enemy_list, score)
    if score > int(high_score):
        high_score = score

    SPEED = level(score, SPEED)

    # to display score on screen

    text = "Score:" + str(score)
    label = MyFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH - 210, 0))

    if collision_check(enemy_list, player_pos):
        game_over = True

        screen.fill(WHITE)
        screen.blit(bck_img, (0, 0))
        text1 = "High Score:" + str(high_score)
        label = MyFont1.render(text1, 1, NAVY)
        screen.blit(label, (300, 220))
        end_text = " Game Over! "
        label1 = MyFont1.render(end_text, 1, GREEN)
        screen.blit(label1, (300, 270))
        pygame.display.update()
        time.sleep(3)

        #updating the high score
        with open("high_score.txt", "w") as f:
            f.write(str(high_score))

        print("\nYour SCORE : " + str(score))
        print("\nHigh Score : " + str(high_score))
        if score >= int(high_score):
            print("Congo! New high score!")
        else:
            print("Better luck next time.")

        break


    draw_box(enemy_list)

    # player
    pygame.draw.rect(screen, ORANGE, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    # display the rect
    pygame.display.update()
