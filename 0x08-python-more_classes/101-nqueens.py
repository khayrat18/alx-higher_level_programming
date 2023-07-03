#!/usr/bin/python3
import sys


def print_board(board):
    """Prints the board."""
    for row in board:
        print(" ".join(row))


def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen at board[row][col].
    Returns True if it is safe, False otherwise.
    """
    # Check row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # The position is safe
    return True


def solve(board, col):
    """
    Recursively places queens on the board, starting from the leftmost column.
    Returns True if a solution is found, False otherwise.
    """
    # Base case: all queens have been placed
    if col == len(board):
        print_board(board)
        return True

    # Recursive case: try placing a queen in each row of the current column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            solve(board, col + 1)
            board[row][col] = "."

    # No solution found
    return False


def nqueens(n):
    """Finds and prints all solutions to the n-queens problem."""
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [["." for _ in range(n)] for _ in range(n)]
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
