#board display
def outline(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_winner(board, mark):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6] # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == mark for i in condition):
            return True
    return False


def available_moves(board):
    return [i for i, v in enumerate(board) if v not in ("X", "O")]

def get_ai_move(board, ai_mark, mode):
    import random
    opponent = "O" if ai_mark == "X" else "X"

    # Simple: random available move
    if mode == "simple":
        return random.choice(available_moves(board))

    # Proficient: win if possible, block if necessary, take center, corners, then random
    if mode == "proficient":
        # try win
        for i in available_moves(board):
            board_copy = board[:]
            board_copy[i] = ai_mark
            if check_winner(board_copy, ai_mark):
                return i
        # try block
        for i in available_moves(board):
            board_copy = board[:]
            board_copy[i] = opponent
            if check_winner(board_copy, opponent):
                return i
        # center
        if 4 in available_moves(board):
            return 4
        # corners
        corners = [0, 2, 6, 8]
        open_corners = [c for c in corners if c in available_moves(board)]
        if open_corners:
            return random.choice(open_corners)
        return random.choice(available_moves(board))

    # Master
    def minimax(board_state, player):
        if check_winner(board_state, ai_mark):
            return 1
        if check_winner(board_state, opponent):
            return -1
        moves_left = available_moves(board_state)
        if not moves_left:
            return 0

        if player == ai_mark:
            best = -float('inf')
            for m in moves_left:
                b = board_state[:]
                b[m] = player
                val = minimax(b, opponent)
                best = max(best, val)
            return best
        else:
            best = float('inf')
            for m in moves_left:
                b = board_state[:]
                b[m] = player
                val = minimax(b, ai_mark)
                best = min(best, val)
            return best

    best_score = -float('inf')
    best_move = None
    for m in available_moves(board):
        b = board[:]
        b[m] = ai_mark
        score = minimax(b, opponent)
        if score > best_score:
            best_score = score
            best_move = m
    return best_move


def game():
    board = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print("Modes: 1) Human vs Human  2) Human vs AI  3) AI vs AI\n")
    mode = input("Choose mode (1/2/3): ").strip()

    ai_mode = None
    ai_mark = None
    human_mark = None
    ai_starts = False

    if mode == '2':
        choice = input("Choose AI difficulty: simple, proficient, master: ").strip().lower()
        if choice not in ("simple", "proficient", "master"):
            print("Invalid choice, defaulting to simple.")
            choice = "simple"
        ai_mode = choice
        human_first = input("Do you want to play first? (y/n): ").strip().lower()
        if human_first == 'y':
            human_mark = "X"
            ai_mark = "O"
            current_player = "X"
        else:
            human_mark = "O"
            ai_mark = "X"
            current_player = "X"
            ai_starts = (ai_mark == current_player)
    elif mode == '3':
        # AI vs AI demonstration
        ai_mode = input("AI difficulty for both (simple/proficient/master): ").strip().lower()
        if ai_mode not in ("simple", "proficient", "master"):
            ai_mode = "master"
        ai_mark = "O"
        human_mark = None
        current_player = "X"
    else:
        current_player = "X"

    print("Choose a cell (a–i) to place your mark.\n")

    while moves < 9:
        outline(board)
        print(f"\nPlayer {current_player}'s turn.")

        if ai_mode and ((mode == '2' and current_player == ai_mark) or mode == '3'):
            idx = get_ai_move(board, current_player, ai_mode)
            print(f"AI ({current_player}) chooses {board[idx]}")
            board[idx] = current_player
        else:
            choice = input("Enter your cell: ").lower()
            # Validate move
            if choice not in board:
                print("Invalid move! Cell is either taken or doesn't exist. Try again.\n")
                continue
            board[board.index(choice)] = current_player

        moves += 1

        # Check winner
        if check_winner(board, current_player):
            outline(board)
            print(f"\n Player {current_player} wins!")
            return

        # Switch player
        current_player = "O" if current_player == "X" else "X"

    # If 9 moves done and no winner
    outline(board)
    print("\nIt's a draw!")

    # If 9 moves done and no winner
    outline(board)
    print("\nIt's a draw!")


def main():
    game()

# Run game
if __name__ == "__main__":
    main()
