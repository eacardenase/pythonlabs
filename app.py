def reverse(text: str) -> str:
    return text if text == "" else text [-1] + reverse(text[:-1])

def main():
    print(reverse("straw"))
    print(reverse("hello"))
    print(reverse("world"))

if __name__ == "__main__":
    main()