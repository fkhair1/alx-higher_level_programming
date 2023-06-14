#!/usr/bin/python3
if __name__ != "__main__":
    exit()
from sys import argv
a = 0
for i in argv[1:]:
    a = a + int(i)
print(f"{a:d}")
