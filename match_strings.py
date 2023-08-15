def matchingStrings(strings: list[str], queries:  list[str]):
    return [strings.count(value) for _, value in enumerate(queries)]

if __name__ == "__main__":
    size_strings = int(input())
    strings = [input ()for _ in range(size_strings)]
    size_queries = int(input())
    queries = [input ()for _ in range(size_queries)]
    response = matchingStrings(strings, queries)
    [print(value) for value in response]