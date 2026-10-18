def load_data(filename):
    """Load data from a file and return it as a list."""
    try:
        with open(filename, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def save_data(filename, entries):
    """Save data to a file."""
    with open(filename, "w") as file:
        for entry in entries:
            file.write(entry + "\n")


# TODO: Build a small program that reads, saves, and updates data.
# Example ideas: a to-do list, a journal, or a simple contact tracker.
