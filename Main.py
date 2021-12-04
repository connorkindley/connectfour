from utils.settings import *
from utils.functions import *

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Connect Four")

run = True
clock = pygame.time.Clock()  
turn = 0
# draw the default screen
draw(SCREEN)    #keeping this outside the loop makes it so when you draw on it things dont disappear
board = empty_board()
game_on = True
deciding = True


while game_on:
    clock.tick(FPS)
#    game = Game(SCREEN)

    for event in pygame.event.get():        
        #so we can press X to quit the game
        if event.type == pygame.QUIT:
            game_on = False 

        #This allows the player to see who's turn it is. Outside the click loop so you know the turn before clicking.
        player_turn(SCREEN,turn)

        #what happens when we click on the board
        if event.type == pygame.MOUSEBUTTONDOWN:    
            
            pos = pygame.mouse.get_pos()
            row, col = get_row_col_from_mouse(pos)

            if turn % 2 == 0:
                
                for i in reversed(range(ROWS)):
                    if board[i][col] == 0:
                        board[i][col] = RED
                        pygame.draw.circle(SCREEN, RED, (SQUARE_SIZE*col+50, SQUARE_SIZE*i+50), 40)
                        if check_winner(board,RED):
                            winner_panel(SCREEN, RED)
                            pygame.display.update()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos1 = pygame.mouse.get_pos()
                                x1, y1 = pos1

                                #If you click outside the boxes
                                if (55 > x1 > 550) or (400 > y1 > 475) or (350 < x1  < 450):
                                    pass
                                #Click the Play again button
                                if (55 <= x1 <= 350) and (400 <= y1 <= 450):
                                    board = empty_board()
                                    draw(SCREEN)
                                    turn = 0
                                    break
                                #Click the quit button
                                elif (450 <= x1 <= 550) and (400 <= y1 <= 450):
                                    game_on = False
                            break

                        turn += 1
                        break

            else:
                pygame.draw.circle(SCREEN, BLACK, (300, 650), 30)
                for i in reversed(range(ROWS)):
                    if board[i][col] == 0:
                        board[i][col] = BLACK
                        pygame.draw.circle(SCREEN, BLACK, (SQUARE_SIZE*col+50, SQUARE_SIZE*i+50), 40)
                        if check_winner(board, BLACK):
                            winner_panel(SCREEN, BLACK)
                            pygame.display.update()
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                pos1 = pygame.mouse.get_pos()
                                x1, y1 = pos1

                                #If you click outside the boxes
                                if (55 > x1 > 550) or (400 > y1 > 475) or (350 < x1  < 450):
                                    pass
                                #Click the Play again button
                                if (55 <= x1 <= 350) and (400 <= y1 <= 450):
                                    board = empty_board()
                                    draw(SCREEN)
                                    turn = 0
                                    break
                                #Click the quit button
                                elif (450 <= x1 <= 550) and (400 <= y1 <= 450):
                                    game_on = False
                            break

                        turn += 1
                        break
                
    pygame.display.update()
            
                       
    


    