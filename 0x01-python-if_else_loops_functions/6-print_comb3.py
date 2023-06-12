#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a+1, 10):
        num = "\n" if (a == 8 and b == 9) else ", "
        print("{:d}{:d}{}".format(a, b, num), end="")
