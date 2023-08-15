
def divisibleSumPairs(*, n, k, ar: list[int]): 
    pairs = 0

    for i,_ in enumerate(range(len(ar))):
        for j, _ in enumerate(range(len(ar))):
            if i < j and (ar[i] + ar[j]) % k ==0:
                pairs+=1

    return pairs

if __name__ == "__main__":
    n_k_input = (input()).split(" ")
    ar_input = input("").split(" ")
    n = int(n_k_input[0])
    k = int(n_k_input[1])
    ar = [int(value.strip()) for value in ar_input]
    r = divisibleSumPairs(n=n , k= k, ar= ar)
    print(r)