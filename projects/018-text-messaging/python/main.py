def text_message_to_keys(message: str="") -> str:

    if not isinstance(message, str):
        raise TypeError("Expected string, got a non-string parameter.")
    
    if message == "":
        return message

    phone_keypad = {"1": ".,?!:",
                    "2": "ABC",
                    "3": "DEF",
                    "4": "GHI",
                    "5": "JKL",
                    "6": "MNO",
                    "7": "PQRS",
                    "8": "TUV",
                    "9": "WXYZ",
                    "0": " "}
    
    pressed_keys = ""
    case_insensitive_msg = message.upper()

    for char in case_insensitive_msg:    
        for phone_key, letters in phone_keypad.items():
            if char in letters:    
                pressed_keys += phone_key * (letters.index(char) + 1)
                break   #avoid useless iterations
            elif char == phone_key:
                pressed_keys += phone_key * (len(letters) + 1)
                break

    return pressed_keys


def main():
    pressed_keys = text_message_to_keys("Hello, world!")
    print(pressed_keys)


if __name__ == "__main__":
    main()
