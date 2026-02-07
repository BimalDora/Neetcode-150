def is_palindrome(string: str) -> bool:
    """
    Checks if a word is palindrome

    Input: A String
    Output: Bool (True/False)

    """
    l = 0
    r = len(string)-1
    while l < r:
        if not string[l].isalnum():
            l += 1
            continue
        elif not string[r].isalnum():
            r -= 1
            continue

        if string[l].lower() != string[r].lower():
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    test_string = "A man, a plan, a canal: Panama"
    print(f"The input string: {test_string}; Valid palindrome?: {is_palindrome(test_string)}")