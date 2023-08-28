class Operation:
    STR = ""
    action: str
    value: str

    def __init__(self, action: str, value: str):
        self.action = action
        self.value = value

    def trigger(self):
        return getattr(self, self.action)()

    def SM(self):
        data = []
        for layer, e in enumerate(self.value):
            if e.istitle():
                data.insert(layer, " ")
                data.insert(layer+1, e.lower())
            else:
                data.append(e)

        return self.STR.join(data).replace("()", "")

    def CV(self):
        data = []
        for layer, e in enumerate(self.value):
            if layer > 1:
                if self.value[layer-1] == " ":
                    data.insert(layer, e.title())
                else:
                    data.append(e)
            else:
                data.append(e)

        return self.STR.join(data).replace(" ", "")

    def CC(self):
        data = []
        for layer, e in enumerate(self.value):
            if layer == 0:
                data.append(e.title())
            elif layer > 1 and self.value[layer-1] == " ":
                data.append(e.title())
            else:
                data.append(e)

        return self.STR.join(data).replace(" ", "")

    def SC(self):
        data = []
        for e in self.value:
            if e.istitle():
                data.append(" ")
                data.append(e.lower())
            else:
                data.append(e)

        return self.STR.join(data).strip()

    def CM(self):
        data = []
        for layer, e in enumerate(self.value):
            if layer > 0 and self.value[layer-1] == " ":
                data.append(e.title())
            else:
                data.append(e)

        data.append("()")

        return self.STR.join(data).replace(" ", "")

    def SV(self):
        data = []
        for e in self.value:
            if e.istitle():
                data.append(" ")
                data.append(e.lower())
            else:
                data.append(e)

        return self.STR.join(data)

if __name__ == "__main__":
    while True:
        try:
            op1, op2, value = input().rstrip().split(";")
            op = Operation("".join([op1, op2]), value)

            print(op.trigger())
        except EOFError:
            break
