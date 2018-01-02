import random


def greeting():
    """Displays greeting to the game."""

    print "Let's play Tic Tac Toe!"


def instructions():
    """Displays position number of the squares on the board."""

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


def draw_board(board):
    """Displays the current board."""

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


def player_letter():
    """Lets player choose letter and returns list with player's letter first
    and computer's letter last."""

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


def who_first():
    """Determines who goes first: player or computer."""

    if random.randint(0, 1) == 0:
        return "player"
    else:
        return "computer"


def free_space(board, move):
    """Determines if space is free for play."""

    return board[move] == " "


def player_move(board):
    """User input next move."""

    positions = set([str(x) for x in (range(1, 10))])
    move = " "

    while move not in positions or not free_space(board, int(move)):
        move = raw_input("\nWhere would you like to go? (1-9) ")

        # Account for edge cases
        if not move.isdigit() or (int(move) < 1 or int(move) > 9):
            print "Please input a position between 1 to 9."
        else:
            print "That space is taken; try again."

    return int(move)


def make_move(board, letter, move):
    """Makes the move on the board."""

    board[move] = letter


def copy_board(board):
    """Creates copy of board to determine possible moves for computer."""

    copyboard = []  # deepcopy in copy library may be an option

    for square in board:
        copyboard.append(square)
    return copyboard


def move_random(board, move_list):
    """Makes random move for computer."""

    possible_moves = []

    for square in move_list:
        if free_space(board, square):
            possible_moves.append(square)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return 0


def computer_move(board, player, computer):
    """Provide various scenarios to determine computer move."""

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


def check_win(board, player, computer):
    """Checks if there is a winner before advancing."""

    combinations = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7])

    for com in combinations:
        if (board[com[0]] == player) and (board[com[1]] == player) and (board[com[2]] == player):
            return "player"
        elif (board[com[0]] == computer) and (board[com[1]] == computer) and (board[com[2]] == computer):
            return "computer"

    return False


def full_board(board):
    """Checks if board is full and out of moves."""

    for square in range(1, 10):
        if free_space(board, square):
            return False

    return True


def switch_turn(turn):
    """Switches player/computer turns."""

    if turn == "player":
        return "computer"
    else:
        return "player"


def play_again():
    """User input to play again."""

    play = raw_input("Do you want to play again? (Y/N) ")
    play = play.upper()

    if play not in ["Y", "N"]:
        print "Please input Y or N!"
    elif play == "Y":
        return True


def execute_repl():
    """Executes tic tac toe game."""

    greeting()

    while True:
        board = [" "] * 10
        instructions()
        player, computer = player_letter()
        turn = who_first()
        print "The " + turn + " will go first."

        while True:
            if turn == "player":
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

################################################################################

if __name__ == '__main__':

    execute_repl()
