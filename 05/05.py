
with open("input.txt", "r") as f:
    lines = f.readlines()

nice = 0
for l in lines:
    if "ab" in l or "cd" in l or "pq" in l or "xy" in l:
        continue
    
    vowels = l.count("a") + l.count("e") + l.count("i") + l.count("o") + l.count("u")

    if vowels < 3:
        continue
    
    for i in range(len(l) - 1):
        if l[i] == l[i+1]:
            nice += 1
            break

print(nice)
