
with open("input.txt", "r") as f:
    fi = f.readlines()

line = fi[0]

floor = 0
count = 0
for c in line:
    count += 1

    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    

    if floor == -1:
        print(count)
        break