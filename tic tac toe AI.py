import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

   
    for row in board:
        if ' ' in row:
            return None
    
    return 'Tie'

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':
        return -10 + depth
    elif winner == 'O':
        return 10 - depth
    elif winner == 'Tie':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = 'O'

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_turn = True

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == 'Tie':
                print("It's a tie!")
            else:
                print(f"{winner} wins!")
            break

        if human_turn:
            print("Your turn. Enter row and column (0-2):")
            while True:
                try:
                    row, col = map(int, input().split())
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("Cell already taken. Choose another.")
                except (ValueError, IndexError):
                    print("Invalid input. Enter row and column as two numbers (0-2).")
        else:
            print("AI's turn:")
            ai_move(board)

        human_turn = not human_turn

if __name__ == "__main__":
    main()