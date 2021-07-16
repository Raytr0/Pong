import pygame
import sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Menu')
screen = pygame.display.set_mode((500, 500), 0, 32)

font = pygame.font.Font("freesansbold.ttf", 50)
start_font = pygame.font.Font("freesansbold.ttf", 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


def main_menu():
    while True:

        screen.fill((31, 31, 31))
        draw_text('P O N G', font, (255, 255, 255), screen, 155, 100)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 350, 200, 50)
        button_2 = pygame.Rect(150, 250, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                import game
        if button_2.collidepoint((mx, my)):
            if click:
                import pong_cpu
        pygame.draw.rect(screen, (175, 238, 238), button_1)
        pygame.draw.rect(screen, (175, 238, 238), button_2)
        draw_text('2 player', start_font, (255, 0, 0), screen, 210, 365)
        draw_text('Vs Computer', start_font, (255, 0, 0), screen, 190, 265)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


main_menu()