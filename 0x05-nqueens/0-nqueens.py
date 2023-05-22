#!/usr/bin/python3
"""
N queens challenge
"""
import sys


def is_safe(board, row, col):
    """
    Check if the current position is under attack by any
    previous queens
    """

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    # The position is safe
    return True


def solve_nqueens(board, col):
    """
    Base case: all queens have been placed
    """
    if col == N:
        print_solution(board)
        return True

    # Recursive backtracking to place queens in the current column
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, col + 1)
            board[row][col] = 0


def print_solution(board):
    """
    Print the coordinates of queens in the current solution
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


# Check the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check the value of N
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty board
board = [[0] * N for _ in range(N)]

# Solve the N-queens problem
solve_nqueens(board, 0)
