'''
All functions for the connect four "main" program are kept here.
'''
from utils import settings
import pygame

pygame.init()

def check_winner(board,color):
    '''
    Checks the entire board to see if there is a winner.
    Input: board object, color of the piece to check.
    Output: True if a winner, else nothing
    '''
    for i in reversed(range(settings.ROWS)):
        for j in range(settings.COLS):
            if board[i][j] == color:
                # Check blocks above
                try:
                    if board[i-1][j] == color:
                        if board[i-2][j] == color:
                            if board[i-3][j] == color:
                                return True
                except:
                    continue
                # Check left diagonal
                try:
                    if board[i-1][j-1] == color:
                        if board[i-2][j-2] == color:
                            if board[i-3][j-3] == color:
                                return True
                except:
                    continue
                # Check right diagonal
                try:
                    if board[i-1][j+1] == color:
                        if board[i-2][j+2] == color:
                            if board[i-3][j+3] == color:
                                return True
                except:
                    continue
                # Check horizontally
                try:
                    if board[i][j+1] == color:
                        if board[i][j+2] == color:
                            if board[i][j+3] == color:
                                return True
                except:
                    continue

def click_outside_boxes(x_pos, y_pos):
    '''
    Checks if the mouse clicked outside of the play again or quit boxes.
    Input: x position of mouse, y position of mouse.
    Output: boolean
    '''
    return ((x_pos < settings.PLAY_AGAIN_BOX[0] or x_pos > (settings.QUIT_BOX[0] + settings.QUIT_BOX[2])) or (
        y_pos < settings.PLAY_AGAIN_BOX[1] or y_pos > (settings.PLAY_AGAIN_BOX[1] + settings.PLAY_AGAIN_BOX[3])) or (
        (settings.PLAY_AGAIN_BOX[0]+settings.PLAY_AGAIN_BOX[2]) < x_pos  < settings.QUIT_BOX[0]))


def click_play_again(x_pos, y_pos):
    '''
    Checks if the play again button is pressed.
    Input: x position of mouse, y position of mouse.
    Output: boolean
    '''
    return ((settings.PLAY_AGAIN_BOX[0] <= x_pos <= settings.PLAY_AGAIN_BOX[0]+settings.PLAY_AGAIN_BOX[2]) and (
     settings.PLAY_AGAIN_BOX[1] <= y_pos <= settings.PLAY_AGAIN_BOX[1] + settings.PLAY_AGAIN_BOX[3]))


def click_quit(x_pos, y_pos):
    '''
    Checks if the quit button is pressed.
    Input: x position of mouse, y position of mouse.
    Output: boolean    
    '''
    return ((settings.QUIT_BOX[0] <= x_pos <= settings.QUIT_BOX[0] + settings.QUIT_BOX[2]) and (
        settings.QUIT_BOX[1] <= y_pos <= settings.QUIT_BOX[1] + settings.QUIT_BOX[3]))


def draw_board(screen):
    '''
    Draws our board.
    Input: the SCREEN we are playing on.
    Output: none.
    '''
    screen.fill(settings.BLUE) 
    pygame.font.init()

    #Draw the circles for the empty spaces
    pygame.draw.rect(screen, settings.YELLOW,(0, 0, settings.WIDTH, settings.HEIGHT))
    for row in range(settings.ROWS):
        for col in range(settings.COLS):
            pygame.draw.circle(screen, settings.WHITE, (settings.SQUARE_SIZE*col+50, settings.SQUARE_SIZE*row+50), 40)

    # Draw the text at the bottom
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render("Player's Turn:", True, settings.BLACK)
    textRect = text.get_rect()
    textRect.center = (125, 625)
    screen.blit(text, textRect)
    

def initialize_board():
    '''
    This puts 0 in every open circle.
    '''
    board = []
    for row in range(settings.ROWS):
        board.append([])   #this creates a list for every row. That list will house the columns
        for _ in range(settings.COLS):   
            board[row].append(0)  # now every open spot has a zero
    return board


def get_row_col_from_mouse(pos):
    '''
    Taken from Code with Tim's checkers game. This takes the position of the mouse and returns the row and column
    number of that coordinate based on the size of the squares used to help sketch out the look of the board.
    '''
    x, y = pos
    col = x // settings.SQUARE_SIZE
    row = y // settings.SQUARE_SIZE
    return row, col


def place_piece(color, col, board, SCREEN, allowed):
    '''
    This draws either a red or black cirlce piece to the botton of the board - like how pieces are dropped to their
    position.
    Input: color of piece, column of selected position, the board of 0s and colors, the SCREEN played on, and a boolean if allowed to play.
    Output: none. Objects are saved in the board object and drawn to the screen.
    '''
    if allowed:
        for i in reversed(range(settings.ROWS)):
            if board[i][col] == 0 and i>=0:
                board[i][col] = color
                pygame.draw.circle(SCREEN, color, (settings.SQUARE_SIZE*col+50, settings.SQUARE_SIZE*i+50), 40)
                break
    

def player_turn(screen, turn):
    '''
    Decides which color piece is playing and draws the piece at the bottom of the screen.
    Input: SCREEN played on, the turn number
    Output: the player's color.    
    '''
    if turn % 2 == 0:
        pygame.draw.circle(screen, settings.RED, (300, 650), 30)
        return settings.RED
    else:
        pygame.draw.circle(screen, settings.BLACK, (300, 650), 30)
        return settings.BLACK


def winner_panel(screen, color):
    '''
    Draws the panel declaring who won, the play again button, and the quit button.
    Input: the SCREEN played on, the color of the winning player.
    Output: none.   
    '''
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf',100)

    if color == settings.RED:
        text = font.render("RED WON!", True, settings.RED, settings.BLUE)
    else:
        text = font.render("BLACK WON!", True, settings.BLACK, settings.BLUE)

    textRect = text.get_rect()
    textRect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)
    screen.blit(text, textRect)

    font2 = pygame.font.Font('freesansbold.ttf', 48)

    text_Left = font2.render("Play Again?", True, settings.BLACK, settings.RED)
    textRect_Left = text_Left.get_rect()
    textRect_Left.center = (200, 425)
    screen.blit(text_Left, textRect_Left)

    text_Right = font2.render("Quit", True, settings.BLACK, settings.RED)
    textRect_Right = text_Right.get_rect()
    textRect_Right.center = (500, 425)
    screen.blit(text_Right, textRect_Right)
