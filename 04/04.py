import hashlib

input = "ckczppom"
i = 0

while True:
    h = hashlib.md5( ( input+str(i) ).encode() )

    # 6 -> 5  and  "00000" for part 1
    if h.hexdigest()[:6] == "000000":
        print(i)
        break;

    i += 1