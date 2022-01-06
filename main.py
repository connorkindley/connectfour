from utils import settings
from utils import functions
import pygame

pygame.init()

def main():
    SCREEN = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Connect Four")

    # Setting up the default screen
    functions.draw_board(SCREEN)
    board = functions.initialize_board()

    # Game Play Initializations
    game_on = True
    allowed = True  # used for placing pieces
    clock = pygame.time.Clock()  
    turn = 0

    while game_on:

        clock.tick(settings.FPS)

        for event in pygame.event.get():  

            if event.type == pygame.QUIT:
                game_on = False

            color = functions.player_turn(SCREEN,turn)

            if event.type == pygame.MOUSEBUTTONDOWN:    

                pos = pygame.mouse.get_pos()
                row, col = functions.get_row_col_from_mouse(pos)
                x, y = pos

                functions.place_piece(color, col, board, SCREEN, allowed)

                if functions.check_winner(board, color):

                    allowed = False     #now pieces won't be placed on the board while waiting on a decision
                    functions.winner_panel(SCREEN, color)
                    pygame.display.update()

                    if functions.click_outside_boxes(x, y):
                        pass

                    if functions.click_play_again(x, y):                                              
                        board = functions.initialize_board()
                        functions.draw_board(SCREEN)
                        turn = 0
                        allowed = True
                        break

                    if functions.click_quit(x, y):                       
                        game_on = False
            
                turn += 1

        pygame.display.update()

    pygame.quit()

    
if __name__ == "__main__":
    main() 
