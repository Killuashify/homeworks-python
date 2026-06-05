def move_zeros_to_end(elements):

    non_zeros = [x for x in elements if x != 0]

    zeros_count = elements.count(0)

    return non_zeros + [0] * zeros_count


test_cases = [
    [0, 1, 0, 12, 3],
    [0],
    [1, 0, 13, 0, 0, 0, 5],
    [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
]

if __name__ == "__main__":
    print("--- Move Zeros Test Results ---")
    for case in test_cases:
        result = move_zeros_to_end(case)
        print(f"Original: {case} \nResult:   {result}\n")