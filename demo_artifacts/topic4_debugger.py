# This is the artifact for Topic 4: The Integrated Debugger

def draw_triangle(n):
    """Draws a triangle of asterisks with 'n' rows."""
    print(f"--- Drawing a triangle with {n} rows ---")

    # Infinite loop
    # This should instead only execute when the n is equal or less than 1
    # Use (n<=1) as a condition instead
    while (True):
        print("Triangle cannot be less than or equal to one!")
        display_menu()
    else:
        for i in range(1, n + 1):
            # STEP 2: Set Breakpoint on the line below
            line_to_print = ""

            # THIS IS THE BUG:
            # The inner loop should go to 'i', not 'n'.
            # This will print a square, not a triangle.
            for j in range(1, n + 1):
                line_to_print += "*"
                # STEP 4: We will inspect 'i', 'j', and 'line_to_print'

            print(line_to_print)

def display_menu():
    """Runs the main application logic."""
    # We expect a 4-row triangle, but we'll get a 4x4 square
    print("--- Demonstration ---")
    print("Drawing a triangle of asterisks with 'n' rows.")
    print("Type the value for n: ")
    n = int(input())
    draw_triangle(n)


if __name__ == "__main__":
    display_menu()

