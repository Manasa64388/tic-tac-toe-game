#tic tac toe

#Create the game board
board = [' '] * 9

# define winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Initialize current player
current_player = 'X'

# Function to print the game board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

#Function to take player input
def take_input():
    while True:
        position = input("Enter a position (1-9): ")
        if position.isdigit() and 1 <= int(position) <= 9 and board[int(position) - 1] == ' ':
            return int(position) - 1
        else:
            print("Invalid input. Try again.")

# Function to check for a win
def check_win(player):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
        return False

# Function to check for a tie
def check_tie():
    return ' ' not in board

# Game loop
while True:
    print_board()
    print("player", current_player)
    position = take_input()
    board[position] = current_player


    if check_win(current_player):
        print_board()
        print("player", current_player, "wins!")
        break

    if check_tie():
        print_board()
        print("It's a tie!")
        break

    # Switch players
    current_player = 'O' if current_player == 'X' else 'X'