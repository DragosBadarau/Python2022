import pygame
import numpy as np
import random
from pygame import gfxdraw
BOARD_WIDTH = 1000
BOARD_COLOR = (255, 211, 155)
BLACK = (0, 0, 0)
pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_WIDTH))


def gridline_coordinates_optim(nr_of_rows):  # graphical interface
    """
    :param nr_of_rows: the size of the matrix - how many rows and columns the user wants to have
    :return: two lists : the board coordinates of the start points and the end points for the gridlines
    """
    start_points = []
    board_size = game_size - border
    xs = np.linspace(border, board_size, nr_of_rows)
    ys = np.full(nr_of_rows, border)
    start_points += list(zip(xs, ys))

    end_points = []
    xe = np.linspace(border, board_size, nr_of_rows)
    ye = np.full(nr_of_rows, board_size)
    end_points += list(zip(xe, ye))

    xs, ys = ys, xs
    start_points += list(zip(xs, ys))
    xe, ye = ye, xe
    end_points += list(zip(xe, ye))

    # print(len(start_points), start_points, '\n', len(end_points), end_points)
    return start_points, end_points


def create_button(screen, position, text, font):  # graphical interface
    """
    :param font: the font used to write the text
    :param screen: the screen used for the game
    :param position: a tuple with the x and y coordinates from which the button shall be created
    :param text: the text to be put in the button
    :return: the button created
    """
    text_render = font.render(text, True, BLACK)
    x, y, w, h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, BLACK, position, (x + w, y), 5)
    pygame.draw.line(screen, GRAY, (x, y + h), (x + w, y + h), 5)
    pygame.draw.rect(screen, GREEN, (x, y, w, h))
    return screen.blit(text_render, (x, y))


class Game:

    def __init__(self, size):
        self.board = np.zeros((size, size))
        self.color_turn = 1  # black - 1 , white - 0
        self.interval = (game_size - 2 * border) / (size - 1)
        self.size = size
        self.start_points, self.end_points = gridline_coordinates_optim(self.size)
        self.points = zip(self.start_points, self.end_points)
        self.opponent = 0  # 1 - player, 2 - BOT

    # graphic functions

    def init_pygame(self):  # graphical interface
        """
        function for game initialising - screen, icon, name of the screen, font
        """
        pygame.init()
        pygame.display.set_caption('Game of GO')
        Icon = pygame.image.load("icon.png")
        pygame.display.set_icon(Icon)
        screen = pygame.display.set_mode((game_size, game_size))
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 40)

        # two utils functions to work with board coordinates
    def remake_board(self):  # graphical interface
        """
        clears the screen and draws the gridlines with numbering and lettering
        """
        self.screen.fill((255, 211, 155))
        # print(self.color_turn)
        # gridlines
        self.points = zip(self.start_points, self.end_points)
        for start_point, end_point in self.points:
            pygame.draw.line(self.screen, BLACK, start_point, end_point)
        # numbering and lettering
        font = pygame.font.SysFont("Arial", 25)
        for index in range(size):
            letter = chr(ord('A') + index)
            # print(letter)
            text = font.render(letter, True, GREEN)
            self.screen.blit(text,
                             (border - 5 + self.interval * index, game_size - border + 30))  # bottom
            self.screen.blit(text, (border - 5 + self.interval * index, border - 60))  # top
            if index == 9:
                number = str(10)
            elif index > 9:
                number = f"{int((index + 1) / 10)}{(index + 1) % 10}"
            else:
                number = chr(ord('1') + index)
            text = font.render(number, True, GREEN)
            self.screen.blit(text, (game_size - border + 30, border - 15 + self.interval * index))
            self.screen.blit(text, (border - 60, border - 15 + self.interval * index))
        pygame.display.flip()
    def coordinates_to_col_row(self, x, y):
        """
        :param x: the float coordinate of the board on the x axis
        :param y: the float coordinate of the board on the y axis
        :return: the row and column integers associated with the given coordinates to be used in game logic
        """
        x_dist = x - border
        y_dist = y - border
        col_loc = round(x_dist / self.interval)
        row_loc = round(y_dist / self.interval)
        return int(col_loc), int(row_loc)

    def col_row_to_coordinates(self, col, row):
        """
        :param col: the integer column that has to be converted into coordinate
        :param row: the integer row that has to be converted into coordinate
        :return: the coordinates of the row and column given to be used in draws
        """
        return int(border + col * self.interval), int(border + row * self.interval)
    def turn_info(self):  # graphical interface
        """
        draws infos about whose turn is
        """
        # text for score and turn info
        turn_position = (game_size / 2 - 80, 10)
        if self.opponent == 1:  # player
            up_message = f"{'Black' if self.color_turn else 'White'} places."
        else:  # bot

            if self.color_turn:
                up_message = "Black places. "
            else:
                up_message = 'BOT places. '
        txt = self.font.render(up_message, True, BLACK)
        self.screen.blit(txt, turn_position)

    def draw_stones(self, color, stone_size):
        """
        :param color: color of the stone to be drawn
        :param stone_size: stone size
        draws all the stone for the specified color with the specified size
        """
        for s_col, s_row in zip(*np.where(self.board == color)):
            x, y = self.col_row_to_coordinates(s_col, s_row)
            if color == 1:
                gfxdraw.aacircle(self.screen, x, y, stone_size, BLACK)
                gfxdraw.filled_circle(self.screen, x, y, stone_size, BLACK)
            elif color == 2:
                gfxdraw.aacircle(self.screen, x, y, stone_size, WHITE)
                gfxdraw.filled_circle(self.screen, x, y, stone_size, WHITE)

    def draw(self):  # graphical interface
        """
         function that calls every other draw functions to draw the empty board, stones, turn info and other details
        """
        stone_size = 20
        self.remake_board()
        self.draw_stones(1, stone_size)
        self.draw_stones(2, stone_size)
        self.turn_info()
        print(self.board)
        pygame.display.flip()

    def choose_opponent(self):  # user interaction
        """
        press b for bot or p for player
        or click to choose your adversary
        esc to quit
        :return: 0 for quit, 1 for player, 2 for bot
        """
        self.screen.fill((255, 211, 155))
        bigger_font = pygame.font.SysFont("Arial", 50)
        text = bigger_font.render('Choose your adversary ! ', False, BLACK)
        self.screen.blit(text, (300, 100))
        b1 = create_button(self.screen, (300, 300), "PLAYER", bigger_font)
        b2 = create_button(self.screen, (600, 300), "BOT", bigger_font)
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
                        self.opponent = 2
                        return 2  # bot
                    if event.key == pygame.K_p:
                        self.opponent = 1
                        return 1  # player
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        self.opponent = 1
                        return 1  # player
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        self.opponent = 2
                        return 2  # bot
            pygame.display.update()


if __name__ == "__main__":
    # TODO choose color when against bot
    game_size = 1025
    border = 125
    WHITE = (255, 255, 255)
    GRAY = (64, 64, 64)
    GREEN = (51, 102, 0)
    BLACK = (0, 0, 0)
    size = 19
    g = Game(size)
    g.init_pygame()
    opponent = g.choose_opponent()
    g.draw()
    if opponent == 1:  # player :
        # function to establish the way the game will be played : AI or opponent
        print(1)
