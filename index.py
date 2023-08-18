
def insertion_sort(data: list[int]):
    output = data
    
    for i in range(len(data)):
        if i == len(data) -1: return output
        
        # for j in range(len(data[i:])):
        #     print(data[j])
    
    return output

if __name__ == "__main__":
    x = insertion_sort([5, 2, 4, 6, 1, 3])
    print(x)
    
    
# 5, 2, 4, 6, 1, 3

# 5 > 2 = true

# [2, 5, 4, 6, 1, 3]