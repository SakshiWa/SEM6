def solve_n_queens(n):
    def is_safe(row, col):
        return all(board[i] != col and \
                   abs(board[i] - col) != row - i for i in range(row))

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
        return False

    board = [-1] * n
    if not backtrack(0):
        print("Solution does not exist")
        return

    for row in range(n):
        print("." * board[row] + "Q" + "." * (n - board[row] - 1))

# Example usage:
n = 4
solve_n_queens(n)