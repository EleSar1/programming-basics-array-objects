def reversed_order(numbers: list) -> list:
    if not isinstance(numbers, list):
        raise TypeError("Expected list, got a non-list value.")
    return sorted(numbers, reverse=True)


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
    reversed_numbers = reversed_order(numbers)
    for n in reversed_numbers:
        print(n)


if __name__ == "__main__":
    main()
