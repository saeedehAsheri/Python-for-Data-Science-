import sys


def count_characters(text: str) -> None:
    """Count and display different character types in a text."""
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digits = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif not char.isalnum():
            punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main() -> None:
    """Handle arguments and start the character counter."""
    try:
        if len(sys.argv) > 2:
            print("AssertionError: more than one argument is provided")
            return

        if len(sys.argv) == 1 or sys.argv[1] == "":
            print("What is the text to count?")
            text = sys.stdin.read()
        else:
            text = sys.argv[1]

        count_characters(text)

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()