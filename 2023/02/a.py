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

    for set_str in sets_str.split(";"):
        m = pattern.findall(set_str)
        if len(m) == 0:
            break
        print(m)
        sets = {}
        for elem in m:
            sets[elem[1]] = int(elem[0])

        for key in sets.keys():
            if sets[key] > max[key]:
                print("{}: {} impossible, {} > {}: {}".format(game, key, sets[key], max[key], line))
                game = 0

    sum += game
    print("game {}: sum is {}".format(game, sum))
print(sum)
