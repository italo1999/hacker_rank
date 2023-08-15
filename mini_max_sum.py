
def miniMaxSum(collection: list[int]):
    total = [sum(collection) - ele for ele in collection]

    return [min(total), max(total)]


if __name__ == "__main__":
    collection = list(map(int, input().rstrip().split()))
    r = miniMaxSum(collection)
    print(f"{r[0]} {r[1]}")