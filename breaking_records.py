
from typing import List


def breaking_records(data: List[int]):
    breaking_min = 0
    breaking_max = 0

    scores = []

    for i in range(1, len(data)+1):
        scores.append((max(data[:i]), min(data[:i])))

    max_value = scores[0][0]
    min_value = scores[0][1]

    for i in range(1, len(scores)):
        current_max = scores[i][0]
        if current_max > max_value:
            max_value = current_max
            breaking_max += 1

        current_min = scores[i][1]
        if current_min < min_value:
            min_value = current_min
            breaking_min += 1

    return [breaking_max, breaking_min]


if __name__ == "__main__":
    number_of_games = input()
    values = input()
    formatted = [int(e) for e in values.split(" ")]

    scores = breaking_records(formatted)
    print(scores)