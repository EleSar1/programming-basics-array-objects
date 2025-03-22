import random 
from tabulate import tabulate


def bingo_card_generator() -> dict:

    """
    Generate a Bingo card as a dictionary.
    
    The Bingo card consists of five columns labeled 'B', 'I', 'N', 'G', and 'O'.
    Each column contains five random numbers within specific ranges:
    - 'B' column: numbers from 1 to 15
    - 'I' column: numbers from 16 to 30
    - 'N' column: numbers from 31 to 45
    - 'G' column: numbers from 46 to 60
    - 'O' column: numbers from 61 to 75
    
    Returns:
        dict: A dictionary representing the Bingo card with column labels as keys
              and lists of five random numbers as values.
    """

    bingo_card = {"B": [random.randint(1,15) for _ in range(5)],
                  "I": [random.randint(16,30) for _ in range(5)],
                  "N": [random.randint(31,45) for _ in range(5)],
                  "G": [random.randint(46,60) for _ in range(5)],
                  "O": [random.randint(61,75) for _ in range(5)]}
    
    return bingo_card


def display_bingo_card(bingo_card: dict) -> str:

    """
    Format and return a Bingo card as a table string.

    This function takes a dictionary representing a Bingo card and formats it
    into a human-readable table using the `tabulate` library.

    Args:
        bingo_card (dict): A dictionary where the keys are the Bingo column labels
                           ('B', 'I', 'N', 'G', 'O') and the values are lists of five 
                           numbers corresponding to each column.

    Returns:
        str: A formatted string representation of the Bingo card in grid format.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    
    if not isinstance(bingo_card, dict):
        raise(TypeError, "Expected dict, got a non-dict parameter.")
    
    return tabulate(bingo_card, headers="keys", tablefmt="grid")


def main():

    bingo_card = bingo_card_generator()
    print(display_bingo_card(bingo_card))


if __name__ == "__main__":
    main()