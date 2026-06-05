def split_list(elements):
    midpoint = (len(elements) + 1) // 2

    first_half = elements[:midpoint]
    second_half = elements[midpoint:]

    return [first_half, second_half]


test_cases = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

if __name__ == "__main__":
    print("--- List Split Test Results ---")
    for case in test_cases:
        result = split_list(case)
        print(f"Original: {case} => Result: {result}")