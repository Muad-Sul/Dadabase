import pygame
import requests
from DadJoke import get_dadJoke
from dropdownmenu import create_dropdown
import pygame_widgets


pygame.init()
# Initialize Pygame
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Dada-Base")
clock = pygame.time.Clock()
dropdown = create_dropdown(screen)

logo_img = pygame.image.load("dadabaselogo.png").convert_alpha()
logo_shape = logo_img.get_rect(center=((1000 // 2) - 2, 150))
# logo gets set near the top

test_surface = pygame.Surface((490, 70))
test_surface.fill((0, 0, 0))
screen.blit(test_surface, (250, 270))
# rectangle where the joke appears

font = pygame.font.SysFont("arial", 22)
button_rect = pygame.Rect(375, 500, 250, 50)
button_color = pygame.Color('turquoise2')
button_text = font.render("Generate more laughs!", True, (0, 0, 0))
# blue button near the bottom | joke text | define generate button

current_joke = get_dadJoke()
# gets joke right away right when app opens


running = True
while running:
    screen.fill((255, 255, 255))
# main loop | handles quitting app | handles button clicks | draws everything on screen repeatedly

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                current_joke = get_dadJoke()
    pygame_widgets.update(events)

    screen.blit(test_surface, (250, 265)) # joke area
    screen.blit(logo_img, logo_shape) # logo
    pygame.draw.rect(screen, button_color, button_rect, border_radius=10) # button
    screen.blit(button_text, button_text.get_rect(center=button_rect.center)) # button
#refreshes background | draws everything on every frame

    # joke wrap
    if current_joke:
        joke_font = pygame.font.SysFont("arial", 20)
        words = current_joke.split(" ")
        #splits joke into individual words so it can split instead of going off screen
        line = ""
        y = 280

        for word in words:
            test_line = line + word + " "
            #for each word, it checks if adding the next word would fit the screen
            if joke_font.size(test_line)[0] < 450:
                line = test_line
                #if it fits within 450px, keep building line
            else:
                text = joke_font.render(line, True, (0, 0, 0))
                x = 250 + (500 - text.get_width()) // 2 # center words
                screen.blit(text, (x, y))
                y += 25
                line = word + " "

    if line:
        text = joke_font.render(line, True, (0, 0, 0))
        x = 250 + (500 - text.get_width()) // 2
        screen.blit(text, (x, y))


    pygame.display.update()
    clock.tick(60)

pygame.quit()

