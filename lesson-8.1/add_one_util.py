def add_one(some_list):
    str_number = "".join([str(digit) for digit in some_list])

    incremented_number = int(str_number) + 1

    return [int(char) for char in str(incremented_number)]


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
    assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
    assert add_one([0]) == [1], 'Test3'
    assert add_one([9]) == [1, 0], 'Test4'

    print("OK")