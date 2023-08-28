
def countingValleys(data: list[str]):
    c = 0
    last = 0
    deep = False
    
    for layer in range(2, len(data)+1):
        
        to_evaluate = data[last:layer]
        
        U = to_evaluate.count("U")
        D = to_evaluate.count("D")

        if to_evaluate[:-1].count("U") < to_evaluate[:-1].count("D"): 
            deep = True                                                                                                                                                                                                                                                                                                               
        
        if U == D:
            if len(to_evaluate) == 2:
                if to_evaluate[0] == "D" and to_evaluate[1] == "U":
                    if deep == True:
                        last = last + len(to_evaluate)
                        c +=1
            else:
                if deep == True:
                    last = last + len(to_evaluate)
                    c +=1
    
    return c

if __name__ == "__main__":
    input()
    value = input().strip()
    x = countingValleys(list(value))
    print(x)