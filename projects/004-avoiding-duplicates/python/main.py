def avoiding_duplicates(words: list) -> list:
    if not isinstance(words, list):
        raise TypeError(f"Expected a list for 'words', got {type(words)} instead.")
        
    without_duplicates = []
    seen = set()

    for word in words:
        if word not in seen:
            seen.add(word)
            without_duplicates.append(word)
    
    return without_duplicates
            

def main():
    user_word = None
    words = []

    while user_word != "":
        user_word = input("Please enter a word (blank line to stop): ").strip(" ")
        if user_word != "":
            words.append(user_word)

    without_duplicates = avoiding_duplicates(words)

    for word in without_duplicates:
        print(word)


if __name__ == "__main__":
    main()