import numpy as np
import pygame
from pygame import gfxdraw
import itertools
import networkx as nx
import random
import sys


def random_move(board, color_turn):  # bot logic
    """
    :param color_turn: whose color turn it is
    :param board: the board of the game (with all the pieces placed)
    :return: a random verified move for the bot
    """
    x = random.randint(0, size - 1)
    y = random.randint(0, size - 1)
    while not is_valid_move(x, y, board, color_turn):
        x = random.randint(0, size - 1)
        y = random.randint(0, size - 1)
    return x, y


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


def is_valid_move(col, row, board, color_turn):  # game logic
    """
    :param color_turn: the color who puts the piece
    :param col: column on which the piece is placed
    :param row: row on which the piece is placed
    :param board: the board of the game (with all the pieces placed)
    :return: True if the piece can be placed, False otherwise
    """
    if col < 0 or col >= size or row < 0 or row >= size:
        return False
    return board[col][row] == 0


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
    captured_stones_by_black: int
    captured_stones_by_white: int

    def __init__(self, size):  # adaugat schimbat putin
        self.board = np.zeros((size, size))
        self.color_turn = 1  # black - 1 , white - 0
        self.interval = (game_size - 2 * border) / (size - 1)
        self.size = size
        self.start_points, self.end_points = gridline_coordinates_optim(self.size)
        self.points = zip(self.start_points, self.end_points)
        self.opponent = 0  # 1 - player, 2 - BOT
        self.last_piece = None
        self.captured_stones_by_black = 0
        self.captured_stones_by_white = 0
        self.first_event = True

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

    def nearly_random(self):  # bot logic
        """
        :return: a valid position for the bot in the liberty of the last piece put by the player
        """
        x, y = self.last_piece[0], self.last_piece[1]
        col, row = self.coordinates_to_col_row(x, y)
        # print(col, row)
        col -= 1
        row -= 1
        max_col = col + 3
        max_row = row + 3
        possible_moves = [[new_col, new_row] for new_col in range(col, max_col) for new_row in range(row, max_row)]
        random.shuffle(possible_moves)
        for move in possible_moves:
            if is_valid_move(move[0], move[1], self.board, self.color_turn):
                return move[0], move[1]

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

    def group_with_no_liberties(self, group):  # game logic
        """
        :param group: group of stones that need to be verified
        :return: True if each stone in the group has no liberties, false if at least one stone has at least one liberty
        """
        for x, y in group:
            if x > 0 and not self.board[x - 1][y] or x < size - 1 and not self.board[x + 1][y]:
                return False
            if y > 0 and not self.board[x][y - 1] or y < size - 1 and not self.board[x][y + 1]:
                return False
        return True

    def capture_group(self, self_color, list_of_groups):  # game logic
        """
        :param self_color: the color that captures
        :param list_of_groups: all the groups of the other color that are verified to be captured
        the groups from the list of groups that have no liberties are captured
        """
        for stone_group in list_of_groups:
            if self.group_with_no_liberties(stone_group):
                for i, j in stone_group:
                    self.board[i, j] = 3
                    if self_color == 1:  # black
                        self.captured_stones_by_black += len(stone_group)
                    else:
                        self.captured_stones_by_white += len(stone_group)

    def get_groups_of_stones(self, color):  # game logic
        """
        :param board: the matrix board with all the pieces placed on it
        :param color: the color whose pieces are searched in the graph for making groups/components
        :return: list of list of coordinates of the groups/components of pieces
        """
        x, y = np.where(self.board == color)
        dimensions = [size, size]
        graph = nx.grid_graph(dimensions)
        stones = set(zip(x, y))
        # print(stones)
        all_spaces = set(itertools.product(range(size), range(size)))
        graph.remove_nodes_from(all_spaces - stones)
        components = nx.connected_components(graph)
        return components

    def handle_click(self):  # user interaction
        """
         function that handles clicks;
         based on user's click it verifies if the click is correct and then updates the board accordingly;
         then it calls the functions for the game logic - the groups function, capture function, draw function
        """
        if self.first_event:
            self.first_event = False
            return
        x, y = pygame.mouse.get_pos()
        col, row = self.coordinates_to_col_row(x, y)
        x, y = self.col_row_to_coordinates(col, row)
        self.last_piece = [x, y]
        if not is_valid_move(col, row, self.board, self.color_turn):
            return
        self.board[col, row] = 2  # white turn
        self_color = 2
        other_color = 1
        if self.color_turn:  # black turn actually
            self.board[col, row] = 1
            self_color = 1
            other_color = 2
        list_of_groups = list(self.get_groups_of_stones(other_color))
        self.capture_group(self_color, list_of_groups)
        self.color_turn = (self.color_turn + 1) % 2
        self.draw()

    def bot_moves(self):  # bot logic
        """
        how the bot plays; first he moves, then he captures (if so) and the turn changes
        """
        # col, row = random_move(self.board)
        if self.last_piece:
            col, row = self.nearly_random()
        else:
            col, row = random_move(self.board, 0)
        if self.color_turn:
            self.board[col, row] = 1
            self_color = 1
            other_color = 2
        else:
            self.board[col, row] = 2
            self_color = 2
            other_color = 1
            list_of_groups = list(self.get_groups_of_stones(other_color))
            self.capture_group(self_color, list_of_groups)

        self.color_turn = (self.color_turn + 1) % 2
        self.draw()

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
        if self.last_piece:
            if self.color_turn:
                gfxdraw.aacircle(self.screen, self.last_piece[0], self.last_piece[1], stone_size - 10, BLACK)
                # gfxdraw.filled_circle(self.screen, self.last_piece[0], self.last_piece[1], stone_size - 10, BLACK)
            else:
                gfxdraw.aacircle(self.screen, self.last_piece[0], self.last_piece[1], stone_size - 10, WHITE)
                # gfxdraw.filled_circle(self.screen, self.last_piece[0], self.last_piece[1], stone_size - 10, WHITE)
        self.turn_info()
        print(self.board)
        pygame.display.flip()

    def is_game_over(self):
        """
        Checks if the game is over (if the board still has any blank spots)
        :return: True if the game is over, False otherwise
        """
        x, y = np.where(self.board == 0)
        if len(x):
            return False
        return True

    def winner(self):
        """
        Checks how many pieces white and black has and compares the numbers
        :return: 0 if black wins, 1 if white wins
        """
        x, y = np.where(self.board == 1)
        self.captured_stones_by_black += len(x)
        x, y = np.where(self.board == 2)
        self.captured_stones_by_white += len(x)
        if self.captured_stones_by_black < self.captured_stones_by_white:
            print("White wins the game!")
        else:
            print("Black wins the game!")

    def event_displayed(self, event):  # game logic
        """
        :param event: the event produced by the user
        how the game reacts because of the user event
        """
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.handle_click()
        elif event.type == pygame.KEYUP and event.key == pygame.K_p:
            self.color_turn = (self.color_turn + 1) % 2
            self.draw()

    def manage_game_with_bot(self, self_color=1):  # bot logic
        """
        :param self_color: the player's color
        :return: how the game reacts because of the user event if his turn or bot moves
        """
        if self_color == 1 and self.color_turn or self_color == 2 and not self.color_turn:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    # print("quit")
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    # print("mouse")
                    self.handle_click()
                if event.type == pygame.KEYUP and event.key == pygame.K_p:
                    # print("p")
                    self.color_turn = (self.color_turn + 1) % 2
                    self.draw()
        else:
            pygame.time.wait(500)
            self.bot_moves()


if __name__ == "__main__":
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
    first_event = False
    g.draw()
    if opponent == 1:  # player :
        # function to establish the way the game will be played : AI or opponent
        while not g.is_game_over():
            events = pygame.event.get()
            for event in events:
                g.event_displayed(event)
    elif opponent == 2:  # bot :
        while not g.is_game_over():
            g.manage_game_with_bot()
    g.winner()

