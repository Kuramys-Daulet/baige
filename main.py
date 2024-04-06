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

text_font = pygame.font.Font("fonts/Roboto-Medium.ttf", 30)
text_render_red = text_font.render("Қызыл шабандоз ұтты", True, (235, 64, 52))
text_render_blue = text_font.render("Көк шабандоз ұтты", True, (52, 143, 235))
text_render_green = text_font.render("Жасыл шабандоз ұтты", True, (11, 125, 15))
finish_red = False
finish_blue = False
finish_green = False


red_jockey_count = 0
red_jockey = pygame.image.load('images/red_jockey/k_1.png')
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
red_jockey_x = -20
red_jockey_y = 450
red_jockey_speed = 2.2

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
blue_jokey_y = 500
blue_jockey_speed = 2

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
green_jockey_y = 550
green_jockey_speed = 2

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(bg_image, (bg_x, 0))
    screen.blit(finish, (900, 500))
    keys = pygame.key.get_pressed()
    if red_jockey_x <= 900:
        if keys[pygame.K_RIGHT]:
            game_start = True
            red_jockey_x += red_jockey_speed
            screen.blit(red_jockey_list[red_jockey_count], (red_jockey_x, red_jockey_y))
            if red_jockey_count == 9:
                red_jockey_count = 1
            else:
                red_jockey_count += 1
        else:
            screen.blit(red_jockey_list[0], (red_jockey_x, red_jockey_y))
    else:
        screen.blit(red_jockey_list[0], (red_jockey_x, red_jockey_y))

    if blue_jokey_x <= 900:
        if game_start:
            blue_jokey_x += blue_jockey_speed
            screen.blit(blue_jockey_list[blue_jockey_count], (blue_jokey_x, blue_jokey_y))
            if blue_jockey_count == 9:
                blue_jockey_count = 1
            else:
                blue_jockey_count += 1
        else:
            screen.blit(blue_jockey_list[0], (blue_jokey_x, blue_jokey_y))
    else:
        screen.blit(blue_jockey_list[0], (blue_jokey_x, blue_jokey_y))

    if green_jockey_x <= 900:
        if game_start:
            green_jockey_x += green_jockey_speed
            screen.blit(green_jockey_list[green_jockey_count], (green_jockey_x, green_jockey_y))
            if green_jockey_count == 9:
                green_jockey_count = 1
            else:
                green_jockey_count += 1
        else:
            screen.blit(green_jockey_list[0], (green_jockey_x, green_jockey_y))
    else:
        screen.blit(green_jockey_list[0], (green_jockey_x, green_jockey_y))

    screen.blit(finish, (900, 690))

    if red_jockey_x >= 900 and finish_blue == False and finish_green == False:
        screen.blit(text_render_red, (450, 150))
        finish_red = True
    elif blue_jokey_x >= 900 and finish_red == False and finish_green == False:
        screen.blit(text_render_blue, (450, 150))
        finish_blue = True
    elif green_jockey_x >= 900 and finish_red == False and finish_blue == False:
        screen.blit(text_render_green, (450, 150))
        finish_green = True

    pygame.display.update()
    clock.tick(20)
