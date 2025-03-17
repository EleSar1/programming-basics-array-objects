def only_the_words(sentence: str) -> list:
    
    if not isinstance(sentence, str):
        raise(TypeError, f"Expected a string, got a non-string parameter.")

    words = []

    for word in sentence.split():
        clean_word = word.strip(".,:;-_!?'\"")
        if clean_word != "": 
            words.append(clean_word)
    
    return words


def main():
    sentence = input("Please enter a phrase: ")
    words = only_the_words(sentence)

    print(words)


if __name__ == "__main__":
    main()