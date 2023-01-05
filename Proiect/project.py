import pygame

BOARD_WIDTH = 1000
BOARD_COLOR = (255, 211, 155)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH))


def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, True, BLACK)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w, y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w, y + h), [x + w, y], 5)
    pygame.draw.rect(screen,(220,20,60), (x, y, w, h))
    return screen.blit(text_render, (x, y))

def menu():
    """ This is the menu that waits you to click the s key to start """
    screen.fill(BOARD_COLOR)
    font = pygame.font.SysFont("Arial", 50)
    text = font.render('Choose your adversary ! ', False, BLACK)
    screen.blit(text, (300, 100))
    b1 = button(screen, (300, 300), "PLAYER")
    b2 = button(screen, (600, 300), "BOT")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return 0
                if event.key == pygame.K_b:
                    return 2  # bot
                if event.key == pygame.K_p:
                    return 1  # player
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    return 1  # player
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    return 2  # bot
        pygame.display.update()


print(menu())
