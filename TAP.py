import pygame
import sys
import random
from pygame.color import THECOLORS
import ctypes
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

# КАРТИНКИ
wallpeper = [
    os.path.join(current_directory, 'data', 'picture', 'завертин.png'),  
    os.path.join(current_directory, 'data', 'picture', 'знание_путь_к_будущему.png'),  
    os.path.join(current_directory, 'data', 'picture', 'наше_знание.png'),  
    os.path.join(current_directory, 'data', 'picture', 'статуя.png'), 
    os.path.join(current_directory, 'data', 'picture', 'ломоносов.png'), 
]

pygame.init()

can_change_wallpaper = True
# Задержка между сменами в секундах
change_delay = 0.0

image = pygame.image.load(os.path.join(current_directory, 'data', 'picture', '430.png'))  

current_directory = os.path.dirname(os.path.abspath(__file__))

#КАРТИНКИ
wallpeper = [os.path.join(current_directory, 'data', 'picture', 'завертин.png'),  
            os.path.join(current_directory, 'data', 'picture', 'знание_путь_к_будущему.png'),  
            os.path.join(current_directory, 'data', 'picture', 'наше_знание.png'),  
            os.path.join(current_directory, 'data', 'picture', 'статуя.png'), 
            os.path.join(current_directory, 'data', 'picture', 'ломоносов.png'), 
             ]

pygame.init()

can_change_wallpaper = True
# Задержка между сменами в секундах
change_delay = 0.0


image = pygame.image.load(os.path.join(current_directory, 'data', 'picture', '430.png'))  ##### 430

pygame.display.set_caption('ЧИПСЫ С ПАПРИКОЛУ')
icon = pygame.image.load(os.path.join(current_directory, 'data', 'picture', 'чипсина.png'))
pygame.display.set_icon(icon)

white = (255, 255, 255)
screen = pygame.display.set_mode((450, 700))
screen.fill(white)
screen.blit(image, (13, 10))

fontq = pygame.font.Font(os.path.join(current_directory, 'data', 'font', 'Monoid.ttf'), 17)   #monoid
textq = fontq.render('поддержать разраба подпиской :3', True, THECOLORS['gray'])


font = pygame.font.Font(os.path.join(current_directory, 'data', 'font', 'Unbounded_SemiBoldOK1.ttf'), 60) # ТЕКСТ КНОПКИ  unboind
text = font.render("ТАПНИ!", True, THECOLORS['black'])

button = pygame.Rect(78, 570, 305, 80)

def knopa():
    global button
    if button:          #КНОПКИ
        pygame.draw.rect(screen, (255, 255, 255), button, 0)

    if button.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (240, 240, 240), button)  


# ================================================= #
#                      |  MANE  |                   #
#                    |  METHODS  |                  #
# ================================================= #

def menu():
    global button, last_change_time
    run = True
    while run:
        
        current_time = pygame.time.get_ticks() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # baseWall = 'data\\picture\\base.jpg'
                ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(current_directory, 'data', 'picture', 'base.jpg'), 0)
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos):
                if can_change_wallpaper:
                        ctypes.windll.user32.SystemParametersInfoW(20, 0, random.choice(wallpeper), 0)
                    
        knopa()
        screen.blit(textq, (58, 500))
        screen.blit(text, (85, 575))
        # screen.blit(texteq, (95, 710))

        pygame.display.flip()
        pygame.display.update()


menu()