def is_palindrome(text):
    clean_chars = [char.lower() for char in text if char.isalnum()]
    clean_text = "".join(clean_chars)

    return clean_text == clean_text[::-1]


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
    assert is_palindrome('0P') == False, 'Test2'
    assert is_palindrome('a.') == True, 'Test3'
    assert is_palindrome('aurora') == False, 'Test4'

    print("OK")