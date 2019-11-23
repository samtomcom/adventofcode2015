
with open("input.txt", "r") as f:
    line = f.readline()

houses = {(0,0)}

x, y = 0, 0
for char in line:
    if char == "^":
        x += 1
    elif char == ">":
        y += 1
    elif char == "v":
        x -= 1
    elif char == "<":
        y -= 1

    houses.add( (x,y) )

print(len(houses))