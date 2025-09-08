# -------------The Game board---------------
board = ["1","2","3","4","5","6","7","8","9"]
#Representing the board------------------
def pr_board():
    print("--------------")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("--------------")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("--------------")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("--------------")

# ------------------CODE LOGIC STARTS HERE---------------------
#fun to check winner either 'X' or 'O' -----------
def check_win(player):
    #------here is the list of all possible winning combo------
    win_cond = [
        #rows
        (0,1,2), (3,4,5), (6,7,8),
        #cols
        (0,3,6), (1,4,7), (2,5,8),
        #diagonal
        (0,4,8),(2,4,6)
    ]

    #-------this is a loop that goes through each winning combo 1 by 1 -----
    for a,b,c in win_cond:
        #--- a = rows -----
        #--- b = cols -----
        #--- c = diag -----
        if board[a] == board[b] == board[c] ==player:
            #-----This checks the 3 spots in a winning combo is occupied by the current player. Like a SOS.-----
            return True
    return False

#fun to check for tie in the match
def check_tie():
    #if no empty spaces (numbers) are left, it's a tie
    for space in board:
        #------it checks the spot still contains original number.--------
        if space.isdigit(): 
            #------If it finds any no. left, i.e, game isn't over.-------
            return False
    return True

#-------------------------MAIN GAME LOOP-------------------------
#---initial state of the game for player 'X'----
current_player = "X"
game_over = False

#------it will continue till the game is over-------
while not game_over:
    pr_board()

    # getting player's move
    try:
        move = int(input(f"Player {current_player}, choose a spot (1-9): "))

        # check if the move is valid?
        # ------This is a double-check-------
        if 1 <= move <= 9 and board[move-1].isdigit():
            #-----this will update the board after choosing the spot by the player-----
            board[move-1] = current_player

            #check for a win
            if check_win(current_player):
                pr_board()
                print(f"Player {current_player} wins! 🎉✨✨✨✨🎉🎉🎉🎉🎉🎉")
                game_over = True
            elif check_tie():
                pr_board()
                print("It's a tie! 🤝")
                game_over = True
            #switch to other player-----
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. That spot is already taken or does not exist.")
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 9. ")
print("Game Over.🍾🎉")