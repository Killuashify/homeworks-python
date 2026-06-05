def shift_last_to_first(elements):

    if len(elements) <= 1:
        return elements


    return elements[-1:] + elements[:-1]

test_cases = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

if __name__ == "__main__":
    print("--- List Shift Test Results ---")
    for case in test_cases:
        result = shift_last_to_first(case)
        print(f"Original: {case} => Result: {result}")