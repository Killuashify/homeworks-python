import string


def get_letter_range(user_input):
    start_char, end_char = user_input.split("-")

    all_letters = string.ascii_letters

    start_index = all_letters.index(start_char)
    end_index = all_letters.index(end_char)

    return all_letters[start_index: end_index + 1]


test_cases = [
    "a-c",
    "a-a",
    "s-H",
    "a-A"
]

if __name__ == "__main__":
    print("--- Letter Range Test Results ---")
    for case in test_cases:
        result = get_letter_range(case)
        print(f'"{case}" -> {result}')