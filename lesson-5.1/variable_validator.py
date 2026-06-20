import string
import keyword


def validate_variable_name(name):
    if name in keyword.kwlist:
        return False

    if name and name[0].isdigit():
        return False

    if "__" in name:
        return False

    for char in name:
        if char.isupper():
            return False
        if char.isspace():
            return False
        if char in string.punctuation and char != '_':
            return False

    return True


test_cases = [
    "_", "__", "___", "x", "get_value", "get value",
    "get!value", "some_super_puper_value", "Get_value",
    "get_Value", "getValue", "3m", "m3", "assert", "assert_exception"
]

if __name__ == "__main__":
    print("--- Variable Name Validator Test Results ---")
    for case in test_cases:
        result = validate_variable_name(case)
        print(f"'{case}' => {result}")