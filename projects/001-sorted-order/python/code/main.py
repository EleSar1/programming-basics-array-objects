def sorted_order(numbers: list) -> list:

    if not isinstance(numbers, list):
        raise TypeError("Expected a list, but got a non-list value.")
    return sorted(numbers)


def main():
    number = None
    numbers = []
    while number != 0:
        try:
            number = int(input("Please enter an integer (enter 0 if you want to stop): "))
            if number != 0:
                numbers.append(number)
            else:
                print("Exiting . . . Goodbye!")
        except ValueError:
            print("\nError: you entered an unsupported value. Please make sure to enter a valid integer.\n")
    sorted_numbers = sorted_order(numbers)
    for n in sorted_numbers:
        print(n)


if __name__ == "__main__":
    main()
