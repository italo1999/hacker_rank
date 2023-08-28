def flip(value: int):
    
    # Crear una lista para almacenar los bytes invertidos
    byte_array = [0] * 32
    
    # Llenar la lista con los bytes invertidos
    for i in range(32):
        byte_array[i] = 1 - value  # Invertir el valor del bit
        
    # Calcular el valor decimal basado en los bytes invertidos
    result = 0
    for i in range(32):
        result += byte_array[i] * (2 ** i)
    
    return result     

if __name__ == "__main__":
    op = int(input())
    value = [int(input()) for _ in range(op)]
    response= [value[e] ^ ((1 << 32) - 1) for e in range(len(value))]
    [print(r) for r in response]

    


# valor 1 --> 4294967294
# valor 2 --> 4294967295 