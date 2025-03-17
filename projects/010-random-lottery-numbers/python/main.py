from random import randrange

def random_lottery_numbers() -> list:
    
    numbers = []
    
    while len(numbers) < 6:
        number = randrange(1,49)
        if number not in numbers:
            numbers.append(number)
    
    return numbers


def main():
    
    numbers = random_lottery_numbers()

    for number in numbers:
        print(number)
        

if __name__ == "__main__":
    main()