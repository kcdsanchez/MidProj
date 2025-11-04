# This is the artifact for Topic 4: The Integrated Debugger

def draw_triangle(n):
    """Draws a triangle of asterisks with 'n' rows."""
    print(f"--- Drawing a triangle with {n} rows ---")

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


def main():
    """Runs the main application logic."""
    # We expect a 4-row triangle, but we'll get a 4x4 square
    draw_triangle(4)


if __name__ == "__main__":
    main()

