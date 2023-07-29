#!/usr/bin/python3
''' 2-append_write.py '''


def append_write(filename="", text=""):
    ''' Append file '''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
