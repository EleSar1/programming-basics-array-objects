def remove_outliers(values: list, n: int) -> list:

    if not isinstance(values, list):
        raise TypeError(f"Expected a list for 'values' parameter, got a {type(values)} instead.")
    if not isinstance(n, int):
        raise TypeError(f"Expected a list for 'n' parameter, got a {type(n)} instead.")

    if n < 0:
        raise ValueError(f"Expected a non-negative number for 'n', got {n}")
    values_in_ascended_order = sorted(values[:])
    return values_in_ascended_order[n:-n]


def main():
    values = [5, -1, 4, -18, 2, 3, 8, 10]
    n = 2
    if len(values) < 4:
        print(f"Expected more than 4 values. Entered only {len(values)}")
    else:
        removed_outliers = remove_outliers(values, n)
        print(f"Result with outliers removed:\n{removed_outliers}")
        print(f"Original list:\n{values}")


if __name__ == "__main__":
    main()




