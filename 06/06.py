
grid = [ [0 for i in range(1000)] for i in range(1000) ]

with open("input.txt", "r") as f:
    lines = f.readlines()

for l in lines:
    index = 1 if l[1] == "o" else 2

    ls = l.split(" ")

    x0, y0 = ls[index].split(",")
    x1, y1 = ls[index+2].split(",")

    x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))

    if l[1] == "u":
        if ls[1] == "on":
            c = 1

        if ls[1] == "off":
            c = 0

        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                grid[x][y] = c
    else:
        for x in range(x0, x1+1):
            for y in range(y0, y1+1):
                grid[x][y] = 0 if grid[x][y] else 1

count = 0
for line in grid:
    count += line.count(1)

print(count)

