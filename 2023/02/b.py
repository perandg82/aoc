#!/usr/bin/env python3

import re

pattern = re.compile("(\d+) (blue|red|green)\s*")

f = open("inputa.txt", "r")
#f = open("testinput.txt", "r")
d = f.readlines()
f.close()

sum = 0
max = {"red": 12,"green": 13, "blue": 14}

for line in d:
    game_str, sets_str = line.split(":")
    game = int(game_str.split(" ")[1])
    print("Found game nr {}".format(game))

    min = {"red": 0,"green": 0, "blue": 0}
    for set_str in sets_str.split(";"):
        m = pattern.findall(set_str)
        if len(m) == 0:
            break
        print(m)
        sets = {}
        for elem in m:
            sets[elem[1]] = int(elem[0])

        for key in sets.keys():
            if sets[key] > min[key]:
                min[key] = sets[key]
    p = 1
    print(min)
    for n in min.values():
        p *= n

    sum += p
    print("game {}: sum is {}".format(p, sum))
print(sum)
