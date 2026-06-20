import string


def generate_hashtag(user_input):
    titled_input = user_input.title()

    clean_chars = []
    for char in titled_input:
        if char not in string.punctuation and not char.isspace():
            clean_chars = clean_chars + [char]

    clean_string = "".join(clean_chars)

    hashtag = "#" + clean_string

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


test_cases = [
    'Python Community',
    'i like python community!',
    'Should, I. subscribe? Yes!',
    'Lorem ipsum dolor sit amet consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.'
]

if __name__ == "__main__":
    print("--- Hashtag Generator Test Results ---")
    for case in test_cases:
        result = generate_hashtag(case)
        print(f"'{case}' -> {result}")