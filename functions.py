import csv

def get_input():

    player_num1 = input('First player\'s move:\n').lower()
    player_num2 = input('Second player\'s move:\n').lower()

    return(player_num1, player_num2)

def game_result(player1, player2):
    
    if player1 == player2:
        raise ValueError('Both players chose the same move!')

    elif player1 == 'rock' and player2 == 'scissors':
        print('--------Player1 wins!---------')
        return('player1')

    elif player1 == 'paper' and player2 == 'rock':
        print('--------Player1 wins!---------')
        return('player1')

    elif player1 == 'scissors' and player2 == 'paper':
        print('--------Player1 wins!---------')    
        return('player1')

    elif player1 == 'rock' and player2 == 'paper':
        print('--------Player2 wins!---------')
        return('player2')

    elif player1 == 'paper' and player2 == 'scissors':
        print('--------Player2 wins!---------')
        return('player2')

    elif player1 == 'scissors' and player2 == 'rock':
        print('--------Player2 wins!---------')
        return('player2')

def read_scoreboard():
    
    print('----------Score Board-----------')

    with open('scoreboard.csv', mode='r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            print(row)

    print('--------------------------------------')

def write_scoreboard(winner_name):

    with open('scoreboard.csv', mode='r') as f:
        reader = csv.DictReader(f)

        winner_score = 0
        other_player_score = 0

        for row in reader:
            if row['name'] == winner_name:
                winner_score = int(row['score'])

            if row['name'] != winner_name:
                other_player_score = int(row['score'])

        
    with open('scoreboard.csv', mode='w') as f:
        
        writer = csv.DictWriter(f, fieldnames=['name', 'score'])

        if winner_name == 'player1':
            winner_score += 1

            writer.writeheader()
            writer.writerow({'name': 'player1', 'score': winner_score})
            writer.writerow({'name': 'player2', 'score': other_player_score})

        elif winner_name == 'player2':
            winner_score += 1

            writer.writeheader()
            writer.writerow({'name': 'player1', 'score': other_player_score})
            writer.writerow({'name': 'player2', 'score': winner_score})



def reset_scoreboard():

    with open('scoreboard.csv', mode='w') as f:

        writer = csv.DictWriter(f, fieldnames=['name', 'score'])

        writer.writeheader()
        writer.writerow({'name': 'player1', 'score': 0})
        writer.writerow({'name': 'player2', 'score': 0})