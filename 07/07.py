import numpy as np

def value(x) -> bool:
    #print("  {}".format(repr(x)))
    try:
        int(x)
        return np.uint16(x)
    except ValueError:
        if x not in wires:
            return np.uint16(0)
        return wires[x]

with open("input.txt", "r") as f:
    lines = f.readlines()

wires = dict()

for l in lines:
    #print(repr(l))

    operation, w = l.split(" -> ")
    os = operation.split(" ")

    w = w[:-1]
    wires[w] = value(w)

    if len(os) == 1:
        wires[w] = value(os[0])
   
    elif len(os) == 2:
        wires[w] = ~ value(os[1])

    else:
        lhs = value(os[0])
        rhs = value(os[2])

        if os[1] == "LSHIFT":
            wires[w] = lhs << rhs
        elif os[1] == "RSHIFT":
            wires[w] = lhs >> rhs
        elif os[1] == "AND":
            wires[w] = lhs & rhs
        elif os[1] == "OR":
            wires[w] = lhs | rhs

    #print(wires)
        
print(wires["a"])

#print()

#print(wires)
        

