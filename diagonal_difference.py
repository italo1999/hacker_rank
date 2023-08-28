def diagonal_difference(data):
    response = (0, 0)

    for layer1, _ in enumerate(data):
        left = data[layer1][layer1]
        right = data[layer1][len(data)-1-layer1]

        sum_left = response[0] + left
        sum_right = response[1] + right

        response = (sum_left, sum_right)

    return abs(response[0] - response[1])


if __name__ == "__main__":
    n = int(input().strip())

    data = []
    for _ in range(n):
        data.append(list(map(int, input().rstrip().split())))

    response = diagonal_difference(data)
    print(response)