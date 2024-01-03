#!/usr/bin/env python3

import re

pattern = re.compile("(\w*) = \((\w*), (\w*)\)")

f = open("inputa.txt", "r")
d = f.readlines()
f.close()

instr = d.pop(0)[:-1]
d.pop(0)

sum = 0

dindex = []
for elem in d:
    if len(elem) == 0:
        continue
    dindex.append(elem.split()[0])

ii = 0
id = dindex.index("AAA")
print(len(instr))
next = "AAA"
while True:
    try:
        char = instr[ii]
    except IndexError as e:
        print("Need to wrap, ii is {}".format(ii))
        ii = 0
        char = instr[ii]
    m = pattern.search(d[id])
    if m == None:
        print("Something went awry!")
        break
    print("{}: {}".format(char, d[id][:-1]))
    if next != m.groups()[0]:
        print("Mismatch! {} <> {}".format(next, m.groups()[0]))
        break
    next = ""
    if instr[ii] == "L":
        next = m.groups()[1]
    elif instr[ii] == "R":
        next = m.groups()[2]
    else:
        print("Something went to shit, ii is {}, len groups is {}".format(ii, len(m.groups())))
        break
    id = dindex.index(next)
    sum += 1
    ii += 1
    if next == "ZZZ":
        break

print(sum)
