from functions import *

def main():
    
    user_opinion = 'y'

    while user_opinion == 'y':
        read_scoreboard()

        score_board_reset = input('-----Do you want to reset the score board? y/n-----\n').lower()

        if score_board_reset == 'y':
            
            reset_scoreboard()
            read_scoreboard()

        player1, player2 = get_input()

        try:
            resultofgame = game_result(player1, player2)
        
        except ValueError:
            print('--------Both players chose the same move!--------\n---try again please---')
            continue

        write_scoreboard(resultofgame)
        read_scoreboard()

        user_opinion = input('-----Do you want to continue? y/n-----\n').lower()


if __name__ == '__main__':
    main()