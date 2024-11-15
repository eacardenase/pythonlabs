def reverse(text: str) -> str:
    return text if text == "" else text [-1] + reverse(text[:-1])

def is_palindrome(text: str) -> bool:
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

def main():
    # print(reverse("straw"))
    # print(reverse("hello"))
    # print(reverse("world"))
    print(is_palindrome("world"))
    print(is_palindrome("seres"))
    print(is_palindrome("reviver"))
    print(is_palindrome("coke"))
    print(is_palindrome("racecar"))

if __name__ == "__main__":
    main()