# 1. Name:
#      Mitzi Vite
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      The hardest partfor me was the play_game function, because i needed to think of different cases where the player could do that could make the code to break. 
# Also, the funcion of is_x_turn was a bit tricky because i was struggling to find a way to count the X's and O's in the board.
# 5. How long did it take for you to complete the assignment?
#      Around 5 hours
import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    try:
        with open(filename, 'r') as filehandle:
            data = json.load(filehandle)
        return data['board']
    except FileNotFoundError:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    with open (filename, 'w') as filehandle:
        json.dump({'board': board}, filehandle)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} \n')
    print()

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    xTotal = board.count(X)
    oTotal = board.count(O)
    return xTotal == oTotal
    

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    display_board(board)
    if is_x_turn(board):
        player = X
    else:
        player = O
    
    user_input = input(f"It is {player}'s turn. Enter a position from 1 to 9 or 'q' to quit: ")
    if user_input == 'q':
        save_board('tictactoe.json', board)
        print("Game saved. Goodbye!")
        return False
    
    if not user_input.isdigit():
        print("Invalid input. Please enter a number between 1 and 9.")
        return True
    
    chosen_square = int(user_input) - 1

    if chosen_square < 0 or chosen_square > 8:
        print("Invalid square. Please choose a number between 1 and 9.")
        return True

    if board[chosen_square] != BLANK:
        print("That square is already occupied. Please choose another.")
        return True
    
    board[chosen_square] = player
    save_board('tictactoe.json', board)
    
    if game_done(board, message=True):
        display_board(board)
        print("Game over!")
        return False
    
    return True


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
# print("The current board is:")

# The file read code, game loop code, and file close code goes here.

def main():
 
    keep_playing = True 

    while keep_playing:
        board = read_board('tictactoe.json')

        if game_done(board):
            print("The previous game is finished.")
            new_game = input("Do you want to start a new game? (y/n): ").lower()
            if new_game == 'y':
                board = blank_board['board'].copy()
            else:
                print("Goodbye!")
                keep_playing = False
                continue

        print("The current board is:")
        
        while play_game(board):
            pass
        
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            keep_playing = False

if __name__ == "__main__":
    main()
