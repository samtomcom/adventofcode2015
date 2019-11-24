import numpy as np

def value(wires, x) -> bool:
    #print("  {}".format(repr(x)))
    try:
        int(x)
        return np.uint16(x)
    except ValueError:
        if x not in wires:
            return np.uint16(0)
        return wires[x]

def scan(wires, lines):
    for l in lines:
        #print(repr(l))

        operation, w = l.split(" -> ")
        os = operation.split(" ")

        w = w[:-1]
        wires[w] = value(wires, w)

        if len(os) == 1:
            wires[w] = value(wires, os[0])
    
        elif len(os) == 2:
            wires[w] = ~ value(wires, os[1])

        else:
            lhs = value(wires, os[0])
            rhs = value(wires, os[2])

            if os[1] == "LSHIFT":
                wires[w] = lhs << rhs
            elif os[1] == "RSHIFT":
                wires[w] = lhs >> rhs
            elif os[1] == "AND":
                wires[w] = lhs & rhs
            elif os[1] == "OR":
                wires[w] = lhs | rhs

    return wires
        

with open("input.txt", "r") as f:
    ls = f.readlines()

ws = dict()

ws = scan(ws, ls)
ws = scan(ws, ls)

print(ws["a"])

