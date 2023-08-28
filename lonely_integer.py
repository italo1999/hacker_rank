from typing import List


def lonely_integer(data: List[int]):
    for value in data:
        occurrences = data.count(value)
        if occurrences == 1:
            return value


if __name__ == "__main__":
    n = input().strip()
    data = list(map(int, input().rstrip().split()))
    x = lonely_integer(data)
    print(x)