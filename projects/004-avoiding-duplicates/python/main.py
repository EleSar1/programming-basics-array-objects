def avoiding_duplicates(words: list) -> list:
    if not isinstance(words, list):
        raise TypeError(f"Expected a list for 'words', got {type(words)} instead.")
        
    without_duplicates = []

    for word in words:
        if not isinstance(word, str):
            raise TypeError(f"Expected a string for {word}, got {type(word)} instead.")
        if word not in without_duplicates:
            without_duplicates.append(word)
    
    return without_duplicates
            

def main():
    user_word = None
    words = []

    while user_word != "":
        user_word = input("Please enter a world (blank line to stop): ")
        if user_word != "":
            words.append(user_word)

    without_duplicates = avoiding_duplicates(words)

    for word in without_duplicates:
        print(word)


if __name__ == "__main__":
    main()