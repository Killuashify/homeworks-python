def second_index(text, some_str):
    first_index = text.find(some_str)

    if first_index == -1:
        return None

    second_idx = text.find(some_str, first_index + 1)

    return second_idx if second_idx != -1 else None


if __name__ == "__main__":
    assert second_index("sims", "s") == 3, 'Test1'
    assert second_index("find the river", "e") == 12, 'Test2'
    assert second_index("hi", "h") is None, 'Test3'
    assert second_index("Hello, hello", "lo") == 10, 'Test4'

    print('OK')