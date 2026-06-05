def sum_even_and_multiply(elements):
    if not elements:
        return 0

    even_sum = sum(elements[::2])

    return even_sum * elements[-1]


test_cases = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

if __name__ == "__main__":
    print("--- Even Sum & Multiply Test Results ---")
    for case in test_cases:
        result = sum_even_and_multiply(case)
        print(f"Original: {case} => Result: {result}")