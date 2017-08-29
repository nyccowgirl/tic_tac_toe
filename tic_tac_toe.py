import random


# define function for greeting

def greeting():
    print "Let's play Tic Tac Toe!"


# define function with instructions for position number for squares on board

def instructions():
    separator = " | "
    print "\nThe following are the position numbers on the board:"
    print "\n  " + separator + " " + separator
    print " 1" + separator + "2" + separator + "3"
    print "  " + separator + " " + separator
    print "-----------"
    print "  " + separator + " " + separator
    print " 4" + separator + "5" + separator + "6"
    print "  " + separator + " " + separator
    print "-----------"
    print "  " + separator + " " + separator
    print " 7" + separator + "8" + separator + "9"
    print "  " + separator + " " + separator + "\n"


# define function to draw board

def draw_board(board):
    separator = " | "
    print "\n  " + separator + " " + separator
    print " " + board[1] + separator + board[2] + separator + board[3]
    print "  " + separator + " " + separator
    print "-----------"
    print "  " + separator + " " + separator
    print " " + board[4] + separator + board[5] + separator + board[6]
    print "  " + separator + " " + separator
    print "-----------"
    print "  " + separator + " " + separator
    print " " + board[7] + separator + board[8] + separator + board[9]
    print "  " + separator + " " + separator


# define function for player to choose his/her letter (e.g., X or O)

def player_letter():
    # lets player choose letter and returns list with player's letter first and computer's letter last
    letter = ""
    while not (letter == "X" or letter == "O"):
        letter = raw_input("\nDo you want to be X or O? ")
        letter = letter.upper()
        if letter not in ["X", "O"]:
            print "Please input X or O!"
        elif letter == "X":
            return ["X", "O"]
        else:
            return ["O", "X"]


# define function to determine who goes first based on random generator

def who_first():
    if random.randint(0, 1) == 0:
        return "player"
    else:
        return "computer"


# define function to determine if space is free

def free_space(board, move):
    return board[move] == " "


# define function to let player input move

def player_move(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not free_space(board, int(move)):
        move = raw_input("\nWhere would you like to go? (1-9) ")
        if not move.isdigit() or (move < 1 or move > 9):
            print "Please input a position between 1 to 9."
        else:
            print "That space is taken; try again."
    return int(move)


# define function to display the move on the board

def make_move(board, letter, move):
    board[move] = letter


# define function to create a copy of the board to determine possible computer move

def copy_board(board):
    copyboard = []

    for square in board:
        copyboard.append(square)
    return copyboard


# define function to make random move for computer

def move_random(board, move_list):
    possible_moves = []
    for square in move_list:
        if free_space(board, square):
            possible_moves.append(square)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return 0


# define function to determine computer's move and display the move on the board

def computer_move(board, player, computer):
    # provide various scenarios to determine computer move

    # check if next move will result in win
    for square in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, square):
            make_move(copy, computer, square)
            if check_win(copy, player, computer) == "computer":
                return square

    # check if player can win in next move and block
    for square in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, square):
            make_move(copy, player, square)
            if check_win(copy, player, computer) == "player":
                return square

    # play corner spot if free
    move = move_random(board, [1, 3, 7, 9])
    if move != 0:
        return move

    # play center if free
    if free_space(board, 5):
        return 5

    # otherwise move on one of the sides if free
    return move_random(board, [2, 4, 6, 8])


# define function to determine if there is a winner

def check_win(board, player, computer):
    combinations = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])
    for com in combinations:
        if (board[com[0]] == player) and (board[com[1]] == player) and (board[com[2]] == player):
            return "player"
        if (board[com[0]] == computer) and (board[com[1]] == computer) and (board[com[2]] == computer):
            return "computer"
    return False


# define function to check if board is full

def full_board(board):
    for square in range(1, 10):
        if free_space(board, square):
            return False
    return True


# define function to switch turns

def switch_turn(turn):
    if turn == "player":
        return "computer"
    else:
        return "player"


# define function to allow player to play again

def play_again():
    play = raw_input("Do you want to play again? (Y/N) ")
    play = play.upper()
    if play not in ["Y", "N"]:
        print "Please input Y or N!"
    elif play == "Y":
        return True


# define function to execute the game of Tic Tac Toe

def execute_repl():
    greeting()
    while True:
        board = [" "] * 10
        instructions()
        player, computer = player_letter()
        turn = who_first()
        print "The " + turn + " will go first."

        while True:
            if turn = "player":
                # Player's turn
                draw_board(board)
                move = player_move(board)
                make_move(board, player, move)

                if check_win(board, player, computer) == "player":
                    draw_board(board)
                    print "Congratulations! You are the winner!"
                    break
                elif full_board(board):
                    draw_board(board)
                    print "The game is a tie!"
                    break
                else:
                    turn = switch_turn(turn)

            elif turn == "computer":
                # Computer's turn
                move = computer_move(board, player, computer)
                make_move(board, computer, move)

                if check_win(board, player, computer) == "computer":
                    draw_board(board)
                    print "The computer has won! Better luck next time!"
                    break
                elif full_board(board):
                    draw_board(board)
                    print "The game is a tie!"
                    break
                else:
                    turn = switch_turn(turn)

        if not play_again():
            break


execute_repl()
