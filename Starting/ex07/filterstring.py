import sys


def filter_words(text: str, number: int) -> list:
    """Return words whose length is greater than number."""
    check_length = lambda word: len(word) > number
    return [word for word in text.split() if check_length(word)]


def main() -> None:
    """Handle arguments and print filtered words."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        number = int(sys.argv[2])

        if not isinstance(text, str):
            raise AssertionError("the arguments are bad")

        print(filter_words(text, number))

    except (ValueError, TypeError, AssertionError):
        print("AssertionError: the arguments are bad")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()