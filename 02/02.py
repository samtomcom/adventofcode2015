


with open("input.txt", "r") as f:
    lines = f.readlines()

count = 0

wrapping = 0
ribbon = 0

for line in lines:
    x, y, z = line.split("x")
    x, y, z = int(x), int(y), int(z)

    s1 = x*y
    s2 = x*z
    s3 = y*z

    extra = min(s1, s2, s3)

    wrapping += 2*s1 + 2*s2 + 2*s3 + extra

    volume = x*y*z
    sides = x + y + z - max(x, y, z)

    ribbon += 2*sides + volume

    

print("w: {}".format(wrapping))
print("r: {}".format(ribbon))
