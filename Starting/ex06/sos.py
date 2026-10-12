import sys


def get_morse() -> dict:
    """Return the Morse code dictionary."""
    return {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }


def encode_morse(text: str) -> str:
    """Convert a valid string into Morse code."""
    morse = get_morse()
    result = []

    for char in text.upper():
        if char not in morse:
            raise ValueError
        result.append(morse[char])

    return " ".join(result)


def main() -> None:
    """Handle arguments and print the Morse code."""
    try:
        if len(sys.argv) != 2:
            print("AssertionError: the arguments are bad")
            return

        print(encode_morse(sys.argv[1]))

    except (ValueError, TypeError):
        print("AssertionError: the arguments are bad")
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()