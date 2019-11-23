
with open("input.txt", "r") as f:
    lines = f.readlines()

nice = 0
for l in lines:
    a = False
    b = False

    for i in range(len(l) - 3):
        if l[i:i+2] in l[i+2:]:
            a = True
            break

    
    for i in range(len(l) - 2):
        if l[i] == l[i+2]:
            b = True
            break

    nice += 1 if a and b else 0

print(nice)
