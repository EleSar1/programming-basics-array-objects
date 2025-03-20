def reverse_lookup(dictionary, value):

    keys = []

    for key in dictionary:
        if dictionary[key] == value:
            keys.append(key)
    
    return keys


def main():
    sample_dict = {"k1": 1,
                   "k2": 2,
                   "k3": 2,
                   "k4": "a",
                   "k5": None,
                   "k6": 2,
                   "k7": 4}

    print(reverse_lookup(sample_dict, 2))
    print(reverse_lookup(sample_dict, 4))
    print(reverse_lookup(sample_dict, 6))


if __name__ == "__main__":
    main()