
def is_sublist(main_list: list, smaller_list: list= []) -> bool:

    main_list_length = len(main_list)
    small_list_length = len(smaller_list)

    if small_list_length > main_list_length:
        return False

    for index in range(main_list_length - small_list_length + 1):
        if main_list[index:index + small_list_length] == smaller_list:
            return True
        
    return False


def main():
    print(is_sublist([0,1,2,3,4], [0,12]))
    print(is_sublist(["a", "b", "c", "d"], ["c", "d"]))
    print(is_sublist([], [1,2,3,4]))

if __name__ == "__main__":
    main()