# This is the artifact for Topic 4: The Integrated Debugger
# This version is longer and has MULTIPLE bugs for a full demo.

def draw_triangle(n: int):
    """Draws a triangle of asterisks with 'n' rows."""
    print(f"--- Drawing a triangle with {n} rows ---")

    # BUG 1: condition infinitely loops, should be n <= 1
    #Bug 1 is an eyeball debug, and does not need a breakpoint to follow the logic
    while True:
        print("Triangle size must be 2 or more.")
        display_menu()

        # This 'else' block is marked as "unreachable" by PyCharm
    else:
        for i in range(1, n + 1):
            line_to_print = ""

            # BUG 3: The inner loop should go to 'i', not 'n'.
            # This will print a square, not a triangle.
            for j in range(1, n + 1):
                line_to_print += "*"

            print(line_to_print)


def display_menu():
    print("\n--- Triangle Drawer Menu ---")
    print("Enter the number of rows for the triangle:")

    try:
        n_input = input("Number of rows (e.g., 4): ")
        n = int(n_input)
        draw_triangle(n)
    except ValueError:
        print("Invalid input. Please enter a number.")
        display_menu()


if __name__ == "__main__":
    display_menu()