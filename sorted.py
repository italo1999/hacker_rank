from typing import List


def sorting(data: List[int]):
    for layer1 in range(1, len(data)):
        data_evaluate = data[:layer1+1]
        len_data_evaluate = len(data_evaluate)

        last = data[len(data_evaluate)-1]

        for layer2 in range(1, len_data_evaluate):
            previous = data_evaluate[len(range(1, len_data_evaluate))-layer2]

            if last < previous:
                data[len(range(1, len_data_evaluate))-layer2] = last
                data[len(range(1, len_data_evaluate))-layer2+1] = previous

    return data


if __name__ == "__main__":
    x = sorting([5, 4, 1, 6, 3, 2])
    print(x)