def text_message_to_keys(message: str="") -> str:
    
    """
    Converts a text message into key presses on a classic mobile phone keypad.

    Letters are mapped to their respective keys and repeated based on position 
    (e.g., 'A' -> '2', 'B' -> '22'). Digits require extra presses (e.g., '2' -> '2222').

    Parameters:
        message (str): The input text.

    Returns:
        str: The corresponding key press sequence.

    Raises:
        TypeError: If input is not a string.

    Example:
        >>> text_message_to_keys("Hi!")
        '444441111'
    """

    if not isinstance(message, str):
        raise TypeError("Expected string, got a non-string parameter.")
    
    if message == "":
        return message
    
    phone_keypad = {".": "1", ",": "11", "?": "111", "!": "1111", ":": "11111", "1": "111111",
                    "A": "2", "B": "22", "C": "222", "2": "2222", "D": "3", "E": "33",
                    "F": "333", "3": "3333", "G": "4", "H": "44", "I": "444", "4": "4444", 
                    "J": "5", "K": "55", "L": "555", "5": "5555", "M": "6", "N": "66", "O": "666",
                    "6": "6666", "P": "7", "Q": "77", "R": "777", "S": "7777", "7": "77777",
                    "T": "8", "U": "88", "V": "888", "8": "8888", "W": "9", "X": "99", "Y": "999",
                    "Z": "9999", "9": "99999",  " " : "0", "0": "00"}
    
    pressed_keys = ""
    upper_msg = message.upper()

    for char in upper_msg:    
        if char in phone_keypad:
            pressed_keys += phone_keypad[char]

    return pressed_keys


def main():
    pressed_keys = text_message_to_keys("Hello, world!")
    print(pressed_keys)


if __name__ == "__main__":
    main()
