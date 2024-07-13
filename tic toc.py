def evaluate(board):
    # Evaluate the current board state and return a score
    # Positive score for X (maximizing player), negative score for O (minimizing player)
    # 10 for X win, -10 for O win, 0 for a tie
    if "XXX" in board:
        return 10
    elif "OOO" in board:
        return -10
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if depth == 0 or " " not in board:
        return evaluate(board)

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if board[i] == " ":
                new_board = board[:i] + "X" + board[i + 1:]
                score = minimax(new_board, depth - 1, False)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                new_board = board[:i] + "O" + board[i + 1:]
                score = minimax(new_board, depth - 1, True)
                best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_move = -1
    best_score = float("-inf")
    for i in range(9):
        if board[i] == " ":
            new_board = board[:i] + "X" + board[i + 1:]
            score = minimax(new_board, 9, False)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])

def main():
    board = " " * 9
    print("Tic-Tac-Toe AI (X) vs. Human (O)")
    print_board(board)

    while " " in board:
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != " ":
            print("Invalid move. Try again.")
            continue
        board = board[:human_move] + "O" + board[human_move + 1:]
        print_board(board)

        if " " not in board:
            break

        ai_move = find_best_move(board)
        board = board[:ai_move] + "X" + board[ai_move + 1:]
        print(f"AI's move: {ai_move}")
        print_board(board)

    result = evaluate(board)
    if result == 10:
        print("AI wins!")
    elif result == -10:
        print("Human wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
