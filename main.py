import pygame
import sys

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Аламан Бәйге')
bg_image = pygame.image.load('images/bg_image.png')
bg_x = 0
finish = pygame.image.load('images/finish.png').convert_alpha()
game_start = False
bg_sound = pygame.mixer.Sound('music/bg_music.mp3')
bg_sound.play()

red_jockey_count = 0
red_jokey = pygame.image.load('images/red_jockey/k_1.png')
red_jockey_list = [
    pygame.image.load('images/red_jockey/k_1.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_2.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_3.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_4.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_5.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_6.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_7.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_8.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_9.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_10.png').convert_alpha(),
    pygame.image.load('images/red_jockey/k_11.png').convert_alpha(),
]
red_jokey_x = -20
red_jockey_speed = 1.6

blue_jockey_count = 0
blue_jockey = pygame.image.load('images/blue_jockey/b_1.png')
blue_jockey_list = [
    pygame.image.load('images/blue_jockey/b_1.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_2.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_3.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_4.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_5.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_6.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_7.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_8.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_9.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_10.png').convert_alpha(),
    pygame.image.load('images/blue_jockey/b_11.png').convert_alpha(),
]
blue_jokey_x = -20
blue_jockey_speed = 1

green_jockey_count = 0
green_jockey = pygame.image.load('images/green_jockey/g_1.png')
green_jockey_list = [
    pygame.image.load('images/green_jockey/g_1.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_2.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_3.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_4.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_5.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_6.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_7.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_8.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_9.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_10.png').convert_alpha(),
    pygame.image.load('images/green_jockey/g_11.png').convert_alpha(),
]
green_jockey_x = -20
green_jockey_speed = 1.3


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg_image, (bg_x, 0))
    screen.blit(finish, (1000, 550))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        game_start = True
        red_jokey_x += red_jockey_speed
        screen.blit(red_jockey_list[red_jockey_count], (red_jokey_x, 400))
        if red_jockey_count == 9:
            red_jockey_count = 1
        else:
            red_jockey_count += 1
    else:
        screen.blit(red_jockey_list[0], (red_jokey_x, 400))

    if game_start:
        blue_jokey_x += blue_jockey_speed
        screen.blit(blue_jockey_list[blue_jockey_count], (blue_jokey_x, 500))
        if blue_jockey_count == 9:
            blue_jockey_count = 1
        else:
            blue_jockey_count += 1
    else:
        screen.blit(blue_jockey_list[0], (blue_jokey_x, 500))

    if game_start:
        green_jockey_x += green_jockey_speed
        screen.blit(green_jockey_list[green_jockey_count], (green_jockey_x, 600))
        if green_jockey_count == 9:
            green_jockey_count = 1
        else:
            green_jockey_count += 1
    else:
        screen.blit(green_jockey_list[0], (green_jockey_x, 600))

    pygame.display.update()
    clock.tick(20)
