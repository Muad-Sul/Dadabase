import pygame
import pygame_widgets
from pygame_widgets.dropdown import Dropdown

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dropdown test")
clock = pygame.time.Clock()

def create_dropdown(screen):
    dropdown = Dropdown(
        screen, 35, 25, 100, 30, name='Categories!',
        choices=['Random', 'Sports', 'Animals', 'Food', 'Tech', 'School'],
        borderRadius = 50,
        colour = pygame.Color('peachpuff3'),
        textColour=(0, 0, 0,),
        values = [1, 2, 3, 4, 5, 6],
        direction = 'down'
    )

    return dropdown









