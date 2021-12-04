'''
This will be where all my functions are kept.
'''
from .settings import *

def draw(screen):
    '''
    Draws our board.
    '''
    screen.fill(BLUE) 

    #Draw the circles for the empty spaces
    pygame.draw.rect(screen, YELLOW,(0, 0, WIDTH, HEIGHT))
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.circle(screen, WHITE, (SQUARE_SIZE*col+50, SQUARE_SIZE*row+50), 40)

    # Draw the text at the bottom
    font = pygame.font.Font('freesansbold.ttf',32)
    text = font.render("Player's Turn:", True, BLACK)
    textRect = text.get_rect()
    textRect.center = (125, 625)
    screen.blit(text, textRect)
    

def get_row_col_from_mouse(pos):
    '''
    Taken from Code with Tim's checkers game. Need this so we can select where we want to put our piece.
    '''
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

def empty_board():
    '''
    This puts 0 in every open circle.
    '''
    board = []
    for row in range(ROWS):
        board.append([])   #this creates a list for every row. That list will house the columns
        for _ in range(COLS):   
            board[row].append(0)  # now every open spot has a zero
    return board

def check_winner(board,color):
    '''
    Checks the entire board to see if there is a winner.
    Input: board object, color of the piece to check.
    Output: True if a winner, else nothing
    '''
    for i in reversed(range(ROWS)):
        for j in range(COLS):
            if board[i][j] == color:
                # Check blocks above
                try:
                    if board[i-1][j] == color:
                        if board[i-2][j] == color:
                            if board[i-3][j] == color:
                                return True
#                            return False
#                        return False
                except:
                    continue
                # Check left diagonal
                try:
                    if board[i-1][j-1] == color:
                        if board[i-2][j-2] == color:
                            if board[i-3][j-3] == color:
                                return True
#                            return False
#                        return False
                except:
                    continue
                # Check right diagonal
                try:
                    if board[i-1][j+1] == color:
                        if board[i-2][j+2] == color:
                            if board[i-3][j+3] == color:
                                return True
#                            return False
#                        return False
                except:
                    continue
                # Check horizontally
                try:
                    if board[i][j+1] == color:
                        if board[i][j+2] == color:
                            if board[i][j+3] == color:
                                return True
#                            return False
#                        return False
                except:
                    continue

def player_turn(screen, turn):
    if turn % 2 == 0:
        pygame.draw.circle(screen, RED, (300, 650), 30)
    else:
        pygame.draw.circle(screen, BLACK, (300, 650), 30)

def winner_panel(screen, color):
    font = pygame.font.Font('freesansbold.ttf',100)
    if color == RED:
        text = font.render("RED WON!", True, RED, BLUE)
    else:
        text = font.render("BLACK WON!", True, BLACK, BLUE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

    font2 = pygame.font.Font('freesansbold.ttf', 48)
    text_Left = font2.render("Play Again?", True, BLACK, RED)
    textRect_Left = text_Left.get_rect()
    text_Right = font2.render("Quit", True, BLACK, RED)
    textRect_Right = text_Right.get_rect()
    textRect_Left.center = (200, 425)
    textRect_Right.center = (500, 425)
    screen.blit(text_Left, textRect_Left)
    screen.blit(text_Right, textRect_Right)

def board_full(board):
    for j in board[0]:
        if j == 0:
            return True

def board_full_panel(screen):
    font = pygame.font.Font('freesansbold.ttf',80)
    text = font.render("BOARD IS FULL!", True, BLACK, BLUE)
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, textRect)

    font2 = pygame.font.Font('freesansbold.ttf', 48)
    text_Left = font2.render("Play Again?", True, BLACK, BLUE)
    textRect_Left = text_Left.get_rect()
    text_Right = font2.render("Quit", True, BLACK, BLUE)
    textRect_Right = text_Right.get_rect()
    textRect_Left.center = (200, 425)
    textRect_Right.center = (500, 425)
    screen.blit(text_Left, textRect_Left)
    screen.blit(text_Right, textRect_Right)