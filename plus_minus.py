from typing import List

def plus_minus(collection: List[int]):
    SIZE = len(collection)
    FORMAT = "{0:.6f}"
    p = 0
    n = 0
    z = 0

    for e in collection:
        if e == 0:
            z += 1
        elif e > 0:
            p += 1
        else:
            n += 1

    return [FORMAT.format(p/SIZE), FORMAT.format(n/SIZE), FORMAT.format(z/SIZE)]


if __name__ == "__main__":
    n = input()
    values = input().split(" ")
    formatted = [int(e) for e in values]
    r = plus_minus(formatted)
    print(f"{r[0]}\n{r[1]}\n{r[2]}\n")