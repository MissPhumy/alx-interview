#!/usr/bin/python3
'''N-Queens Challenge '''


import sys

def is_valid(board, row, col):
    # Check the column
    for i in range(row):
        if board[i] == col:
            return False
    # Check the diagonal (top-left to bottom-right)
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    # Check the other diagonal (top-right to bottom-left)
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False
    return True

def solve_nqueens(n):
    def backtrack(board, row):
        if row == n:
            print_solution(board)
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)
                board[row] = -1
def print_solution(board):
        solution = []
        for row in range(n):
            solution.append([row, board[row]])
        print(solution)

    board = [-1] * n
    backtrack(board, 0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

	try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N) 
        

