#!/usr/bin/env python3

import re

index_re = re.compile("Card\s+(\d*):")

#f = open("testinput.txt", "r")
f = open("inputa.txt", "r")
d = f.readlines()
f.close()

sum = 0

for line in d:
    try:
        index = index_re.search(line).groups()[0]
    except Exception as e:
        print("Caught {}, invalid line: {}".format(e, line))
        continue

    winning, mine = line.split(":")[1].split("|")
    results = 0
    for num in mine.split():
        results += winning.count(" {} ".format(num))

    print()
    print(line[:-1])
    print("Got {} results".format(results))
    if results > 0:
        sum += pow(2,results-1)

print(sum)
