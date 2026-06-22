def common_elements():
    list_mult_3 = [i for i in range(100) if i % 3 == 0]

    list_mult_5 = [i for i in range(100) if i % 5 == 0]

    result_set = set(list_mult_3) & set(list_mult_5)

    return result_set

if __name__ == "__main__":
    my_result = common_elements()

    print("Result of the function")
    print(f"The function returned: {my_result}")
    print("-" * 35)

    assert my_result == {0, 75, 45, 15, 90, 60, 30}
    print('Autotest passed successfully: OK')