# This is a more extensive artifact for Topic 4: The Integrated Debugger
# It's a buggy solution to the "N-Queens" problem, a classic "hard" LeetCode problem.
# The goal is to find all valid ways to place N queens on an NxN board.

# --- The "Pretty Print" function (This one is correct) ---
def print_solution(board, solution_id):
    """A helper function to print the board nicely."""
    print(f"--- Solution {solution_id} ---")
    for row in board:
        # .join() is a clean way to print the row
        print(" ".join(row))
    print("-" * (len(board) * 2 + 3))


# --- The "Safety Check" function (Contains a bug) ---
def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""

    # Check this column
    # BUG 1: This logic is wrong. It's checking the *row* for queens.
    # It should be checking the *column* by iterating 'i' from 0 to 'row'.
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper-left diagonal
    # This loop is correct
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    # This loop is also correct
    for i, j in zip(range(row, -1, -1), range(col, n, 1)):
        if board[i][j] == 'Q':
            return False

    return True


# --- The main "Solver" function (Contains TWO bugs) ---
def solve_n_queens_util(board, row, n, solutions):
    """
    The main recursive "backtracking" function to solve the problem.
    'row' is the current row we are trying to place a queen on.
    """

    # BUG 2: This is the Base Case. It's an "off-by-one" error.
    # It should be 'if row == n:', not 'row > n'.
    # Because of this, it will never find a solution.
    if row > n:
        # We found a valid solution, add it to our list
        solutions.append([r[:] for r in board])  # Add a *copy* of the board
        return

    # This is the recursive step. Try placing a queen in each column of the current 'row'.
    for col in range(n):

        # Presenter: Set a breakpoint on the next line
        if is_safe(board, row, col, n):
            # 1. Place the queen
            board[row][col] = 'Q'

            # 2. Recurse to the next row
            solve_n_queens_util(board, row + 1, n, solutions)

            # 3. Backtrack (Remove the queen to try the next column)
            # BUG 3: This is the most critical bug. The backtracking
            # step is commented out. The board is never reset.
            # board[row][col] = '.'

    # If no column worked, this function will just end,
    # (implicitly returning) and backtrack to the previous call.


def main():
    """Main function to set up and run the solver."""
    print("--- N-Queens Solver ---")

    try:
        n = int(input("Enter the size of the board (e.g., 4): "))
        if n <= 3:
            print("No solutions exist for N < 4 (except N=1).")
            return
    except ValueError:
        print("Invalid input.")
        return

    # Create the empty board (a list of lists)
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []  # A list to store all found solutions

    # Start the recursive solver from the first row (row 0)
    solve_n_queens_util(board, 0, n, solutions)

    # --- Print the results ---
    if not solutions:
        print(f"No solutions found for N={n}.")
        print("This is probably a bug...")
    else:
        print(f"Found {len(solutions)} solutions for N={n}:")
        for i, s in enumerate(solutions):
            print_solution(s, i + 1)


if __name__ == "__main__":
    main()