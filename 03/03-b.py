
with open("input.txt", "r") as f:
    line = f.readline()

houses = {(0,0)}

x, y, rX, rY = 0, 0, 0, 0

count = 0
for char in line:

    if (count % 2) == 0:
        if char == "^":
            x += 1
        elif char == ">":
            y += 1
        elif char == "v":
            x -= 1
        elif char == "<":
            y -= 1

        houses.add( (x,y) )
    else:
        if char == "^":
            rX += 1
        elif char == ">":
            rY += 1
        elif char == "v":
            rX -= 1
        elif char == "<":
            rY -= 1

        houses.add( (rX, rY) )

    count += 1

print(len(houses))