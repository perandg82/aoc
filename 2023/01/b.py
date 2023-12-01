#!/usr/bin/env python3

import re

pattern = re.compile("(one|two|three|four|five|six|seven|eight|nine|\d)")

f = open("inputa.txt", "r")
#f = open("testinput.txt", "r")
d = f.readlines()
f.close()

lut=["ph","one","two","three","four","five","six","seven","eight","nine"]
sum = 0

for line in d:
    m = pattern.findall(line)
    print(m)
    if len(m) == 0:
        print("###########\nLine is {}###########".format(line))
        continue
    try:
        f = int(m[0])
    except Exception as e:
        f = lut.index(m[0])
    try:
        l = int(m[-1])
    except Exception as e:
        l = lut.index(m[-1])
    print("numbers are {} and {}, line is {}".format(f, l, line))
    sum += ((f * 10) + l)

print(sum)
