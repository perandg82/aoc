#!/usr/bin/env python3

import re

full_pattern = re.compile("^\D*(\d).*(\d)\D*$")
short_pattern = re.compile("^\D*(\d)")

f = open("inputa.txt", "r")
d = f.readlines()
f.close()

sum = 0

for line in d:
    m = full_pattern.match(line)
    if m == None:
        m = short_pattern.match(line)
        if m == None:
            print("###########\nLine is {}###########".format(line))
            continue
    print("Line is {}".format(line))
    f = l = -1
    try:
        f = int(m.groups()[0])
        l = int(m.groups()[1])
    except Exception as e:
        print("Numbers did not convert, error is:")
        print(e)
        print("line is:")
        print(line)
    if l == -1:
        l = f
    sum += ((f * 10) + l)
    print("{} and {} gives {}".format( f, l, (f * 10) + l))

print(sum)
