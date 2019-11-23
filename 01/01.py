
with open("input.txt", "r") as f:
    fi = f.readlines()

line = fi[0]

print(line.count("(") - line.count(")"))