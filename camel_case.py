
def camelCase(*, operation:str, type_operation: str, string: str):
    if operation == "S" and type_operation == "M":
        return SM(string)
    
    if operation == "C" and type_operation == "V":
        return CV(string)
    
    if operation == "C" and type_operation == "C":
        return CC(string)
    
    if operation == "S" and type_operation == "C":
        return SC(string)
    
    if operation == "C" and type_operation == "M":
        return CM(string)
    
    if operation == "S" and type_operation == "V":
        return SV(string)

def SV(string: str):
    r = []
    for e in string:
        if e.isupper():
            r.append(" ")
        r.append(e.lower())
    
    return "".join(r).strip()

def CM(string: str):
    r = [e.title() if l > 0 else e for l, e in enumerate(string.split(" "))]
    
    return "".join(r).__add__("()").strip()

def SC(string: str):
    r=[]
    
    for  l, e in enumerate(string):
        if l > 0 and e.isupper():
            r.append(" ")
        r.append(e.lower())
        
    return "".join(r)


def CC(string: str):
    r = [e.title() for e in string.split(" ")]
    
    return "".join(r).replace(" ", "")

def CV(string:str):
    r = [e.upper() if l> 1 and string[l-1] == " " else e for l, e in enumerate(string)]
    
    return "".join(r).replace(" ", "")

def SM(string:str):
    r = []
    for e in string:
        if not e.isupper(): r.append(e)
        else: 
            r.append(" ")
            r.append(e.lower())

    return "".join(r).replace("()", "")


if __name__ == "__main__":
    ar = input().split(";")
    r = camelCase(operation=ar[0], type_operation=ar[1], string=ar[2])
    print(r)