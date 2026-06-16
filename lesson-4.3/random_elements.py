import random


def generate_and_pick_elements():

    list_length = random.randint(3, 10)

    source_list = [random.randint(1, 10) for _ in range(list_length)]

    result_list = [source_list[0], source_list[2], source_list[-2]]

    return source_list, result_list


if __name__ == "__main__":
    print("Random Elements Picker Test Results  ")

    for i in range(1, 4):
        original, final = generate_and_pick_elements()
        print(f"Run {i}: {original} == {final}")