import string

ALPHABET = list(dict.fromkeys(string.ascii_lowercase, 0).keys())


def pangram(value: str):
    for e in value:
        if e in ALPHABET:
            ALPHABET.remove(e)

    if len(ALPHABET) == 0:
        return "pangram"

    return "not pangram"


if __name__ == "__main__":
    value = input().strip().replace(" ", "").lower()
    r = pangram(value)
    print(r)