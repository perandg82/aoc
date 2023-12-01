#!/usr/bin/env python3

import re

pattern = re.compile("^\D*(\d)")

f = open("inputa.txt", "r")
d = f.readlines()
f.close()

sum = 0

for line in d:
    m = pattern.match(line)
    if m == None:
        continue
    try:
        pass
    except Exception as e:
        print(e)

print(sum)
