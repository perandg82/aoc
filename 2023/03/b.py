#!/usr/bin/env python3

import re

def find_indexes(line)
    i = 0
    nums = []
    while i < len(line):
        try:
            nums.append(line[i:].index("*"))
        except ValueError:
            break
    return nums

def find_numbers(line):
    i = 0
    nums = []
    while i < len(line):
        if line[i].isdigit():
            s = i 
            try:
                while line[i].isdigit():
                    i+=1
            except IndexError:
                pass
            nums.append((s,i))
        i += 1
    return nums


def has_symbol(pattern):
    print("Testing {}".format(pattern))
    for c in pattern:
        if c != "." and not c.isdigit():
            print("Abort on char {}".format(c))
            return True
    return False

#f = open("testinput.txt", "r")
f = open("inputa.txt", "r")
d = f.readlines()
f.close()
print(d)
sum = 0
t = "."*len(d[0])
d.insert(0,t)
d.append(t)

for line in d[1:-1]:
    index = d.index(line)
    last_index = len(line)-1
    nums = find_indexes(line)

print(sum)
