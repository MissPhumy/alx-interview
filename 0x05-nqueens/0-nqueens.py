#!/usr/bin/python3
'''N-Queens Challenge'''

import sys

def is_safe(queens, row, col):
    """Check if it's safe to place a queen at (row, col)"""
    for r, c in enumerate(queens):
        if c == col or c - (row - r) == col or c + (row - r) == col:
            return False
    return True

def solve_nqueens(n):
    """Solve the N-Queens problem and return all solutions"""
    def backtrack(queens, row):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(queens, row + 1)
                queens.pop()

    solutions = []
    backtrack([], 0)
    return solutions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[i, solution[i]] for i in range(n)])
