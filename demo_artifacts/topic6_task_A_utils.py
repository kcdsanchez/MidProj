# This is the *second file* for "Task A".
# A realistic context involves multiple open files.

def load_data_from_source(source_id: str) -> list:
    """
    A utility function to fetch data from a remote source.
    This is intentionally a separate file.
    """
    print(f"-> Utils: Connecting to remote source {source_id}...")

    # Simulate a complex data-fetching operation
    import time
    time.sleep(0.1)  # Simulate network lag

    # The presenter will add a BOOKMARK on this file
    # (e.g., on the 'return' line) to show that
    # bookmarks are also part of the context.

    print("-> Utils: Data fetched.")
    return [10, 20, 30, 40, 50]


def helper_function_2():
    pass

# ... more utility functions ...